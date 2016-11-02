from bottle import route, run, template, static_file, post, request
import sys

import question_generator

global question_generator_i


def read_file(filename: str):
    try:
        file_content = open(filename, "r").read()
        return file_content
    except Exception:
        raise Exception("Can't read file " + filename)


def prepare_html():
    html = read_file("static/index.html")
    question = question_generator_i.generate_question()
    html = html.replace("{{IMAGE_URL}}", question[2])
    sel_data = "".join(
        ["<option value=" + str(i) + ">" + question[1][i] + "</option>" for i in range(1, len(question[1]))])
    html = html.replace("{{SELECT_DATA}}", sel_data)
    html = html.replace("{{QUESTION_ID}}", str(question[0]))
    return html


@route("/")
def index_request():
    html = prepare_html()
    return html


@post("/checkanswer")
def check_answer():
    question_id = int(request.forms.get("question_id"))
    answer = int(request.forms.get("selected_name"))
    res = question_generator_i.check_answer(question_id, answer)
    if res:
        return "<p>YES</p>"
    else:
        return "<p>No</p>"


def main(args):
    if len(args) < 2:
        print("First argument must be file name which contains names")
        return 1
    global question_generator_i
    question_generator_i = question_generator.QuestionGenerator(args[1], 5)
    run(host="localhost", port=8080)


if __name__ == '__main__':
    main(sys.argv)
