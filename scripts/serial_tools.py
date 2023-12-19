import serial
from serial.tools.list_ports import comports


def get_data(dev: serial.Serial, serial_bytes: int = 0) -> str:
    "Reads data from serial device. Will block for duration of device timeout, or until [serial_bytes] number of bytes have been read."

    assert type(dev) is serial.Serial, f"{dev} must be a serial object."
    with dev:
        #print(f"Listening on device {dev.name}...")
        if serial_bytes > 0:
            outstring = dev.read(serial_bytes)
        else:
            outstring = dev.readline()
        
        if outstring:
            return outstring
        else:
            return None


def get_ports(silent=False, quiet_fail=False) -> dict:
    if not quiet_fail and not(comports()):
        raise RuntimeError("No serial devices found.")

    ports = {}
    if not silent: 
        print("Available ports:")
    for index, port in enumerate(comports()):
        if not silent:
            print(f"[{index}] {port}")
        ports[index] = port.name
    return ports