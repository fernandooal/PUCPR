
from flask import Flask, render_template

app= Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/sensors')
def sensors():
    sensores = {'Umidade':22, 'Temperatura':23, 'Luminosidade':1034}
    return render_template("sensors.html", sensores=sensores)

@app.route('/actuators')
def actuators():
    #exercicio7
    atuadores = {'Servo Motor':122, 'Lâmpada':1}
    return render_template("actuators.html", atuadores=atuadores)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)