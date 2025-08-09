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
    return render_template("bedroom/sensors.html")

@app.route('/bedroom-actuators')
def bedroom_actuators():
    return render_template("bedroom/actuators.html")

@app.route('/bathroom')
def bathroom():
    return render_template("bathroom/index.html")

@app.route('/bathroom-sensors')
def bathroom_sensors():
    return render_template("bathroom/sensors.html")

@app.route('/bathroom-actuators')
def bathroom_actuators():
    return render_template("bathroom/actuators.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)