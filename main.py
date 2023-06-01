On = Faluse

def on_pin_pressed_p1():
    global On
    On = not (On)
input.on_pin_pressed(TouchPin.P1, on_pin_pressed_p1)

def on_forever():
    led.plot_bar_graph(input.light_level(), 255)
basic.forever(on_forever)

def on_forever2():
    if On:
        music.set_tempo(pins.map(abs(input.acceleration(Dimension.Y)), 0, 1023, 60, 120))
        music.play_tone(input.light_level() * 25, music.beat(BeatFraction.QUARTER))
    else:
        music.rest(music.beat(BeatFraction.WHOLE))
basic.forever(on_forever2)
