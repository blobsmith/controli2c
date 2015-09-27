import ctypes

c_uint8 = ctypes.c_uint8
class Leds_bits( ctypes.LittleEndianStructure ):
    _fields_ = [
                ("led1",    c_uint8, 1 ),  # asByte & 1
                ("led2",    c_uint8, 1 ),  # asByte & 2
                ("led3",    c_uint8, 1 ),  # asByte & 4
                ("led4",    c_uint8, 1 ),  # asByte & 8
                ("led5",    c_uint8, 1 ),  # asByte & 16
              ]

class Leds( ctypes.Union ):
    _fields_ = [
                ("b",      Leds_bits ),
                ("asByte", c_uint8    )
               ]
    _anonymous_ = ("b")