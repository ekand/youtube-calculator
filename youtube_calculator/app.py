import os
from flask import Flask, render_template, request, redirect, url_for, session
from calculate import calculate_playlist_duration
from googleapiclient.discovery import build
import re
from dotenv import load_dotenv

load_dotenv()



def format_duration(duration):
    days, remainder = divmod(duration, 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)

    formatted_duration = ""
    if days > 0:
        formatted_duration += f"{days} days, "
    if hours > 0:
        formatted_duration += f"{hours} hours, "
    if minutes > 0:
        formatted_duration += f"{minutes} minutes, "
    if seconds > 0 or not formatted_duration:
        formatted_duration += f"{seconds} seconds"

    return formatted_duration

def extract_youtube_playlist_id(link):
    playlist_regex = (
        r'(https?://)?(www\.)?'
        r'(youtube|youtu|youtube-nocookie)\.(com|be)/'
        r'playlist\?list=([^&=%\?]+)'
    )

    match = re.match(playlist_regex, link)
    if match:
        id =  match.group(5)
        hours, minutes, seconds = calculate_playlist_duration(id)
        total_seconds = hours * 3600 + minutes * 60 + seconds
        duration = format_duration(total_seconds)
        return duration  # Return the extracted duration as the result
    else:
        return "Invalid YouTube playlist link."


app = Flask(__name__, template_folder="templates")
app.secret_key = os.getenv("FLASK_SECRET_KEY")  # Replace with a secret key for session


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/functions/playlist_duration/', methods=['POST', 'GET'])
def show_page():
    duration = None  # Initialize the duration to None

    if request.method == "POST":
        youtube_link = request.form.get("url")
        duration = extract_youtube_playlist_id(youtube_link)
        session['duration'] = duration  # Store the duration in the session
        print(duration)
    return render_template('functions/playlist_duration/index.html', duration=duration)


@app.route('/about/', methods=['GET'])
def show_about_page():
    return render_template('about/index.html')

@app.route('/functions/', methods=['GET'])
def show_functions_index():
    return render_template('functions/index.html')

if __name__ == '__main__':
    app.run(debug=True, port=8080)
