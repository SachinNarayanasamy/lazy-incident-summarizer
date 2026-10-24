import streamlit as st
import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "gemma3:1b"

st.set_page_config(page_title="Lazy Incident Summarizer", page_icon="🦥")

st.title("🦥 Lazy Incident Summarizer")
st.caption("Turn a long IT incident description into a quick action summary using a local open-weight AI model.")

incident = st.text_area(
    "Paste an incident / ticket description",
    height=220,
    placeholder="Example: Users in the Chennai office are unable to access the internal VPN..."
)

if st.button("Summarize Incident", type="primary"):
    if not incident.strip():
        st.warning("Please paste an incident description first.")
        st.stop()

    prompt = f"""You are an IT support assistant.
Analyze the incident below and return ONLY these four sections:

Summary:
Priority:
Key Issue:
Suggested Next Action:

Keep each section concise. Do not invent facts that are not in the incident.

Incident:
{incident}
"""

    try:
        response = requests.post(
            OLLAMA_URL,
            json={"model": MODEL, "prompt": prompt, "stream": False},
            timeout=120,
        )
        response.raise_for_status()
        result = response.json()["response"]

        st.subheader("AI Result")
        st.markdown(result)

        st.success("Processed locally with an open-weight model. Your incident text is sent to your local Ollama instance, not a hosted AI API.")

    except requests.exceptions.ConnectionError:
        st.error("Ollama is not running. Start Ollama, make sure `gemma3:1b` is installed, then try again.")
    except Exception as e:
        st.error(f"Something went wrong: {e}")
