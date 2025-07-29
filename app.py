
from flask import Flask, render_template, request
import openai
import os

app = Flask(__name__)

# Load API key
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/", methods=["GET", "POST"])
def home():
    caption = None
    if request.method == "POST":
        prompt = request.form.get("prompt")
        if prompt:
            try:
                response = openai.Completion.create(
                    engine="text-davinci-003",
                    prompt=f"Generate an Instagram caption with hashtags for: {prompt}",
                    max_tokens=100
                )
                caption = response.choices[0].text.strip()
            except Exception as e:
                caption = f"Error: {str(e)}"
    return render_template("index.html", caption=caption)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
