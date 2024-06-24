# Video to GIF with Subtitles

## Overview

The Video to GIF with Subtitles project aims to automate the process of adding subtitles to a video, segmenting the video into smaller clips based on timestamps from an SRT file, and converting these video segments into GIFs. This project is useful for creating short, captioned video clips or GIFs from a longer video, which can then be used for sharing on social media, in presentations, or for any other purposes.

### Key Features

1. **Transcription with Whisper**: 
   - The project begins by using Whisper for transcription. Whisper is an automatic speech recognition (ASR) system trained on 680,000 hours of multilingual and multitask supervised data collected from the web. This ensures improved robustness to accents, background noise, and technical language. It supports transcription in multiple languages and translation into English.

2. **Adding Subtitles**: 
   - Subtitles are added to the video using an SRT file. This is done using FFmpeg to overlay the subtitles directly onto the video. The subtitle font size can be customized to ensure readability.

3. **Video Segmentation**: 
   - The video is segmented into smaller clips based on timestamps extracted from the SRT file. This allows for creating precise video segments that correspond to specific parts of the original video.

4. **GIF Conversion**: 
   - Each segmented video clip is converted into a GIF. This provides a convenient format for sharing short clips on various platforms.

### Implementation

The project is implemented using Python and the following key libraries:
- **MoviePy**: For video processing, including reading, writing, and manipulating video files.
- **FFmpeg**: For adding subtitles to the video.
- **Whisper**: For transcribing the audio in the video into text.

## Requirements

- Python 3.x
- [Whisper](https://github.com/openai/whisper)
- [MoviePy](https://github.com/Zulko/moviepy)
- [FFmpeg](https://ffmpeg.org/download.html)
