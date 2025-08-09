from flask import Flask, render_template, request
from login import login
from sensors import sensor
from actuators import actuator

app= Flask(__name__)

app.register_blueprint(login, url_prefix='/')
app.register_blueprint(sensor, url_prefix='/')
app.register_blueprint(actuator, url_prefix='/')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)