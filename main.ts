/** 

Signed in with Microsoft/GitHub

Project and Repo named FlyEarth02


 */
let cmd = ""
let roll = 0
let pitch = 0
let button = 0
serial.redirectToUSB()
let count = 0
basic.showIcon(IconNames.SmallDiamond)
basic.forever(function on_forever() {
    
    if (input.buttonIsPressed(Button.AB)) {
        basic.showIcon(IconNames.Square)
        serial.writeLine("-1,0,0,0")
        game.pause()
    }
    
    count = count + 1
    if (input.buttonIsPressed(Button.A)) {
        button = 1
    }
    
    if (input.buttonIsPressed(Button.B)) {
        button = -1
    }
    
    pitch = input.rotation(Rotation.Pitch)
    roll = input.rotation(Rotation.Roll)
    cmd = "" + convertToText(count) + " , " + convertToText(pitch) + " , " + convertToText(roll) + ", " + convertToText(button)
    serial.writeLine(cmd)
    basic.pause(1000)
})
