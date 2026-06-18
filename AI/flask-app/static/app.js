let chatHistory = [];

async function loadModels() {

    const res = await fetch("/v1/models");
    const data = await res.json();

    const select = document.getElementById("modelSelect");

    select.innerHTML = "";

    data.models.forEach(model => {

        const option = document.createElement("option");

        option.value = model.name;
        option.textContent = model.name;

        select.appendChild(option);
    });
}

async function showModelInfo() {

    const model =
        document.getElementById("modelSelect").value;

    const res =
        await fetch(`/v1/model/${model}`);

    const data = await res.json();

    document.getElementById("modelInfo")
        .textContent =
        JSON.stringify(data.details, null, 2);
}

async function generateText() {

    const model =
        document.getElementById("modelSelect").value;

    const prompt =
        document.getElementById("prompt").value;

    const res = await fetch("/v1/text", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            model,
            prompt
        })
    });

    const data = await res.json();

    document.getElementById("generateResult")
        .innerText = data.text;
}

async function sendMessage() {

    const model =
        document.getElementById("modelSelect").value;

    const input =
        document.getElementById("chatInput");

    const text = input.value;

    if (!text) return;

    chatHistory.push({
        role: "user",
        content: text
    });

    renderChat();

    input.value = "";

    const res = await fetch("/v1/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            model,
            messages: chatHistory
        })
    });

    const data = await res.json();

    chatHistory.push(data.reply);

    renderChat();
}

function renderChat() {

    const box =
        document.getElementById("chatBox");

    box.innerHTML = "";

    chatHistory.forEach(msg => {

        const div =
            document.createElement("div");

        div.className = msg.role;

        div.innerHTML =
            `<b>${msg.role}:</b> ${msg.content}`;

        box.appendChild(div);
    });

    box.scrollTop = box.scrollHeight;
}

window.onload = loadModels;