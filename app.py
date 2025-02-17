from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Store notes in a list
notes = []

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        note = request.form.get("note")
        if note:  # Ensure the note is not empty
            notes.append(note)
        return redirect(url_for('index'))  # Redirect to avoid form resubmission
    return render_template("home.html", notes=notes)

if __name__ == '__main__':
    app.run(debug=True)
