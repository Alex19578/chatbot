from flask import Flask, render_template, request
import openai

app = Flask(__name__)

openai.api_key = "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"

model_engine = "text-davinci-002"

def generate_response(prompt):
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    answer = response.choices[0].text.strip()
    return answer

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    user_text = request.args.get("msg")
    bot_response = generate_response(user_text)
    return bot_response

if __name__ == "__main__":
    app.run(debug=True)
