def on_gesture_tilt_right():
    calliBot2.motor(C2Motor.RECHTS, C2Dir.RÜCKWÄRTS, 10)
    calliBot2.motor(C2Motor.LINKS, C2Dir.VORWÄRTS, 100)
    calliBot2.set_rgb_led(C2RgbLed.RH, 16, 0, 0)
    calliBot2.set_rgb_led(C2RgbLed.RV, 16, 0, 0)
input.on_gesture(Gesture.TILT_RIGHT, on_gesture_tilt_right)

def on_pin_touch_p1():
    MotionKit.neutral()
input.on_pin_touch_event(TouchPin.P1, input.button_event_down(), on_pin_touch_p1)

def on_button_a():
    MotionKit.turn_left(90)
input.on_button_event(Button.A, input.button_event_click(), on_button_a)

def on_gesture_tilt_left():
    calliBot2.motor(C2Motor.RECHTS, C2Dir.VORWÄRTS, 100)
    calliBot2.motor(C2Motor.LINKS, C2Dir.RÜCKWÄRTS, 10)
    calliBot2.set_rgb_led(C2RgbLed.LH, 16, 0, 0)
    calliBot2.set_rgb_led(C2RgbLed.LV, 16, 0, 0)
input.on_gesture(Gesture.TILT_LEFT, on_gesture_tilt_left)

def on_button_ab():
    motors.motor_command(MotorCommand.SLEEP)
input.on_button_event(Button.AB, input.button_event_click(), on_button_ab)

def on_button_b():
    MotionKit.turn_right(90)
input.on_button_event(Button.B, input.button_event_click(), on_button_b)

def on_pin_touch_p0():
    MotionKit.turn_left(180)
input.on_pin_touch_event(TouchPin.P0, input.button_event_down(), on_pin_touch_p0)

def on_pin_touch_p2():
    MotionKit.backward()
    calliBot2.set_rgb_led(C2RgbLed.LH, 16, 0, 0)
    calliBot2.set_rgb_led(C2RgbLed.RH, 16, 0, 0)
input.on_pin_touch_event(TouchPin.P2, input.button_event_down(), on_pin_touch_p2)

def on_pin_touch_p3():
    MotionKit.stop()
input.on_pin_touch_event(TouchPin.P3, input.button_event_down(), on_pin_touch_p3)

calliBot2.warte(C2SensorWait.DISTANCE_CM, C2Check.LESS_THAN, 7)
motors.motor_power(100)

def on_forever():
    basic.show_string("McLarry")
    calliBot2.set_rgb_led(C2RgbLed.ALL, 16, 16, 16)
    calliBot2.set_led(C2Motor.BEIDE, C2State.AN)
    calliBot2.motor(C2Motor.BEIDE, C2Dir.VORWÄRTS, 100)
    calliBot2.warte(C2SensorWait.DISTANCE_CM, C2Check.EQUAL, 1.5)
    music.play_tone(698, music.beat(BeatFraction.DOUBLE))
    MotionKit.drive_backwards(100)
    MotionKit.turn_left(90)
basic.forever(on_forever)
