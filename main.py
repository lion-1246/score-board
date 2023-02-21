def on_button_pressed_a():
    global Counter_B
    Counter_B += 1
    led.stop_animation()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global Counter_B
    Counter_B = 1
    led.stop_animation()
input.on_button_pressed(Button.B, on_button_pressed_b)

Counter_B = 0
Counter_A = 0
Counter_B = 0

def on_forever():
    basic.show_string("" + str(Counter_A) + ":" + str(Counter_B))
basic.forever(on_forever)
