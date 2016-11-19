import feedparser

import rss_channel
import rss_post
import rss_db


def parse_url(url: str):
    try:
        data = feedparser.parse(url)
    except Exception:
        raise Exception("Can't read or parse url")
    return data


def get_post(data, position: int, channel_id: int):
    post = rss_post.rss_post()
    post.channel_id = channel_id
    post.title = data['entries'][position]['title']
    post.link = data['entries'][position]['link']
    post.data = data['entries'][position]['summary']
    post.pub_date = data['entries'][position]['published']
    return post


def get_channel(data, rss_db_connection: rss_db, url):
    db_res = rss_db_connection.find_channel(url)
    if len(db_res) > 0:
        return db_res[0]
    channel = rss_channel.rss_channel()
    channel.id = None
    channel.title = data['feed']['title']
    channel.description = data['feed']['subtitle']
    channel.link = data['feed']['link']
    channel.url = url
    channel.id = rss_db_connection.insert_channel(channel)
    return channel


def update_db(data, rss_db_connection: rss_db, url):
    channel = get_channel(data, rss_db_connection, url)
    post_list = []
    for i in range(0, len(data['entries'])):
        post = get_post(data, i, channel.id)
        post_in_db = rss_db_connection.find_post(post.channel_id, post.link)
        if len(post_in_db) == 0:
            rss_db_connection.insert_post(post)


def update_all_channels(rss_db_connection: rss_db):
    res = rss_db_connection.find_all_urls()
    for url in res:
        add_new_channel(rss_db_connection, url)


def add_new_channel(rss_db_connection: rss_db, url):
    data = parse_url(url)
    update_db(data, rss_db_connection, url)
