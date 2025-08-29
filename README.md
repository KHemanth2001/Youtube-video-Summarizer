# 🎬 YouTube Transcript Summarizer  

This project extracts transcripts from YouTube videos and summarizes them using a **Hugging Face Transformers model**. It provides a simple **Gradio-based web interface** where users can input a YouTube URL and get a concise summary of the video content.  

---

## 📌 Features  
- ✅ Extracts transcripts from YouTube videos (supports normal, embed, and shorts URLs).  
- ✅ Uses Hugging Face’s **BART/DistilBART** summarization models.  
- ✅ Simple **Gradio UI** for easy interaction.  
- ✅ Transcript also gets saved locally (`transcript.txt`).  

---

## 📂 Project Structure  

```
.
├── requirements.txt # Dependencies
├── youtube_summarizer.py # Extracts transcript from YouTube video
├── main.py # Runs summarization + Gradio UI
└── transcript.txt # Saved transcript (generated after running)
```


---

## ⚙️ Installation  

1. **Clone the repository**  
```bash
git clone https://github.com/KHemanth2001/Youtube-video-Summarizer.git
cd Youtube-video-Summarizer
```

2. Create a virtual environment (recommended)
```
python -m venv venv
source venv/bin/activate   # For Linux/Mac
venv\Scripts\activate      # For Windows
```

3. Install dependencies
```
pip install -r requirements.txt
```

4. Run the script with Gradio summarizer UI
```
python main.py
```

Opens a local web app (default: http://127.0.0.1:7860).
Paste a YouTube URL → Get summarized text instantly.
