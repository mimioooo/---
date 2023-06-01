let On = false
input.onPinPressed(TouchPin.P1, function on_pin_pressed_p1() {
    
    On = !On
})
basic.forever(function on_forever() {
    led.plotBarGraph(input.lightLevel(), 255)
})
basic.forever(function on_forever2() {
    if (On) {
        music.setTempo(pins.map(Math.abs(input.acceleration(Dimension.Y)), 0, 1023, 60, 120))
        music.playTone(input.lightLevel() * 25, music.beat(BeatFraction.Quarter))
    } else {
        music.rest(music.beat(BeatFraction.Whole))
    }
    
})
