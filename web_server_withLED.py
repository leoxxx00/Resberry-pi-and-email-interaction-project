from flask import Flask
import RPi.GPIO as GPIO

BUTTON_PIN = 26
LED_PIN_LIST=[17,27,22]

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN,GPIO.IN)

for pin in LED_PIN_LIST:
    GPIO.setup(pin,GPIO.OUT)

for pin in LED_PIN_LIST:
    GPIO.output(pin,GPIO.LOW)

app=Flask(__name__)

for pin in LED_PIN_LIST:
    GPIO.output(pin,GPIO.LOW)

@app.route("/")#create some routes

def index():
    return "Hello form Flask"

@app.route("/push-button")
def check_push_button_state():
    if GPIO.input(BUTTON_PIN)==GPIO.HIGH:
        return "Button is pressed"
    else:
        return "Button is not pressed"
    
@app.route("/led/<int:led_pin>/state/<int:led_state>")
def trigger_led(led_pin,led_state):
    if not led_pin in LED_PIN_LIST:
        return "Wrong GPIO number: " +str(led_pin)
    if led_state==0:
        GPIO.output(led_pin,GPIO.LOW)
    elif led_state==1:
        GPIO.output(led_pin,GPIO.HIGH)
    else:
        return "State must be zero or one"
    return "OKAY"
app.run(host="0.0.0.0")


