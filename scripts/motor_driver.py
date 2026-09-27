class TrackMotorDriver:
    """Controls BTS7960 43A H-Bridge dual DC crawler tracks."""
    def __init__(self, pins):
        self.pins = pins
        print(f"[INIT] Motor driver configured on pins: {pins}")

    def set_drive_speed(self, left_speed, right_speed):
        """Speed range: -100 to 100."""
        pass

    def stop(self):
        self.set_drive_speed(0, 0)
      
