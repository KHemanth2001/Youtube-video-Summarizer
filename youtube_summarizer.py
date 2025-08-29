# youtube_summarizer.py
from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs

def extract_video_id(url: str) -> str:
    """Extract the video ID from a YouTube URL."""
    parsed_url = urlparse(url)

    if parsed_url.hostname in ["www.youtube.com", "youtube.com"]:
        if parsed_url.path == "/watch":
            return parse_qs(parsed_url.query).get("v", [None])[0]
        elif parsed_url.path.startswith("/embed/"):
            return parsed_url.path.split("/")[2]
        elif parsed_url.path.startswith("/shorts/"):
            return parsed_url.path.split("/")[2]
    elif parsed_url.hostname == "youtu.be":
        return parsed_url.path.lstrip("/")
    return None

def get_youtube_transcript(url: str) -> str:
    video_id = extract_video_id(url)
    if not video_id:
        return "❌ Could not extract video ID."

    try:
        ytt_api = YouTubeTranscriptApi()
        transcript = ytt_api.fetch(video_id, languages=["en"])

        # ✅ Extract only the text from snippets
        if hasattr(transcript, "snippets"):
            text = " ".join(snippet.text for snippet in transcript.snippets)
        elif hasattr(transcript, "lines"):
            text = " ".join(line.text for line in transcript.lines)
        elif hasattr(transcript, "data"):
            text = " ".join(entry["text"] for entry in transcript.data)
        else:
            text = str(transcript)

        return text.strip()

    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    url = "https://www.youtube.com/watch?v=csWluHwfsB8"  # replace with your URL
    plain_text = get_youtube_transcript(url)
    print(plain_text)

    # Optional: Save to file
    with open("transcript.txt", "w", encoding="utf-8") as f:
        f.write(plain_text)