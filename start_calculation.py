import ctypes
from datetime import date
from typing import List


def start_calculation(dt: date, in_folder: str, out_folder: str, hours: List[int], hours_num: int, max_iter: int) -> int:

    # status 0 - success
    status = 0

    # load cpp library
    eq_lib = ctypes.CDLL('./libequillibrium.0.1.dylib')

    # set returning type to function alias
    eq_lib.startCalculation.restype = ctypes.c_int

    # set types for input parameters
    eq_lib.startCalculation.argtypes = [ctypes.c_char_p,
                                        ctypes.c_char_p,
                                        ctypes.POINTER(ctypes.c_int),
                                        ctypes.c_int,
                                        ctypes.c_int]

    # invoke c++ function
    hoursP = (ctypes.c_int * hours_num)(*hours)
    res = eq_lib.startCalculation(in_folder.encode('utf-8'),
                                  out_folder.encode('utf-8'),
                                  hoursP,
                                  hours_num,
                                  max_iter)

    status = res

    return status
