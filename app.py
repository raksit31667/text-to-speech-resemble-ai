from flask import Flask, jsonify, make_response, request
from datetime import datetime
from resemble import Resemble
import os

app = Flask(__name__)

Resemble.api_key(os.getenv('RESEMBLE_API_KEY'))


@app.route("/")
def hello_from_root():
    return jsonify(message='Hello from root!')


@app.route("/tts", methods=["POST"])
def tts():
    project_uuid = '25022e82'  # Earth's default project
    voice_uuid = 'c54347f8'  # Junior's voice
    api_endpoint = os.getenv('API_URL')
    callback_uri = f'{api_endpoint}/webhook'
    body = request.json['message']

    clip = Resemble.v2.clips.create_async(
        project_uuid,
        voice_uuid,
        callback_uri,
        body,
        title=str(datetime.now()),
        sample_rate=None,
        output_format=None,
        precision=None,
        include_timestamps=None,
        is_public=None,
        is_archived=None
    )
    return jsonify(clip)


@app.route("/webhook", methods=["POST"])
def webhook():
    print(request.get_json())
    return jsonify(request.get_json())


@app.errorhandler(404)
def resource_not_found(e):
    return make_response(jsonify(error='Not found!'), 404)
