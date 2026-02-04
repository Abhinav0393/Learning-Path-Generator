import streamlit as st
from utils import generate_learning_path

st.set_page_config(page_title="AI Learning Path Generator", page_icon="📚", layout="wide")

st.title("🎓 AI Learning Path Generator")

# Sidebar
st.sidebar.header("Configuration")

google_api_key = st.sidebar.text_input("Google Gemini API Key", type="password")
youtube_url = st.sidebar.text_input("Pipedream YouTube Webhook URL")

st.sidebar.markdown("""
Paste your **Pipedream YouTube workflow webhook URL** here.
This will automatically create playlists and add videos.
""")

# Main
st.header("Enter Your Learning Goal")

goal = st.text_input(
    "What do you want to learn?",
    placeholder="Example: I want to learn DBMS in 7 days"
)

if st.button("🚀 Generate Learning Path"):
    if not google_api_key:
        st.error("Please enter your Gemini API key")
    elif not youtube_url:
        st.error("Please enter your Pipedream URL")
    elif not goal:
        st.error("Please enter a learning goal")
    else:
        with st.spinner("Creating your learning path and YouTube playlist..."):
            try:
                result = generate_learning_path(
                    api_key=google_api_key,
                    youtube_url=youtube_url,
                    goal=goal
                )

                st.success("🎉 Learning Path & Playlist Created!")

                st.subheader("🎧 Your YouTube Playlist")
                st.markdown(f"[Click here to open your playlist]({result['playlist_url']})")

                st.subheader("📘 Study Plan")
                st.markdown(result["plan"])

            except Exception as e:
                st.error("Something went wrong")
                st.code(str(e))
