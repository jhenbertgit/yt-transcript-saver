import os
from youtube_transcript_api import YouTubeTranscriptApi

def save_youtube_transcript(video_id: str, output_dir: str = "output", filename: str = "transcript.txt") -> None:
    """
    Fetch a YouTube video transcript and save it to a .txt file in the specified directory.
    
    Args:
        video_id (str): YouTube video ID (e.g., "yqqsIhCt1D0").
        output_dir (str): Output directory name (default: "output").
        filename (str): Output filename (default: "transcript.txt").
    """
    try:
        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)
        
        # Fetch transcript
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=["en", "fil"])
        full_text = "\n".join([entry["text"] for entry in transcript])
        
        # Save to file
        output_path = os.path.join(output_dir, filename)
        with open(output_path, "w", encoding="utf-8") as file:
            file.write(full_text)
        
        print(f"✅ Transcript saved to '{output_path}'")
    except Exception as e:
        print(f"❌ Error: {e}")

# Example usage
video_id = "ocE5oHfE2uo"  # Replace with your video ID
save_youtube_transcript(video_id, filename="yt_transcript_ra_10173.txt")