class FaceDisplay:
    """Controls 2.1-inch round SPI display expressions using framebuffers."""
    def __init__(self):
        self.current_state = "neutral"
        print("[INIT] Round IPS face display initialized (480x480).")

    def show_expression(self, expression_name):
        self.current_state = expression_name
        print(f"[FACE DISPLAY] Expression transitioned to: -> {expression_name}")
  
