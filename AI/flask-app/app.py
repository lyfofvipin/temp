from flask import Flask, request, jsonify, render_template
import requests

from config import OLLAMA_URL

app = Flask(__name__)

# ----------------------------
# Helper
# ----------------------------

def ollama_post(endpoint, payload):
    try:
        response = requests.post(
            f"{OLLAMA_URL}{endpoint}",
            json=payload,
            timeout=300
        )

        response.raise_for_status()
        return response.json(), response.status_code

    except requests.exceptions.RequestException as e:
        return {"error": str(e)}, 500


# =====================================================
# CUSTOM API -> LIST MODELS
# Maps to Ollama: GET /api/tags
# =====================================================

@app.route("/v1/models", methods=["GET"])
def list_models():
    try:
        response = requests.get(
            f"{OLLAMA_URL}/api/tags",
            timeout=30
        )

        response.raise_for_status()

        data = response.json()

        return jsonify({
            "success": True,
            "models": [
                {
                    "name": m["name"],
                    "size": m.get("size"),
                    "modified": m.get("modified_at")
                }
                for m in data.get("models", [])
            ]
    })

    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


# =====================================================
# CUSTOM API -> GENERATE TEXT
# Maps to Ollama: POST /api/generate
# =====================================================

@app.route("/v1/text", methods=["POST"])
def generate_text():

    body = request.json

    model = body.get("model", "llama3")
    prompt = body.get("prompt")

    if not prompt:
        return jsonify({
            "success": False,
            "error": "prompt required"
        }), 400

    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }

    result, status = ollama_post("/api/generate", payload)

    return jsonify({
        "success": True,
        "model": model,
        "text": result.get("response", "")
    }), status


# =====================================================
# CUSTOM API -> CHAT
# Maps to Ollama: POST /api/chat
# =====================================================

@app.route("/v1/chat", methods=["POST"])
def chat():

    body = request.json

    model = body.get("model", "llama3")
    messages = body.get("messages", [])

    payload = {
        "model": model,
        "messages": messages,
        "stream": False
    }

    result, status = ollama_post("/api/chat", payload)

    return jsonify({
        "success": True,
        "reply": result.get("message", {})
    }), status


# =====================================================
# CUSTOM API -> MODEL INFO
# Maps to Ollama: POST /api/show
# =====================================================

@app.route("/v1/model/<model_name>", methods=["GET"])
def model_info(model_name):

    payload = {
        "model": model_name
    }

    result, status = ollama_post("/api/show", payload)

    return jsonify({
        "success": True,
        "details": result
    }), status


# =====================================================
# OPENAI API (commented — same pattern as Ollama, via requests)
# Uncomment config values in config.py, then uncomment this block.
# See also: ../08_chatgpt_api_uses.py
# =====================================================

# def openai_post(endpoint, payload):
#     from config import OPENAI_API_URL, OPENAI_API_KEY
#
#     try:
#         response = requests.post(
#             f"{OPENAI_API_URL}{endpoint}",
#             headers={
#                 "Authorization": f"Bearer {OPENAI_API_KEY}",
#                 "Content-Type": "application/json",
#             },
#             json=payload,
#             timeout=120,
#         )
#         response.raise_for_status()
#         return response.json(), response.status_code
#
#     except requests.exceptions.RequestException as e:
#         return {"error": str(e)}, 500
#
#
# @app.route("/v1/openai/chat", methods=["POST"])
# def openai_chat():
#     from config import OPENAI_MODEL
#
#     body = request.json or {}
#     messages = body.get("messages", [])
#     model = body.get("model", OPENAI_MODEL)
#
#     if not messages:
#         return jsonify({"success": False, "error": "messages required"}), 400
#
#     payload = {"model": model, "messages": messages}
#     result, status = openai_post("/chat/completions", payload)
#
#     if status != 200:
#         return jsonify({"success": False, "error": result.get("error")}), status
#
#     return jsonify({
#         "success": True,
#         "reply": result["choices"][0]["message"],
#     })


# =====================================================
# HEALTH CHECK
# =====================================================

@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "ok",
        "service": "ollama-gateway"
    })


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8000,
        debug=True
    )
