import requests
import json
import re
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage


def extract_json(text):
    match = re.search(r"\{[\s\S]*\}", text)
    if not match:
        raise Exception("AI did not return valid JSON")
    return json.loads(match.group())


def generate_learning_path(api_key, youtube_url, goal):

    model = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        google_api_key=api_key
    )

    prompt = f"""
You are an expert teacher.

User goal: {goal}

Return ONLY valid JSON in this exact format:

{{
  "title": "Short playlist title",
  "videos": [
    "Professional YouTube search query 1",
    "Professional YouTube search query 2",
    "Professional YouTube search query 3",
    "Professional YouTube search query 4",
    "Professional YouTube search query 5",
    "Professional YouTube search query 6",
    "Professional YouTube search query 7",
    "Professional YouTube search query 8",
    "Professional YouTube search query 9",
    "Professional YouTube search query 10"
  ],
  "plan": "A detailed 7-day learning plan"
}}

Rules:
- Every video query MUST be educational
- NO shorts, no reels, no random words
- Queries must match the learning goal
- Do NOT include anything outside JSON
"""

    response = model.invoke([HumanMessage(content=prompt)])
    raw = response.content

    data = extract_json(raw)

    payload = {
        "title": data["title"],
        "videos": data["videos"]
    }

    yt = requests.post(youtube_url, json=payload)
    yt_data = yt.json()

    return {
        "playlist_title": data["title"],
        "playlist_url": yt_data["playlist_url"],
        "plan": data["plan"]
    }
