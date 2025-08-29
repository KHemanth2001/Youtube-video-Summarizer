# main.py
from transformers import pipeline
import gradio as gr
import torch
from youtube_summarizer import get_youtube_transcript

# model_path=r"D:\projects\python\GenAI\textSummarization\Models\models--sshleifer--distilbart-cnn-12-6\snapshots\a4f8f3ea906ed274767e9906dbaede7531d660ff"
# Load summarizer directly from Hugging Face Hub
summarizer = pipeline("summarization", model= "sshleifer/distilbart-cnn-12-6", torch_dtype = torch.bfloat16)

def summary(url):
    plain_text=get_youtube_transcript(url)
    response = summarizer(plain_text)
    return response[0]['summary_text']

gr.close_all()
demo = gr.Interface(fn=summary,
                    inputs=gr.Textbox(label="Enter the youtube URL", lines=1),
                    outputs=gr.Textbox(label="Youtube Summarized Text", lines=10),
                    title="@GenAI Project: TEXT SUMMARIZER",
                    description="THIS APPLICATION WILL BE USED TO SUMMARIZE THE TEXT")
demo.launch()
