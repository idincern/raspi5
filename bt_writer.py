import serial

def write_to_serial_once(port, baudrate=9600, timeout=1):
    try:
        # Initialize serial connection
        ser = serial.Serial(port, baudrate, timeout=timeout)
        print(f"Connected to {port} at {baudrate} baud")

        # Message to send
        message = '{"service":{"command":"EXECUTE","name":"shade-pro-service.BackendReady","params":{},"api":true}}'

        # Write data to serial port
        ser.write(message.encode('utf-8'))
        print(f"Sent: {message}")

    except serial.SerialException as e:
        print(f"Error: {e}")
    finally:
        if ser.is_open:
            ser.close()
            print("Serial connection closed")

if __name__ == "__main__":
    write_to_serial_once('/dev/rfcomm0')
