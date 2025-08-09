from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/bedroom')
def bedroom():
    return render_template("bedroom/index.html")

@app.route('/bedroom-sensors')
def bedroom_sensors():
    sensores = ['Luminosidade', 'Temperatura']
    return render_template("bedroom/sensors.html", sensores=sensores)

@app.route('/bedroom-actuators')
def bedroom_actuators():
    atuadores = ['Ar Condicionado', 'Lâmpada Inteligente']
    return render_template("bedroom/actuators.html", atuadores=atuadores)

@app.route('/bathroom')
def bathroom():
    return render_template("bathroom/index.html")

@app.route('/bathroom-sensors')
def bathroom_sensors():
    sensores = ['Luminosidade', 'Umidade']
    return render_template("bathroom/sensors.html", sensores=sensores)

@app.route('/bathroom-actuators')
def bathroom_actuators():
    atuadores = ['Piso Aquecido', 'Encher Banheira']
    return render_template("bathroom/actuators.html", atuadores=atuadores)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)