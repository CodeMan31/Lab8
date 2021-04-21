from guizero import App, Slider, TextBox
from gpiozero import AngularServo
servo1 = AngularServo(12, min_pulse_width = 0.001, max_pulse_width = 0.002, initial_angle = 0, min_angle=-90, max_angle = 90)
servo2 = AngularServo(13, min_pulse_width = 0.001, max_pulse_width = 0.002, initial_angle = 0, min_angle=-90, max_angle = 90)


def sliderPos1(sliderVal):
    tb.value = sliderVal
    servo1.angle = int(sliderVal)


def sliderPos2(sliderVal):
    tb.value = sliderVal
    servo2.angle = int(sliderVal)


app = App(title = "Servo Control", height = 300, width = 600)
slider1 = Slider(app, width = 600, start = -90, end = 90, command = sliderPos1)
slider2 = Slider(app, width = 600, start = -90, end = 90, command = sliderPos2)
tb = TextBox(app)
tb.hide()

app.display()