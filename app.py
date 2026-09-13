from flask import Flask, request
import requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        question = request.form["question"]

        response = requests.post(
            "http://127.0.0.1:11434/api/generate",
            json={
                "model": "llama3.2",
                "prompt": question,
                "stream": False
            }
        )

        answer = response.json()["response"]

        return f"<h2>AI Answer:</h2><p>{answer}</p>"

    return """
    <h1>Student Problem Solver</h1>

    <form method="POST">
        <input type="text" name="question" placeholder="Enter your question">
        <button type="submit">Ask</button>
    </form>
    """

if __name__ == "__main__":
    app.run(debug=True)