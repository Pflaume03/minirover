import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

class Motor:

    def __init__(self, PWMA_pin, AIN2_pin, AIN1_pin, STBY_pin):
        self.PWMA_pin = PWMA_pin
        self.AIN1_pin = AIN1_pin
        self.AIN2_pin = AIN2_pin
        self.STBY_pin = STBY_pin
        
        GPIO.setup(PWMA_pin, GPIO.OUT)
        GPIO.setup(AIN1_pin, GPIO.OUT)
        GPIO.setup(AIN2_pin, GPIO.OUT)
        GPIO.setup(STBY_pin, GPIO.OUT)
        
    def foward(self):
        GPIO.output(self.AIN1_pin, GPIO.HIGH)
        GPIO.output(self.AIN2_pin, GPIO.LOW)

    def backwards(self):
        GPIO.output(self.AIN1_pin, GPIO.LOW)
        GPIO.output(self.AIN2_pin, GPIO.HIGH)

    def set_speed(self):
        GPIO.output(self.PWMA_pin, GPIO.HIGH)
        
    def start(self):
        GPIO.output(self.STBY_pin, GPIO.HIGH)

    def stop(self):
        GPIO.output(self.STBY_pin, GPIO.LOW)

    def GPIO_reset(self):
        GPIO.output(self.PWMA_pin, GPIO.LOW)
        GPIO.output(self.AIN1_pin, GPIO.LOW)
        GPIO.output(self.AIN2_pin, GPIO.LOW)
        GPIO.output(self.STBY_pin, GPIO.LOW)
