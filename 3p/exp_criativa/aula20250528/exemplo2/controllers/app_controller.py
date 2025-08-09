#app_controller.py
from flask import Flask, render_template, request
from models.db import db, instance
from controllers.sensors_controller import sensor_
from controllers.actuators_controller import actuator_
from controllers.reads_controller import read
from controllers.write_controller import write
from controllers.users_controller import user
from models.iot.read import Read
from models.iot.write import Write
import json
from flask_mqtt import Mqtt

def create_app():
    app = Flask(__name__, template_folder="./views/", static_folder="./static/", root_path="./")
    
    app.register_blueprint(sensor_, url_prefix='/')
    app.register_blueprint(actuator_, url_prefix='/')
    app.register_blueprint(read, url_prefix='/')
    app.register_blueprint(write, url_prefix='/')
    app.register_blueprint(user, url_prefix='/')
    
    app.config['TESTING'] = False
    app.config['SECRET_KEY'] = 'generated-secrete-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = instance
    
    app.config['MQTT_BROKER_URL'] = 'mqtt-dashboard.com'
    app.config['MQTT_BROKER_PORT'] = 1883
    app.config['MQTT_USERNAME'] = ''
    app.config['MQTT_PASSWORD'] = ''
    # Set this item when you need to verify username and password
    # Set this item when you need to verify username and password
    app.config['MQTT_KEEPALIVE'] = 5000 # Set KeepAlive time in seconds
    app.config['MQTT_TLS_ENABLED'] = False # If your broker supports TLS, set it True
    
    mqtt_client= Mqtt()
    mqtt_client.init_app(app)
    
    topic_subscribe = "/aula_flask/"
    
    db.init_app(app)
    
    @app.route('/')
    def index():
        return render_template("home.html")
    
    @mqtt_client.on_connect()
    def handle_connect(client, userdata, flags, rc):
        if rc == 0:
            print('Broker Connected successfully')
            mqtt_client.subscribe(topic_subscribe) # subscribe topic
        else:
            print('Bad connection. Code:', rc)
            
    @mqtt_client.on_message()
    def handle_mqtt_message(client, userdata, message):
        if message.topic == topic_subscribe:
            js = json.loads(message.payload.decode())
            try:
                with app.app_context():
                    if "sensor" in js:
                        Read.save_read(js["sensor"], js["valor"])
                    elif "actuator" in js:
                        Write.save_write(js["actuator"], js["valor"])
            except Exception as e:
                pass
        
    return app