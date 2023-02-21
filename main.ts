input.onButtonPressed(Button.A, function () {
    Counter_A += 1
    led.stopAnimation()
})
let Counter_A = 0
let Counter_B = 0
basic.forever(function () {
    basic.showString("" + Counter_A + ":" + Counter_B)
})
