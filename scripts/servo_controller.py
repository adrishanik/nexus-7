import serial
import time

class ServoController:
    """Handles UART daisy-chained Waveshare ST3215 serial bus servos."""
    def __init__(self, port="/dev/ttyS2", baud=1000000):
        self.port_name = port
        self.baud = baud
        self.ser = None
        try:
            self.ser = serial.Serial(self.port_name, self.baud, timeout=0.05)
        except Exception as e:
            print(f"[WARN] Serial port not accessible ({e}). Running in simulation mode.")

    def set_servo_position(self, servo_id, position, speed=1000):
        """Send ST3215 position packet (0-4095)."""
        if not self.ser:
            return
        pos_h = (position >> 8) & 0xFF
        pos_l = position & 0xFF
        spd_h = (speed >> 8) & 0xFF
        spd_l = speed & 0xFF
        packet = bytearray([0xFF, 0xFF, servo_id, 0x07, 0x03, 0x2A, pos_h, pos_l, spd_h, spd_l])
        checksum = (~(sum(packet[2:]) & 0xFF)) & 0xFF
        packet.append(checksum)
        self.ser.write(packet)

    def center_all_joints(self):
        for sid in range(1, 11):
            self.set_servo_position(sid, 2048, 500)
            time.sleep(0.02)

    def gesture_wave(self):
        self.set_servo_position(7, 2800, 1000)
        time.sleep(0.3)
        for _ in range(2):
            self.set_servo_position(9, 2600, 1200)
            time.sleep(0.3)
            self.set_servo_position(9, 1800, 1200)
            time.sleep(0.3)
        self.set_servo_position(7, 2048, 800)
      
