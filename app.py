# app.py
from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

def generate_password(length=12, use_special_chars=True):
    characters = string.ascii_letters + string.digits
    if use_special_chars:
        characters += string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

@app.route('/', methods=['GET', 'POST'])
def index():
    password = ''
    if request.method == 'POST':
        length = int(request.form.get('length', 12))
        use_special_chars = 'special' in request.form
        password = generate_password(length, use_special_chars)
    return render_template('index.html', password=password)

if __name__ == '__main__':
    app.run(debug=True)