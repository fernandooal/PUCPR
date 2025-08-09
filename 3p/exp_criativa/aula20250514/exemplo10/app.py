from flask import Flask, render_template, request

app= Flask(__name__)

users = {
'user1': '1234',
'user2': '1234'
}

sensors = {
    'Umidade': 22,
    'Temperatura': 23,
    'Luminosidade': 1034
}

actuators = {
    'Servo Motor': 1, 
    'Lâmpada': 1, 
    'DHT': 0
}

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/register_user')
def register_user():
    return render_template("register_user.html")

@app.route('/add_user', methods=['GET','POST'])
def add_users():
    global users
    if request.method == 'POST':
        user = request.form['user']
        password = request.form['password']
    else:
        user = request.args.get('user', None)
        password = request.args.get('password', None)
    users[user] = password
    return render_template("users.html", users=users)

@app.route('/remove_user')
def remove_user():
    return render_template("remove_user.html", users=users)

@app.route('/del_user', methods=['GET','POST'])
def del_user():
    global users
    if request.method == 'POST':
        user = request.form['user']
    else:
        user = request.args.get('user', None)
    users.pop(user)
    return render_template("users.html", users=users)

@app.route('/list_users')
def list_users():
    global users
    return render_template("users.html", users=users)

@app.route('/sensors')
def index_sensors():
    global sensors
    return render_template("sensors.html", sensores=sensors)

@app.route('/register_sensor')
def register_sensor():
    return render_template("register_sensor.html")

@app.route('/add_sensor', methods=['GET','POST'])
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

@app.route('/remove_sensor')
def remove_sensor():
    return render_template("remove_sensor.html", sensores=sensors)

@app.route('/del_sensor', methods=['GET','POST'])
def del_sensor():
    global sensors
    if request.method == 'POST':
        sensor = request.form['sensor']
    else:
        sensor = request.args.get('sensor', None)
    sensors.pop(sensor)
    return render_template("sensors.html", sensores=sensors)

@app.route('/list_sensors')
def list_sensors(): 
    global sensors
    return render_template("sensors.html", sensores=sensors)

@app.route('/actuators')
def index_actuators():
    global actuators
    return render_template("actuators.html", atuadores=actuators)

@app.route('/register_actuator')
def register_actuator():
    return render_template("register_actuator.html")

@app.route('/add_actuator', methods=['GET','POST'])
def add_actuator():
    global actuators
    if request.method == 'POST':
        actuator = request.form['actuator_name']
        value = request.form['actuator_value']
    else:
        actuator = request.args.get('actuator_name', None)
        value = request.args.get('actuator_value', None)
    actuators[actuator] = value
    return render_template("actuators.html", atuadores=actuators)

@app.route('/remove_actuator')
def remove_actuator():
    return render_template("remove_actuator.html", atuadores=actuators)

@app.route('/del_actuator', methods=['GET','POST'])
def del_actuator():
    global actuators
    if request.method == 'POST':
        actuator = request.form['actuator']
    else:
        actuator = request.args.get('actuator', None)
    actuators.pop(actuator)
    return render_template("actuators.html", atuadores=actuators)

@app.route('/list_actuators')
def list_actuators(): 
    global actuators
    return render_template("actuators.html", atuadores=actuators)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)