import subprocess
import re
import os
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.editor import VideoFileClip

# Function to convert SRT timestamp to seconds
def srt_to_seconds(timestamp):
    h, m, s = map(float, re.split(r'[:,]', timestamp))
    return h * 3600 + m * 60 + s

# Function to extract timestamps from SRT file
def extract_timestamps_from_srt(srt_file):
    timestamps = []
    with open(srt_file, 'r') as file:
        lines = file.readlines()
        for i in range(0, len(lines), 4):
            start, end = lines[i+1].strip().split(' --> ')
            start_seconds = srt_to_seconds(start.split(',')[0])
            end_seconds = srt_to_seconds(end.split(',')[0])
            timestamps.append((start_seconds, end_seconds))
    return timestamps

# Function to segment video based on extracted timestamps
def segment_video(video_file, timestamps, output_folder='segments'):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    video = VideoFileClip(video_file)
    for i, (start, end) in enumerate(timestamps):
        clip = video.subclip(start, end)
        segment_path = os.path.join(output_folder, f'segment_{i}.mp4')
        clip.write_videofile(segment_path, fps=30)  # Adjust FPS as needed
        print(f'Segment created: {segment_path}')

# Function to convert video to GIF
def convert_to_gif(video_file, gif_file, fps=10):
    clip = VideoFileClip(video_file)
    clip.write_gif(gif_file, fps=fps)
    print(f'GIF created: {gif_file}')

# Function to add subtitles using ffmpeg with larger font size
def add_subtitles(video_path, subtitle_path, output_path, font_size=28):
    ffmpeg_command = [
        'ffmpeg',
        '-i', video_path,
        '-vf', f"subtitles={subtitle_path}:force_style='Fontsize={font_size}'",
        output_path
    ]

    try:
        subprocess.run(ffmpeg_command, check=True, capture_output=True, text=True)
        print("Subtitles added successfully!")
    except subprocess.CalledProcessError as e:
        print("Error occurred:")
        print(e.stderr)

# Main processing function
def process_video(video_path, subtitle_path, output_folder='output_gifs', segment_folder='segments', font_size=24):
    # Ensure output folders exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    if not os.path.exists(segment_folder):
        os.makedirs(segment_folder)

    # Step 1: Add subtitles to the video
    subtitled_video_path = 'subtitled_video.mp4'
    add_subtitles(video_path, subtitle_path, subtitled_video_path, font_size)

    # Step 2: Extract timestamps from SRT file and segment the video
    timestamps = extract_timestamps_from_srt(subtitle_path)
    segment_video(subtitled_video_path, timestamps, segment_folder)

    # Step 3: Convert each video segment to GIF
    for i in range(len(timestamps)):
        segment_path = os.path.join(segment_folder, f'segment_{i}.mp4')
        gif_path = os.path.join(output_folder, f'segment_{i}.gif')
        convert_to_gif(segment_path, gif_path)

# Example usage
if __name__ == "__main__":
    video_path = 'input_video.mp4'
    subtitle_path = 'subtitles.srt'
    
    process_video(video_path, subtitle_path)
