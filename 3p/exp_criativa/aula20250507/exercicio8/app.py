from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    info = {'Quarto': "/bedroom", 'Banheiro':"bathroom"}
    return render_template("index.html", info=info)

@app.route('/bedroom')
def bedroom():
    info = {'Sensores':'bedroom-sensors', 'Atuadores':'bedroom-actuators'}
    return render_template("bedroom/index.html", info=info)

@app.route('/bedroom-sensors')
def bedroom_sensors():
    sensores = {'Luminosidade':20, 'Temperatura':15}
    return render_template("bedroom/sensors.html", sensores=sensores)

@app.route('/bedroom-actuators')
def bedroom_actuators():
    atuadores = {'Ar Condicionado':1, 'Lâmpada Inteligente':0}
    return render_template("bedroom/actuators.html", atuadores=atuadores)

@app.route('/bathroom')
def bathroom():
    info = {'Sensores':'bathroom-sensors', 'Atuadores':'bathroom-actuators'}
    return render_template("bathroom/index.html", info=info)

@app.route('/bathroom-sensors')
def bathroom_sensors():
    sensores = {'Luminosidade':30, 'Umidade':40}
    return render_template("bathroom/sensors.html", sensores=sensores)

@app.route('/bathroom-actuators')
def bathroom_actuators():
    atuadores = {'Piso Aquecido':0, 'Encher Banheira':1}
    return render_template("bathroom/actuators.html", atuadores=atuadores)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)