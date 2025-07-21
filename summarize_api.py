from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import Optional
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.text_rank import TextRankSummarizer
import re

app = FastAPI()

class ParagraphInput(BaseModel):
    text: str

def split_sentences(text):
    return re.split(r'(?<=[.!?])\s+', text.strip())

@app.post("/summarize/task1")
def task1(input: ParagraphInput):
    return {"summary": "Summary coming soon"}

@app.post("/summarize/task2")
def task2(input: ParagraphInput):
    sentences = split_sentences(input.text)
    if not sentences or sentences == ['']:
        return {"error": "Empty or invalid input"}
    return {"summary": " ".join(sentences[:2])}

@app.post("/summarize/task3")
def task3(input: ParagraphInput, num_sentences: int = Query(2, ge=1, le=10)):
    if not input.text.strip():
        return {"error": "Empty input"}
    parser = PlaintextParser.from_string(input.text, Tokenizer("english"))
    summarizer = TextRankSummarizer()
    summary = summarizer(parser.document, num_sentences)
    return {"summary": " ".join(str(s) for s in summary)}
