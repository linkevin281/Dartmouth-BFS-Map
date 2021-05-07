# name: Kevin Lin


KEY1 = "1"
KEY2 = "2"
KEY3 = "3"
KEY4 = "4"
KEY5 = "5"
KEY6 = "6"
KEY7 = "7"
KEY8 = "8"
KEY9 = "9"
KEY0 = "0"
KEYA = "a"
KEYB = "b"
KEYC = "c"
KEYD = "d"
KEYE = "e"
KEYF = "f"
KEYG = "g"
KEYH = "h"
KEYI = "i"
KEYJ = "j"
KEYK = "k"
KEYL = "l"
KEYM = "m"
KEYN = "n"
KEYO = "o"
KEYP = "p"
KEYQ = "q"
KEYR = "r"
KEYS = "s"
KEYT = "t"
KEYU = "u"
KEYV = "v"
KEYW = "w"
KEYX = "x"
KEYY = "y"
KEYZ = "z"
KEY_SPACE = " "
KEY_EQUAL = "="

pressed1 = False
pressed2 = False
pressed3 = False
pressed4 = False
pressed5 = False
pressed6 = False
pressed7 = False
pressed8 = False
pressed9 = False
pressed0 = False
presseda = False
pressedb = False
pressedc = False
pressedd = False
pressede = False
pressedf = False
pressedg = False
pressedh = False
pressedi = False
pressedj = False
pressedk = False
pressedl = False
pressedm = False
pressedn = False
pressedo = False
pressedp = False
pressedq = False
pressedr = False
presseds = False
pressedt = False
pressedu = False
pressedv = False
pressedw = False
pressedx = False
pressedy = False
pressedz = False
pressed_space = False
pressed_equal = False



def key_down(key): # checks if a key is pressed
    global presseda, pressedb, pressedc, pressedd, pressede, pressedf, pressedg, pressedh, pressedi, pressedj, pressedk
    global pressedl, pressedm, pressedn, pressedo, pressedp, pressedq, pressedr, presseds, pressedt, pressedu, pressedv
    global pressedw, pressedx, pressedy, pressedz, pressed_space, pressed1, pressed2, pressed3, pressed4, pressed0
    global pressed_equal, pressed5, pressed6, pressed7, pressed8, pressed9

    if key == KEY1:
        pressed1 = True
    if key == KEY2:
        pressed2 = True
    if key == KEY3:
        pressed3 = True
    if key == KEY4:
        pressed4 = True
    if key == KEY5:
        pressed5 = True
    if key == KEY6:
        pressed6 = True
    if key == KEY7:
        pressed7 = True
    if key == KEY8:
        pressed8 = True
    if key == KEY9:
        pressed9 = True
    if key == KEY0:
        pressed0 = True
    if key == KEYA:
        presseda = True
    if key == KEYB:
        pressedb = True
    if key == KEYC:
        pressedc = True
    if key == KEYD:
        pressedd = True
    if key == KEYE:
        pressede = True
    if key == KEYF:
        pressedf = True
    if key == KEYG:
        pressedg = True
    if key == KEYH:
        pressedh = True
    if key == KEYI:
        pressedi = True
    if key == KEYJ:
        pressedj = True
    if key == KEYK:
        pressedk = True
    if key == KEYL:
        pressedl = True
    if key == KEYM:
        pressedm = True
    if key == KEYN:
        pressedn = True
    if key == KEYO:
        pressedo = True
    if key == KEYP:
        pressedp = True
    if key == KEYQ:
        pressedq = True
    if key == KEYR:
        pressedr = True
    if key == KEYS:
        presseds = True
    if key == KEYT:
        pressedt = True
    if key == KEYU:
        pressedu = True
    if key == KEYV:
        pressedv = True
    if key == KEYW:
        pressedw = True
    if key == KEYX:
        pressedx = True
    if key == KEYY:
        pressedy = True
    if key == KEYZ:
        pressedz = True
    if key == KEY_SPACE:
        pressed_space = True
    if key == KEY_EQUAL:
        pressed_equal = True


def key_up(key): # checks if a key is released
    global presseda, pressedb, pressedc, pressedd, pressede, pressedf, pressedg, pressedh, pressedi, pressedj, pressedk
    global pressedl, pressedm, pressedn, pressedo, pressedp, pressedq, pressedr, presseds, pressedt, pressedu, pressedv
    global pressedw, pressedx, pressedy, pressedz, pressed_space, pressed1, pressed2, pressed3, pressed4, pressed0
    global pressed_equal, pressed5, pressed6, pressed7, pressed8, pressed9

    if key == KEY1:
        pressed1 = False
    if key == KEY2:
        pressed2 = False
    if key == KEY3:
        pressed3 = False
    if key == KEY4:
        pressed4 = False
    if key == KEY5:
        pressed5 = False
    if key == KEY6:
        pressed6 = False
    if key == KEY7:
        pressed7 = False
    if key == KEY8:
        pressed8 = False
    if key == KEY9:
        pressed9 = False
    if key == KEY0:
        pressed0 = False
    if key == KEYA:
        presseda = False
    if key == KEYB:
        pressedb = False
    if key == KEYC:
        pressedc = False
    if key == KEYD:
        pressedd = False
    if key == KEYE:
        pressede = False
    if key == KEYF:
        pressedf = False
    if key == KEYG:
        pressedg = False
    if key == KEYH:
        pressedh = False
    if key == KEYI:
        pressedi = False
    if key == KEYJ:
        pressedj = False
    if key == KEYK:
        pressedk = False
    if key == KEYL:
        pressedl = False
    if key == KEYM:
        pressedm = False
    if key == KEYN:
        pressedn = False
    if key == KEYO:
        pressedo = False
    if key == KEYP:
        pressedp = False
    if key == KEYQ:
        pressedq = False
    if key == KEYR:
        pressedr = False
    if key == KEYS:
        presseds = False
    if key == KEYT:
        pressedt = False
    if key == KEYU:
        pressedu = False
    if key == KEYV:
        pressedv = False
    if key == KEYW:
        pressedw = False
    if key == KEYX:
        pressedx = False
    if key == KEYY:
        pressedy = False
    if key == KEYZ:
        pressedz = False
    if key == KEY_SPACE:
        pressed_space = False
    if key == KEY_EQUAL:
        pressed_equal = False