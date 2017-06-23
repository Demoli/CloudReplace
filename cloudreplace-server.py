from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify

import json
import markdown

app = Flask(__name__)


class InvalidRequest(Exception):
    status_code = 400

    def __init__(self, message, status_code=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code

    def to_dict(self):
        rv = {}
        rv['error'] = self.message
        return rv


@app.route('/')
def hello_world():
    with open('README.md') as file:
        readme = file.read()
    return markdown.markdown(readme)


@app.route('/replace', methods=['POST'])
def replace():
    data = json.loads(request.data)
    expected_args = ['subject', 'search', 'replace']
    missing_args = [param for param in expected_args if param not in list(data.keys())]
    if (len(missing_args)):
        raise InvalidRequest("Missing argument(s) {}".format(', '.join(missing_args)))
    data['result'] = data['subject'].replace(data['search'], data['replace'])
    return jsonify(data)


@app.errorhandler(InvalidRequest)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


if __name__ == '__main__':
    app.run(debug=True, threaded=True)
