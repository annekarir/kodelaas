input.onButtonPressed(Button.A, function () {
    Temp = "" + Brukerforslag + "A"
    basic.showString("A")
    basic.clearScreen()
    sjekke_bokstav()
})
input.onButtonPressed(Button.B, function () {
    Temp = "" + Brukerforslag + "B"
    basic.showString("B")
    basic.clearScreen()
    sjekke_bokstav()
})
function sjekke_bokstav () {
    Brukerforslag = Temp
    serial.writeLine(Brukerforslag)
    if (Brukerforslag == kode) {
        for (let index = 0; index < 3; index++) {
            basic.showNumber(hemmelighet_låskoden)
        }
    } else if (Brukerforslag.length > kode.length) {
        basic.showIcon(IconNames.No)
        basic.pause(2000)
        basic.clearScreen()
        Brukerforslag = ""
    }
}
let Temp = ""
let Brukerforslag = ""
let kode = ""
let hemmelighet_låskoden = 0
hemmelighet_låskoden = 3791
kode = "ABAA"
Brukerforslag = ""
basic.forever(function () {
    if (Brukerforslag.length == 0) {
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . #
            `)
        basic.clearScreen()
        basic.pause(500)
    }
})
