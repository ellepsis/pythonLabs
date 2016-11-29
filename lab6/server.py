from bottle import route, run, template, static_file, post, request, redirect
import sys
import rss_worker
import rss_db

rss_db_connection = rss_db.rss_db()


@route("/")
def index_request():
    redirect("/channels_list/")
    return


@route("/channels_list/")
def page_request():
    channels = rss_db_connection.find_all_channels()
    res = ""
    res += '<form action="/add_channel/" method="POST"> <p>Добавить канал ' \
           '<input type="text" name="channel_url">' \
           '<input type="submit" value="Добавить">' \
           '</p></form>'
    for channel in channels:
        res += '<a href="http://localhost:8080/' + str(channel.id) + '/0/">' + channel.title + '</a><br/>\n'
    return res

@post("/add_channel/")
def add_channel():
    val = request.forms.get("channel_url")
    rss_worker.add_new_channel(rss_db_connection, val)
    return

@route("/<channel_id>/<page>/")
def change_complexity(channel_id, page):
    channel = rss_db_connection.find_channel_by_id(channel_id)[0]
    page = int(page)
    posts = rss_db_connection.find_posts(channel.id, 10, page)
    res = "<H3>" + channel.title + "</H3>"
    res += '<H2><a href="http://localhost:8080/' + channel_id + '/' + \
           str(0 if page - 1 < 0 else page - 1) + '/">Назад</a></H2>'
    res += '<H2><a href="http://localhost:8080/' + channel_id + '/' + str(page + 1) + '/">Вперед</a></H2>'
    for post in posts:
        res += '<H2><a href="' + post.link + '">' + post.title + "</a></H2>"
        res += "<p>" + post.data + "</p>"
        res += '<H4>' + str(post.pub_date) + "</H4>"
    res += '<H2><a href="http://localhost:8080/' + channel_id + '/' + \
           str(0 if page - 1 < 0 else page - 1) + '/">Назад</a></H2>'
    res += '<H2><a href="http://localhost:8080/' + channel_id + '/' + str(page + 1) + '/">Вперед</a></H2>'
    return res


def main(args):
    #rss_worker.add_new_channel(rss_db_connection, "https://habrahabr.ru/rss/interesting/")
    #rss_worker.update_all_channels(rss_db_connection)
    run(host="localhost", port=8080)


if __name__ == '__main__':
    main(sys.argv)
