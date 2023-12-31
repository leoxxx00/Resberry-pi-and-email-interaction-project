import RPi.GPIO as GPIO
import time


PIR_PIN=4
LED_PIN=17

#setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN,GPIO.IN)
GPIO.setup(LED_PIN,GPIO.OUT)
GPIO.output(LED_PIN,GPIO.LOW)
print("GPIOs setup.")

MOVE_DETECT_TRESHOLD = 3.0
last_pir_state = GPIO.input(PIR_PIN)
movement_timer=time.time()
MIN_DURATION_BETWEEN_2_PHOTOS = 5.0
last_time_photo_taken = 0

try:
    while True:
        time.sleep(0.01)
        pir_state=GPIO.input(PIR_PIN)
        if pir_state == GPIO.HIGH:
            GPIO.output(LED_PIN , GPIO.HIGH)
        else:
            GPIO.output(LED_PIN,GPIO.LOW)
        if last_pir_state == GPIO.LOW and pir_state == GPIO.HIGH:
            movement_timer = time.time()
        if last_pir_state == GPIO.HIGH and pir_state == GPIO.HIGH:
            if time.time() - movement_timer > MOVE_DETECT_TRESHOLD:
                if time.time()-last_time_photo_taken > MIN_DURATION_BETWEEN_2_PHOTOS:
                    print("Take photo and send it email.")
                    last_time_photo_taken=time.time()
        last_pir_state = pir_state

except KeyboardInterrupt:
    GPIO.cleanup()


