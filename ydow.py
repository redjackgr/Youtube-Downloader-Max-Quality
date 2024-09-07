import yt_dlp
import os

def download_youtube_video(url, save_path='.', audio_only=False):
    try:
        # Καθορισμός επιλογών για κατέβασμα
        ydl_opts = {
            'outtmpl': f'{save_path}/%(title)s.%(ext)s',
            'format': 'bestvideo+bestaudio/best',  # Λήψη βίντεο και ήχου σε καλύτερη ποιότητα
            'merge_output_format': 'mp4',  # Εξασφάλιση μορφής MP4
            'noplaylist': True,  # Αποφυγή κατεβάσματος ολόκληρων playlists
        }

        # Αν ο χρήστης θέλει μόνο τον ήχο (MP3)
        if audio_only:
            ydl_opts.update({
                'format': 'bestaudio/best',  # Λήψη μόνο του καλύτερου ήχου
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',  # Μετατροπή σε MP3
                    'preferredquality': '192',  # Ποιότητα ήχου (192 kbps)
                }],
                'outtmpl': f'{save_path}/%(title)s.%(ext)s'  # Αποθήκευση ως mp3
            })

        # Εκτέλεση της λήψης
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            print(f"Downloaded '{info_dict['title']}' successfully!")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Ζητάμε από τον χρήστη το URL του βίντεο
    video_url = input("Enter the YouTube video URL: ").strip()
    
    # Προαιρετικά: Ζητάμε το φάκελο αποθήκευσης (προεπιλογή ο τρέχων κατάλογος)
    save_path = input("Enter the path to save the video/audio (default is current directory): ").strip() or '.'
    
    # Ζητάμε από τον χρήστη αν θέλει να κατεβάσει μόνο τον ήχο (MP3)
    audio_only = input("Do you want to download only audio as MP3? (yes/no): ").strip().lower() == 'yes'
    
    # Κατεβάζουμε το βίντεο ή τον ήχο
    download_youtube_video(video_url, save_path, audio_only)
