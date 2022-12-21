from flask import Flask, render_template, send_file
from pytube import YouTube
from io import BytesIO

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("./index.html")


@app.route("/download/<youtube_link>")
def download(youtube_link):
    buffer = BytesIO()
    video = (
        YouTube(youtube_link).streams.filter(file_extension="mp4", res="720p").first()
    )
    video.stream_to_buffer(buffer)
    buffer.seek(0)
    return send_file(
        buffer,
        as_attachment=True,
        attachment_filename="video.mp4",
        mimetype="video/mp4",
    )
