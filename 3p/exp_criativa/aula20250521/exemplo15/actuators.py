from flask import Blueprint, request, render_template, redirect, url_for

actuator = Blueprint("actuators", __name__ , template_folder="templates")

actuators = {
    'Servo Motor': 1, 
    'Lâmpada': 1, 
    'DHT': 0
}

@actuator.route('/actuators')
def index_actuators():
    global actuators
    return render_template("actuators.html", atuadores=actuators)

@actuator.route('/register_actuator')
def register_actuator():
    return render_template("register_actuator.html")

@actuator.route('/add_actuator', methods=['GET','POST'])
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

@actuator.route('/remove_actuator')
def remove_actuator():
    return render_template("remove_actuator.html", atuadores=actuators)

@actuator.route('/del_actuator', methods=['GET','POST'])
def del_actuator():
    global actuators
    if request.method == 'POST':
        actuator = request.form['actuator']
    else:
        actuator = request.args.get('actuator', None)
    actuators.pop(actuator)
    return render_template("actuators.html", atuadores=actuators)

@actuator.route('/list_actuators')
def list_actuators(): 
    global actuators
    return render_template("actuators.html", atuadores=actuators)