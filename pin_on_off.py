# funciones/pin_on_off.py
import RPi.GPIO as GPIO
import threading
import time

class Pin_on_off:
    def __init__(self, pin, timmer=False, time_on=0):
        self.pin = pin
        self.timmer = timmer
        self.time_on = time_on
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)
        self.estado = False

    def encender(self):
        GPIO.output(self.pin, GPIO.HIGH)
        self.estado = True
        if self.timmer and self.time_on > 0:
            threading.Thread(target=self._temporizador_apagar).start()

    def apagar(self):
        GPIO.output(self.pin, GPIO.LOW)
        self.estado = False

    def _temporizador_apagar(self):
        time.sleep(self.time_on)
        self.apagar()
