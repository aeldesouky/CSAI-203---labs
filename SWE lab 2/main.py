from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    
    return render_template("index.html", name="")  # Provide a default empty name

@app.route('/text', methods=['POST'])
def get_input():
    name = request.form['input']
    if not isinstance(name, str) or not name.strip():  # Check for empty string
        name = "invalid"
    return render_template('index.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)
