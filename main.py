from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)

@app.route('/')
def form():
    return render_template('bajo_peso.html')

@app.route('/peso_normal')
def form2():
    return render_template('peso_normal.html')

@app.route('/sobre_peso')
def form3():
    return render_template('sobre_peso.html')

@app.route('/obesidad')
def form4():
    return render_template('obesidad.html')

@app.route('/consejos')
def form5():
    return render_template('consejos.html')

@app.route('/imc')
def form6():
    return render_template('imc.html')

@app.route('/preguntas')
def form7():
    return render_template('preguntas.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

