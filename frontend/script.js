document.getElementById("ask-btn").addEventListener("click", async () => {
  const question = document.getElementById("question").value;
  const responseDiv = document.getElementById("response");

  responseDiv.innerHTML = `You asked: ${question} <br> <i>Loading...</i>`;

  try {
    const res = await fetch(`http://127.0.0.1:8000/ask?question=${encodeURIComponent(question)}`);
    const data = await res.json();

    responseDiv.innerHTML = `You asked: ${question}<br><b>${data.answer}</b>`;
  } catch (error) {
    responseDiv.innerHTML = "⚠️ Error connecting to backend!";
  }
});
