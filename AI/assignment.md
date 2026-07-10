
# 🚀 GenAI Project Assignment: AI-Powered Code Grading Portal

## Objective

Your task is to build a lightweight web application (using either **Flask** or **Streamlit**) that acts as an automated Python testing portal for schools. The app will fetch coding challenges, accept code submissions from students, and route that code to a locally running **Ollama LLM** instance to dynamically evaluate whether the solution is logically correct.

---

## 🏗️ System Architecture & Data Flow

To successfully complete this project, your application must manage the following end-to-end workflow:

```text
[Student UI] ──(Submits Code)──> [Web Backend] ──(Injects Prompt)──> [Local Ollama API]
     ▲                                                                        │
     └──────────(Returns Verdict & Feedback)◄─────────────────────────────────┘

```

* **The Frontend (UI):** Displays a curated list of Python coding problems (extracted from the provided data source). It provides a text area for the student to write their Python code.
* **The Prompt Engine (Backend):** Once the student clicks "Submit", the backend captures their raw code and wraps it inside a strictly engineered system prompt.
* **The AI Evaluator (Ollama):** The backend sends a `POST` request to Ollama's local endpoint (`http://localhost:11434/api/generate`). The local LLM acts as the TA (Teaching Assistant), reviewing the code logic.
* **The Verdict:** The backend parses Ollama's response and presents the final evaluation (Pass/Fail) and qualitative feedback back to the student on the UI.

---

## 🎯 Core Technical Milestones (Student Checklist)

To get full credit for this assignment, your implementation must address these four pillars:

### 1. UI and State Management

* Create a clean sidebar or dropdown menu to switch between different programming challenges.
* Dynamically update the problem description, sample inputs, and expected outputs based on the active selection.

### 2. Local LLM Orchestration

* Ensure Ollama is running locally with an appropriate model suited for code/logic understanding (e.g., `llama3`, `codellama`, or `mistral`).
* Connect your web framework to Ollama using standard Python HTTP networking libraries (`requests`) or the official `ollama` Python library.

### 3. Advanced Prompt Engineering

* **Crucial constraint:** LLMs can be wordy. You must engineer your prompt so that the local model responds in a strict, predictable format.
* **Example Required Format:**
> **STATUS:** `[CORRECT / INCORRECT]`
> **FEEDBACK:** `[A short 2-sentence explanation of their logic or bugs]`



### 4. Response Parsing & UI Styling

* Your backend must read the AI's response, programmatically check if it contains the "CORRECT" or "INCORRECT" status flag, and render appropriate UI feedback elements (e.g., green success alerts for correct answers, red warning alerts for bugs).

---

## 💡 Bonus Challenges for Extra Credit

* **The Sandbox Guard:** Before sending the code to Ollama, run it through a basic local check (like standard error handling or Python's `compile()` function) to immediately alert the student if they have a glaring syntax error.
* **Structured JSON Output:** Force Ollama to return a pure JSON object instead of raw text, and use Python's `json` library to parse it cleanly.