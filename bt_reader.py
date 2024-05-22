import serial
import time

def read_from_serial(port, baudrate=9600, timeout=1):
    try:
        # Initialize serial connection
        ser = serial.Serial(port, baudrate, timeout=timeout)
        print(f"Connected to {port} at {baudrate} baud")

        while True:
            # Read data from serial port
            if ser.in_waiting > 0:
                data = ser.readline().decode('utf-8').rstrip()
                print(data)

    except serial.SerialException as e:
        print(f"Error: {e}")
    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        if ser.is_open:
            ser.close()
            print("Serial connection closed")

if __name__ == "__main__":
    read_from_serial('/dev/rfcomm0')
