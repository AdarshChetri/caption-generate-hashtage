from flask import Flask, render_template, request
import openai
import os

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/", methods=["GET", "POST"])
def index():
    caption = ""
    if request.method == "POST":
        prompt = request.form["prompt"]
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Generate a creative Instagram caption with hashtags for: {prompt}",
            max_tokens=60
        )
        caption = response.choices[0].text.strip()
    return render_template("index.html", caption=caption)

if __name__ == "__main__":
    app.run(debug=True)


