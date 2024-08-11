import yt_dlp
import os

def download_youtube_video(url, save_path='.'):
    try:
        # Define download options
        ydl_opts = {
            'outtmpl': f'{save_path}/%(title)s.%(ext)s',
            'format': 'bestvideo+bestaudio/best',  # Download best quality by default
            'merge_output_format': 'mp4',  # Ensure output is in mp4 format
            'noplaylist': True,  # Avoid downloading playlists
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            print(f"Downloaded '{info_dict['title']}' successfully!")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Ask the user for the YouTube video URL
    video_url = input("Enter the YouTube video URL: ").strip()
    
    # Optional: Ask the user for the save path (default is current directory)
    save_path = input("Enter the path to save the video (default is current directory): ").strip() or '.'
    
    # Download the video
    download_youtube_video(video_url, save_path)