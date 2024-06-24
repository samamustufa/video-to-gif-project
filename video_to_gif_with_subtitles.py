import subprocess

# Paths to your input video/GIF and subtitle files
video_path = "input_video.mp4"  # or input.gif
subtitle_path = "subtitles.srt"
output_path = "output_gifs/output.mp4"  # or output.gif

# Construct the ffmpeg command
ffmpeg_command = [
    'ffmpeg',
    '-i', video_path,
    '-vf', f"subtitles={subtitle_path}",
    output_path
]

try:
    # Run the command
    subprocess.run(ffmpeg_command, check=True, capture_output=True, text=True)
    print("Subtitles added successfully!")
except subprocess.CalledProcessError as e:
    print("Error occurred:")
    print(e.stderr)
