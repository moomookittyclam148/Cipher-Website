from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encodings')
def encodings():
    return render_template('encodings.html')

@app.route('/ciphers')
def ciphers():
    return render_template('ciphers.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/encodings/<encoding>')
def specific_encoding(encoding):
    encoding_hash = {}
    encoding_hash['base64'] = 'base64'
    return render_template('converter.html', encoding_name=encoding_hash[encoding])

if __name__ == '__main__':
   app.run(debug=True)
