from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import json
import os

app = Flask(__name__, template_folder='templates')

NOTES_FILE = "notes.json"

def load_notes():
    if not os.path.exists(NOTES_FILE):
        return []
    with open(NOTES_FILE, 'r') as f:
        return json.load(f)

def save_notes(notes):
    with open(NOTES_FILE, 'w') as f:
        json.dump(notes, f, indent=2)

@app.route('/')
def index():
    notes = load_notes()
    return render_template('index.html', notes=notes)

@app.route('/add_note', methods=['POST'])
def add_note():
    title = request.form.get('title')
    content = request.form.get('content')
    if title:
        notes = load_notes()
        notes.append({'title': title, 'content': content})
        save_notes(notes)
    return redirect(url_for('index'))

@app.route('/delete_note/<int:index>')
def delete_note(index):
    notes = load_notes()
    if 0 <= index < len(notes):
        notes.pop(index)
        save_notes(notes)
    return redirect(url_for('index'))

# Add route to serve CSS file
@app.route('/style.css')
def serve_css():
    return send_from_directory('templates', 'style.css', mimetype='text/css')

if __name__ == '__main__':
    app.run(debug=True)