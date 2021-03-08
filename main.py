def on_button_pressed_a():
    global Temp
    Temp = "" + Brukerforslag + "A"
    basic.show_string("A")
    basic.clear_screen()
    sjekke_bokstav()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global Temp
    Temp = "" + Brukerforslag + "B"
    basic.show_string("B")
    basic.clear_screen()
    sjekke_bokstav()
input.on_button_pressed(Button.B, on_button_pressed_b)

def sjekke_bokstav():
    global Brukerforslag
    Brukerforslag = Temp
    serial.write_line(Brukerforslag)
    if Brukerforslag == kode:
        for index in range(3):
            basic.show_number(hemmelighet_låskoden)
    elif len(Brukerforslag) > len(kode):
        basic.show_icon(IconNames.NO)
        basic.pause(2000)
        basic.clear_screen()
        Brukerforslag = ""
Temp = ""
Brukerforslag = ""
kode = ""
hemmelighet_låskoden = 0
hemmelighet_låskoden = 3791
kode = "ABA"
Brukerforslag = ""

def on_forever():
    if len(Brukerforslag) == 0:
        basic.show_icon(IconNames.SMALL_DIAMOND)
        basic.clear_screen()
        basic.pause(500)
basic.forever(on_forever)
