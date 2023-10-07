let cmdString = ""
let roll = 0
let pitch = 0
let updown = 0
serial.redirectToUSB()
basic.forever(function () {
    if (serial.readLine() == "req") {
        if (input.buttonIsPressed(Button.A)) {
            updown = 1
        } else {
            if (input.buttonIsPressed(Button.B)) {
                updown = -1
            }
        }
        pitch = input.rotation(Rotation.Pitch)
        roll = input.rotation(Rotation.Roll)
        cmdString = "" + convertToText(updown) + "," + convertToText(pitch) + "," + convertToText(roll)
        serial.writeLine(cmdString)
    }
})
