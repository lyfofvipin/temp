import requests
import streamlit as st

OLLAMA_URL = "http://localhost:11434"
DEFAULT_MODEL = "llama3.2"


def fetch_models() -> list[str]:
    try:
        response = requests.get(f"{OLLAMA_URL}/api/tags", timeout=10)
        response.raise_for_status()
        models = [m["name"] for m in response.json().get("models", [])]
        return models or [DEFAULT_MODEL]
    except requests.RequestException:
        return [DEFAULT_MODEL]


def ollama_chat(model: str, messages: list[dict]) -> str:
    response = requests.post(
        f"{OLLAMA_URL}/api/chat",
        json={"model": model, "messages": messages, "stream": False},
        timeout=120,
    )
    response.raise_for_status()
    return response.json()["message"]["content"]

st.set_page_config(page_title="AI Gateway — Streamlit", page_icon="🤖", layout="wide")

st.title("AI Gateway — Streamlit")
st.caption("Same Ollama backend as flask-app — UI written in pure Python.")

if "messages" not in st.session_state:
    st.session_state.messages = []

with st.sidebar:
    st.header("Settings")
    models = fetch_models()
    model = st.selectbox("Model", models, index=0)
    if st.button("Clear chat"):
        st.session_state.messages = []
        st.rerun()
    st.markdown("---")
    st.markdown("**Ollama:** `" + OLLAMA_URL + "`")
    st.markdown("Compare with `flask-app/`")

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Ask something…"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking…"):
            with st.spinner("Thinking again…"):
                try:
                    reply = ollama_chat(model, st.session_state.messages)
                    st.markdown(reply)
                    st.session_state.messages.append({"role": "assistant", "content": reply})
                except requests.RequestException as exc:
                    st.error(f"Ollama error: {exc}. Is `ollama serve` running?")
