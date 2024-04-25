# config

CFG_comport = 'COM3'
CFG_baudrate = 115200
CFG_serial_timeout = 1

CFG_no_arduino = False   # do not connect to Arduino, read data from the file (for testing)

import serial
import datetime
import time

def read_sensor_data():
    try:
        if not CFG_no_arduino:
            print('Reading from serial port %s...' % CFG_comport)
            # Before opening the serial port
            print("Opening serial port...")
            ser = serial.Serial(CFG_comport, CFG_baudrate, timeout=CFG_serial_timeout)    # open serial port
            # After opening the serial port
            print("Serial port opened successfully.")
        while True:
            if CFG_no_arduino:
                print("Reading from sensor (simulated data)...")
                # Here you would read from the sensor; since we're simulating, we'll just print some random data
                data = "S123\nB456\nQ789\n"
                print("Received data:", data.strip())
                return data.strip()
            else:
                data = ser.readline().decode('ascii').strip()  # Read the data from the serial port
                print("Received data:", data)
                return data
    except Exception as e:
        print("An error occurred:", str(e))
    finally:
        if not CFG_no_arduino:
            ser.close()  # Close the serial port
