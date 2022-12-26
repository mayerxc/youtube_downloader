from flask import Flask, render_template, send_file, request
from pytube import YouTube
from io import BytesIO

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/download/")
def download():
    youtube_link = request.args.get("youtube")
    print("youtube link", youtube_link)
    buffer = BytesIO()
    video = (
        YouTube(youtube_link).streams.filter(file_extension="mp4", res="720p").first()
    )
    title = video.title
    video.stream_to_buffer(buffer)
    buffer.seek(0)
    return send_file(
        buffer,
        as_attachment=True,
        download_name=f"{title}.mp4",
        mimetype="video/mp4",
    )



@app.route("/download2/<path:youtube_link2>")
def download2(youtube_link2):
    print("youtube link is:", youtube_link2)
    buffer = BytesIO()
    video = (
        YouTube(youtube_link2).streams.filter(file_extension="mp4", res="720p").first()
    )
    title = video.title
    video.stream_to_buffer(buffer)
    buffer.seek(0)
    return send_file(
        buffer,
        as_attachment=True,
        # attachment_filename="video.mp4",
        download_name=f"{title}.mp4",
        mimetype="video/mp4",
    )