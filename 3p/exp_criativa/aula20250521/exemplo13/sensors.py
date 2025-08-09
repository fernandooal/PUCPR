from flask import Blueprint, request, render_template, redirect, url_for

sensor = Blueprint("sensors", __name__ , template_folder="templates")

sensors = {
    'Umidade': 22,
    'Temperatura': 23,
    'Luminosidade': 1034
}

@sensor.route('/sensors')
def index_sensors():
    global sensors
    return render_template("sensors.html", sensores=sensors)

@sensor.route('/register_sensor')
def register_sensor():
    return render_template("register_sensor.html")

@sensor.route('/add_sensor', methods=['GET','POST'])
def add_sensors():
    global sensors
    if request.method == 'POST':
        sensor = request.form['sensor_name']
        value = request.form['sensor_value']
    else:
        sensor = request.args.get('sensor_name', None)
        value = request.args.get('sensor_value', None)
    sensors[sensor] = value
    return render_template("sensors.html", sensores=sensors)

@sensor.route('/remove_sensor')
def remove_sensor():
    return render_template("remove_sensor.html", sensores=sensors)

@sensor.route('/del_sensor', methods=['GET','POST'])
def del_sensor():
    global sensors
    if request.method == 'POST':
        sensor = request.form['sensor']
    else:
        sensor = request.args.get('sensor', None)
    sensors.pop(sensor)
    return render_template("sensors.html", sensores=sensors)

@sensor.route('/list_sensors')
def list_sensors(): 
    global sensors
    return render_template("sensors.html", sensores=sensors)