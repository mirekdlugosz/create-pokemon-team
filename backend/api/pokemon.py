import os
import flask

DIRECTORY = os.path.dirname(os.path.abspath(__file__))
DEFAULT_HEADERS = {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*",
    }

app = flask.Flask(__name__)

@app.errorhandler(404)
def not_found(e):
    response_text = """{"error": "404 - no such resource"}"""
    return flask.make_response(response_text, 404, DEFAULT_HEADERS)

@app.route('/pokemon')
def api_root():
    with open(os.path.join(DIRECTORY, "pokemon-list.json"), 'r') as fh:
        js = fh.read()

    return flask.make_response(js, 200, DEFAULT_HEADERS)

@app.route('/pokemon/<pokemon_name>/moves')
def api_articles(pokemon_name):
    move_file_path = os.path.join(DIRECTORY, "moves", pokemon_name + ".json")
    if not os.path.exists(move_file_path):
        flask.abort(404)

    with open(move_file_path, 'r') as fh:
        js = fh.read()

    return flask.make_response(js, 200, DEFAULT_HEADERS)

if __name__ == '__main__':
    app.run()
