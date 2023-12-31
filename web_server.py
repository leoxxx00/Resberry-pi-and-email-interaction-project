from flask import Flask
import RPi.GPIO as GPIO

BUTTON_PIN = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN,GPIO.IN)

app=Flask(__name__)

@app.route("/")#create some routes

def index():
    return "Hello form Flask"

@app.route("/push-button")
def check_push_button_state():
    if GPIO.input(BUTTON_PIN)==GPIO.HIGH:
        return "Button is pressed"
    else:
        return "Button is not pressed" 
app.run(host="0.0.0.0")


