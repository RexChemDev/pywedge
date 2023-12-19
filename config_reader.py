import configparser as cp
import serial



CONFIG = cp.ConfigParser()
CONFIG.read("config.ini")

PARITY = {
    "none": serial.PARITY_NONE,
    "even": serial.PARITY_EVEN,
    "odd": serial.PARITY_ODD,
    "mark": serial.PARITY_MARK,
    "space": serial.PARITY_SPACE
}

BYTESIZE = {
    5: serial.FIVEBITS,
    6: serial.SIXBITS,
    7: serial.SEVENBITS,
    8: serial.EIGHTBITS
}

STOPBITS = {
    1: serial.STOPBITS_ONE,
    1.5: serial.STOPBITS_ONE_POINT_FIVE,
    2: serial.STOPBITS_TWO
}


def get_device():

    baud = CONFIG.getint("Device", "baud", fallback=9600)
    parity = PARITY[
        CONFIG.get("Device", "parity", fallback="none").lower()
    ]
    stopbits = STOPBITS[
        int(CONFIG.get("Device", "stopbits", fallback=1))
    ]
    bytesize = BYTESIZE[
        int(CONFIG.get("Device", "bytesize", fallback=8))
    ]
    timeout = CONFIG.getfloat("Device", "timeout", fallback=0)
    
    device = serial.Serial(
        baudrate=baud,
        parity=parity,
        stopbits=stopbits,
        bytesize=bytesize,
        timeout=timeout
    )
    return device

def serial_size() -> int:
    serial_bytes = CONFIG.getint("Extra", "serial_bytes", fallback=0)
    return serial_bytes

def kb_filter() -> dict:
    filter_str = CONFIG.get("Filter", "blacklist", fallback="")
    if filter_str == "":
        return {}
    
    tr_table = {ord(letter): "" for letter in filter_str}
    return tr_table
    

