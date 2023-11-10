import cpp_structs as cpps
import ctypes
from datetime import date
from typing import List


def start_calculation_with_struct(dt: date, states: List[cpps.HourState], hours: List[int], hours_num: int, max_iter: int) -> int:

    # status 0 - success
    status = 0

    # load cpp library
    eq_lib = ctypes.CDLL('./libequillibrium.0.1.dylib')

    # set returning type to function alias
    eq_lib.startCalculationWithStruct.restype = ctypes.c_int

    # set types for input parameters
    eq_lib.startCalculationWithStruct.argtypes = [ctypes.POINTER(cpps.HourState),
                                        ctypes.POINTER(ctypes.c_int),
                                        ctypes.c_int,
                                        ctypes.c_int]

    # invoke c++ function
    hoursP = (ctypes.c_int * hours_num)(*hours)
    states_p = (cpps.HourState * len(states))(*states)
    res = eq_lib.startCalculationWithStruct(states_p, hoursP, hours_num, max_iter)

    status = res

    return status