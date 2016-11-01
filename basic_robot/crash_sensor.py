from irproximity_sensor import IRProximitySensor
from motors import Motors
from ultrasonic import Ultrasonic


class Crash_sensor():

    def __init__(self):

        self.pri_value = 0

        self.IR_command = ""

    """
    def calculate(self):

        u_sensor = Ultrasonic()

        motors = Motors()

        while True:

            u_sensor.update()
            distance = u_sensor.get_value()
            if distance < 20:
                motors.stop()
                break
            motors.forward(.2, 3)"""

    def calculateFront(self):

        u_sensor = Ultrasonic()
        u_sensor.update()
        distance = u_sensor.get_value()
        if distance < 15:
            self.pri_value = 10000

        else:
            self.pri_value = 0

        return self.pri_value


    def calculateSides(self):

        ir_proxy_sensor = IRProximitySensor()
        ir_proxy_sensor.update()

        values = ir_proxy_sensor.get_value()

        if values[0] == values[1] == False or values[0] == values[1] == True:

            self.IR_command = "FORWARD"
        elif values[1] == True and values[0] == False:
            self.IR_command = "RIGHT"

        elif values[0] == True and values[1] == False:
            self.IR_command = "LEFT"

        return self.IR_command














    #Ultraviolet og 