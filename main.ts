input.onGesture(Gesture.TiltRight, function () {
    calliBot2.motor(C2Motor.rechts, C2Dir.rückwärts, 10)
    calliBot2.motor(C2Motor.links, C2Dir.vorwärts, 100)
    calliBot2.setRgbLed(C2RgbLed.RH, 16, 0, 0)
    calliBot2.setRgbLed(C2RgbLed.RV, 16, 0, 0)
})
input.onPinTouchEvent(TouchPin.P1, input.buttonEventDown(), function () {
    MotionKit.neutral()
})
input.onButtonEvent(Button.A, input.buttonEventClick(), function () {
    MotionKit.turnLeft(90)
})
input.onGesture(Gesture.TiltLeft, function () {
    calliBot2.motor(C2Motor.rechts, C2Dir.vorwärts, 100)
    calliBot2.motor(C2Motor.links, C2Dir.rückwärts, 10)
    calliBot2.setRgbLed(C2RgbLed.LH, 16, 0, 0)
    calliBot2.setRgbLed(C2RgbLed.LV, 16, 0, 0)
})
input.onButtonEvent(Button.AB, input.buttonEventClick(), function () {
    motors.motorCommand(MotorCommand.Sleep)
})
input.onButtonEvent(Button.B, input.buttonEventClick(), function () {
    MotionKit.turnRight(90)
})
input.onPinTouchEvent(TouchPin.P0, input.buttonEventDown(), function () {
    MotionKit.turnLeft(180)
})
input.onPinTouchEvent(TouchPin.P2, input.buttonEventDown(), function () {
    MotionKit.backward()
    calliBot2.setRgbLed(C2RgbLed.LH, 16, 0, 0)
    calliBot2.setRgbLed(C2RgbLed.RH, 16, 0, 0)
})
input.onPinTouchEvent(TouchPin.P3, input.buttonEventDown(), function () {
    MotionKit.stop()
})
calliBot2.warte(C2SensorWait.distanceCm, C2Check.lessThan, 7)
motors.motorPower(100)
basic.forever(function () {
    basic.showString("McLarry")
    calliBot2.setRgbLed(C2RgbLed.All, 16, 16, 16)
    calliBot2.setLed(C2Motor.beide, C2State.an)
    calliBot2.motor(C2Motor.beide, C2Dir.vorwärts, 100)
    calliBot2.warte(C2SensorWait.distanceCm, C2Check.equal, 1.5)
    music.playTone(698, music.beat(BeatFraction.Double))
    MotionKit.driveBackwards(100)
    MotionKit.turnLeft(90)
})
