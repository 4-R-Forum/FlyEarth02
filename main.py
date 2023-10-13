"""

Signed in with Microsoft/GitHub

Project and Repo named FlyEarth02

"""
cmd = ""
roll = 0
pitch = 0
button = 0
serial.redirect_to_usb()
count = 0
basic.show_icon(IconNames.SMALL_DIAMOND)

def on_forever():
    global count, button, pitch, roll, cmd
    if input.button_is_pressed(Button.AB):
        basic.show_icon(IconNames.SQUARE)
        serial.write_line("-1,0,0,0")
        game.pause()
    count = count + 1
    if input.button_is_pressed(Button.A):
        button = 1
    if input.button_is_pressed(Button.B):
        button = -1
    pitch = input.rotation(Rotation.PITCH)
    roll = input.rotation(Rotation.ROLL)
    cmd = "" + convert_to_text(count) + " , " + convert_to_text(pitch) + " , " + convert_to_text(roll) + ", " + convert_to_text(button)
    serial.write_line(cmd)
    basic.pause(1000)
basic.forever(on_forever)
