async function askQuestion() {
    const question = document.getElementById("question").value;
    const responseDiv = document.getElementById("answer");
    responseDiv.innerHTML = "🤖 Thinking...";

    try {
        const response = await fetch("http://127.0.0.1:8000/ask", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ query: question })
        });
        const data = await response.json();
        responseDiv.innerHTML = `Q: ${data.question}<br>A: ${data.answer}`;
    } catch (error) {
        responseDiv.innerHTML = "❌ Oops, couldn’t reach the server!";
    }
}
