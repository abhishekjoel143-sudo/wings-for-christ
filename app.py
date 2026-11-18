from pathlib import Path
from flask import Flask, render_template

app = Flask(__name__)

TEACHER_RECORDINGS = [
    {"school": "Adarsha", "file": "Adarsha Teacher Words.mp4"},
    {"school": "Aishwarya", "file": "Aishwarya Teacher Words.mp4"},
    {"school": "Carmal Convert", "file": "Carmal Convert Teacher Words.mp4"},
    {"school": "Republic", "file": "Republic Teacher Words.mp4"},
    {"school": "St. John’s", "file": "st Johns Teacher words.mp4"},
]

STUDENT_RECORDINGS = [
    {"school": "Adarsha", "file": "Adarsha Student Words.mp4"},
    {"school": "Aishwarya", "file": "Aishwarya Student Words.mp4"},
    {"school": "Carmal Convert", "file": "Carmal convert Student Words.mp4"},
    {"school": "Republic", "file": "Republic Student Words.mp4"},
]

VIDEO_TYPES = {
    ".mp4": "video/mp4",
    ".webm": "video/webm",
    ".ogg": "video/ogg",
}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/student-feedback")
def student_feedback():
    return render_template("student_feedback.html", recordings=STUDENT_RECORDINGS)




@app.route("/gallery")
def gallery():
    video_folder = Path(app.static_folder) / "media"

    student_videos = []
    teacher_videos = []

    for video_path in sorted(video_folder.iterdir(), key=lambda item: item.name.lower()):
        video_type = VIDEO_TYPES.get(video_path.suffix.lower())

        if video_path.is_file() and video_type:
            video = {
                "title": video_path.stem.replace("_", " ").replace("-", " "),
                "file": f"media/{video_path.name}",
                "type": video_type,
            }

            filename = video_path.name.lower()

            if "student" in filename:
                student_videos.append(video)

            elif "teacher" in filename:
                teacher_videos.append(video)

    return render_template(
        "gallery.html",
        student_videos=student_videos,
        teacher_videos=teacher_videos
    )




@app.route("/faq")
def faq():
    return render_template("faq.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/teacher-feedback")
def teacher_feedback():
    return render_template("teacher_feedback.html", recordings=TEACHER_RECORDINGS)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=False, use_reloader=False)
