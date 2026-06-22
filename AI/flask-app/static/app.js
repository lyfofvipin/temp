let chatHistory = [];

async function checkHealth() {
    const pill = document.getElementById("healthStatus");

    try {
        const res = await fetch("/health");
        const data = await res.json();

        if (data.status === "ok") {
            pill.textContent = "Online";
            pill.className = "status-pill ok";
            return;
        }
    } catch (_) {}

    pill.textContent = "Offline";
    pill.className = "status-pill error";
}

async function loadModels() {
    const select = document.getElementById("modelSelect");
    select.innerHTML = `<option value="">Loading models…</option>`;

    try {
        const res = await fetch("/v1/models");
        const data = await res.json();

        select.innerHTML = "";

        if (!data.models?.length) {
            select.innerHTML = `<option value="">No models found</option>`;
            return;
        }

        data.models.forEach(model => {
            const option = document.createElement("option");
            option.value = model.name;
            option.textContent = model.name;
            select.appendChild(option);
        });
    } catch (error) {
        select.innerHTML = `<option value="">Failed to load models</option>`;
        console.error(error);
    }
}

async function showModelInfo() {
    const model = document.getElementById("modelSelect").value;
    const info = document.getElementById("modelInfo");

    if (!model) {
        info.textContent = "Select a model first.";
        return;
    }

    info.textContent = "Loading model details…";

    try {
        const res = await fetch(`/v1/model/${encodeURIComponent(model)}`);
        const data = await res.json();
        info.textContent = JSON.stringify(data.details, null, 2);
    } catch (error) {
        info.textContent = "Could not load model details.";
        console.error(error);
    }
}

async function generateText() {
    const model = document.getElementById("modelSelect").value;
    const prompt = document.getElementById("prompt").value.trim();
    const result = document.getElementById("generateResult");
    const button = document.querySelector(".card-generate .btn-primary");

    if (!model) {
        result.textContent = "Select a model first.";
        return;
    }

    if (!prompt) {
        result.textContent = "Enter a prompt first.";
        return;
    }

    button.disabled = true;
    result.textContent = "Generating…";

    try {
        const res = await fetch("/v1/text", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ model, prompt }),
        });

        const data = await res.json();
        result.textContent = data.text || data.error || "No response returned.";
    } catch (error) {
        result.textContent = "Generation failed. Check that Ollama is running.";
        console.error(error);
    } finally {
        button.disabled = false;
    }
}

async function sendMessage(event) {
    event.preventDefault();

    const model = document.getElementById("modelSelect").value;
    const input = document.getElementById("chatInput");
    const text = input.value.trim();
    const button = document.querySelector(".chat-form .btn-primary");

    if (!model) {
        renderSystemMessage("Select a model before chatting.");
        return;
    }

    if (!text) return;

    chatHistory.push({ role: "user", content: text });
    renderChat();
    input.value = "";
    button.disabled = true;

    try {
        const res = await fetch("/v1/chat", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ model, messages: chatHistory }),
        });

        const data = await res.json();

        if (data.reply) {
            chatHistory.push(data.reply);
        } else {
            renderSystemMessage(data.error || "Chat request failed.");
        }

        renderChat();
    } catch (error) {
        renderSystemMessage("Chat failed. Check that Ollama is running.");
        console.error(error);
    } finally {
        button.disabled = false;
        input.focus();
    }
}

function clearChat() {
    chatHistory = [];
    renderChat();
}

function renderSystemMessage(text) {
    const box = document.getElementById("chatBox");
    box.innerHTML = "";

    const div = document.createElement("div");
    div.className = "message system";
    div.textContent = text;
    box.appendChild(div);
}

function renderChat() {
    const box = document.getElementById("chatBox");
    box.innerHTML = "";

    if (!chatHistory.length) {
        box.innerHTML = `<p class="chat-empty">Send a message to start the conversation.</p>`;
        return;
    }

    chatHistory.forEach(msg => {
        const div = document.createElement("div");
        div.className = `message ${msg.role}`;

        const role = document.createElement("span");
        role.className = "message-role";
        role.textContent = msg.role;

        const content = document.createElement("div");
        content.textContent = msg.content;

        div.appendChild(role);
        div.appendChild(content);
        box.appendChild(div);
    });

    box.scrollTop = box.scrollHeight;
}

window.onload = () => {
    checkHealth();
    loadModels();
};
