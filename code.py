from keyboard import *

keyboard = Keyboard()

___ = TRANSPARENT
BOOT = BOOTLOADER
L1 = LAYER_TAP(1)
L2CAPS = LAYER_TAP(2)
LSFT4 = LAYER_MODS(4, MODS(LSHIFT))
RSFT4 = LAYER_MODS(4, MODS(RSHIFT))

# Semicolon & Ctrl
SCC = MODS_TAP(MODS(RCTRL), ';')

keyboard.keymap = (
    # layer 0
    (
        ESC,   1,   2,   3,   4,   5,   6,   7,   8,   9,   0, '-', '=', BACKSPACE,
        TAB,   Q,   W,   E,   R,   T,   Y,   U,   I,   O,   P, '[', ']', '|',
        L2CAPS,  A,   S, D,   F,   G,   H,   J,   K,   L, SCC, '"',    ENTER,
        LSHIFT, Z,   X,   C,   V, B,   N,   M, ',', '.', '/',         UP,
        LCTRL, LGUI, LALT,          SPACE,            L1, LEFT,  DOWN, RIGHT
    ),

    # layer 1
    (
        '`',  F1,  F2,  F3,  F4,  F5,  F6,  F7,  F8,  F9, F10, F11, F12, DEL,
        MACRO(0), ___,  ___, ___, ___, ___, ___, ___, ___, ___,___,___,___,___,
        CAPS,TRANSPORT_PLAY_PAUSE,TRANSPORT_PREV_TRACK,TRANSPORT_NEXT_TRACK,AUDIO_MUTE, AUDIO_VOL_DOWN, AUDIO_VOL_UP, ___, ___, ___, ___, ___,      ___,
        ___, BT1, BT2, BT3, BT4,BT5, MACRO(1), ___, ___, ___, ___,       ___,
        ___, ___, ___,                BT_TOGGLE,               ___, ___, ___,  ___
    ),

    # layer 2
    (
        '`',  F1,  F2,  F3,  F4,  F5,  F6,  F7,  F8,  F9, F10, F11, F12, DEL,
        ___, ___, ___, ___, ___, ___, ___,___, ___, ___, ___,AUDIO_VOL_DOWN,AUDIO_VOL_UP,AUDIO_MUTE,
        ___, ___, ___, ___, ___, ___,HOME,PGDN, PGUP,END, ___, ___,      ___,
        ___, ___, ___, ___, ___, ___,___, ___, ___, ___, ___,           ___,
        ___, ___, ___,                ___,               ___, ___, ___,  ___
    ),

    # layer 3
    (
        BT_TOGGLE,BT1,BT2, BT3,BT4,BT5,BT6,BT7, BT8, BT9, BT0, ___, ___, ___,
        RGB_MOD, ___, ___, ___, ___, ___,___,USB_TOGGLE,___,___,___,___,___, ___,
        RGB_TOGGLE, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___,      ___,
        ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___,           ___,
        ___, ___, ___,                ___,               ___, ___, ___,  ___
    ),

    # layer 4
    (
        '`', ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___,
        ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___,
        ___, ___, ___,   D, ___, ___, ___, ___, ___, ___, ';', ___,      ___,
        ___, ___, ___, ___, ___,   B, ___, ___, ___, ___, ___,           ___,
        ___, ___, ___,                ___,               ___, ___, ___,  ___
    ),
)

def rshift_tab(dev, is_down):
    if is_down:
        dev.press(RSHIFT)
        dev.press(TAB)
    else:
        dev.release(TAB)
        dev.release(RSHIFT)

def rshift_n(dev, is_down):
    if is_down:
        dev.press(RSHIFT)
        dev.press(N)
    else:
        dev.release(N)
        dev.release(RSHIFT)

def macro_handler(dev, n, is_down):
    if n == 0:
        rshift_tab(dev, is_down)
    elif n == 1:
        rshift_n(dev, is_down)

def pairs_handler(dev, n):
    dev.send_text('You just triggered pair keys #{}\n'.format(n))


keyboard.macro_handler = macro_handler
keyboard.pairs_handler = pairs_handler

# Pairs: J & K, U & I
#keyboard.pairs = [{35, 36}, {20, 19}]

keyboard.verbose = False

keyboard.run()
