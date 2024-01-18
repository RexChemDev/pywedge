import config_reader
import keyboard as kb
import scripts.serial_tools as st
import scripts.loadingthread as lt
import platform
from multiprocessing import Process, freeze_support


logo = """

    ______  ___       ____________  ____________
   / __ \ \/ / |     / / ____/ __ \/ ____/ ____/
  / /_/ /\  /| | /| / / __/ / / / / / __/ __/   
 / ____/ / / | |/ |/ / /___/ /_/ / /_/ / /___   
/_/     /_/  |__/|__/_____/_____/\____/_____/   
                                                
"""


def port_selection() -> str:
    try:
        ports = st.get_ports()
    except RuntimeError as e:
        print(e)
        input("Press any key to continue.")
        exit()
    while True:
        try:
            selected_port = input("Select serial device (index):\n> ")
            if selected_port == "q":
                print("Shutting down...")
                exit()
            portname = ports[int(selected_port)]
            return portname
        except (KeyError, ValueError):
            print(f"'{selected_port}' is not a valid port index.")
            st.get_ports()

def readloop(device, readsize, tr_table):
    while True:
        serial_str = st.get_data(device, serial_bytes=readsize)  
        
        if serial_str:
            out_str = serial_str.decode().translate(tr_table).strip()
            out_str += "\n"
            print(f"Got string: {serial_str}")
            print(f"Translated to: {repr(out_str)}\n")
            kb.write(out_str)

def main():
    print(logo)
    os_name = platform.system()
    print(os_name, "\n")

    portname = port_selection()
    if os_name == "Linux":
        portname = f"/dev/{portname}"

    device = config_reader.get_device()
    device.port = portname
    readsize = config_reader.serial_size()
    tr_table = config_reader.kb_filter()
    print(device)

    job1 = Process(target=readloop, args=[device, readsize, tr_table])
    job2 = Process(target=lt.loading)

    job1.start()
    job2.start()

if __name__ == "__main__":
    freeze_support()
    main()

