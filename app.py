from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

from app.services import *
from model.enums import *

app = Flask(__name__)
cors = CORS(app)

services = Services()


#@app.route('/', methods=['GET'])
#def serve_form():
 #   return render_template('web/mlt.html')


@app.route('/translate', methods=['POST'])
def translate_word():
    data = request.get_json()
    word = data.get('word')
    source_language = LANG(data.get('source_language'))
    target_language = LANG(data.get('target_language'))

    translation = services.translate_word(word, source_language, target_language)

    if translation:
        return jsonify(translation)
    else:
        return jsonify({'message': 'Translation not found'}), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
