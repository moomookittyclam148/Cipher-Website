from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/')
def index():
    render_template('index.html')

if __name__ == '__main__':
   app.run(debug=True)
