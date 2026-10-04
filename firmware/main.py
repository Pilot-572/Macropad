import board
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation


keyboard = KMKKeyboard()
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)
keyboard.extensions.append(MediaKeys())
keyboard.col_pins = (board.D3, board.D6, board.D7)
keyboard.row_pins = (board.D0, board.D1, board.D2)
encoder_handler.pins = ((board.D8, board.D9, board.D10, False),)
keyboard.diode_orientation = DiodeOrientation.COL2ROW
keyboard.keymap = [
    [KC.MPRV, KC.MPLY, KC.MNXT,
     KC.NO, KC.NO, KC.NO,
     KC.NO, KC.NO, KC.NO]
]
encoder_handler.map = [((KC.VOLD, KC.VOLU, KC.MUTE),)]


if __name__ == "__main__":
    keyboard.go()