from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    text = ""
    total_vowels = 0
    vowel_counts = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}

    if request.method == "POST":
        text = request.form.get("text", "")
        lower_text = text.lower()

        for char in lower_text:
            if char in vowel_counts:
                vowel_counts[char] += 1
                total_vowels += 1

    return render_template(
        "index.html",
        text=text,
        total_vowels=total_vowels,
        vowel_counts=vowel_counts
    )

if __name__ == "__main__":
    app.run(debug=True)
