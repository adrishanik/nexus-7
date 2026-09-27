#!/usr/bin/env python3
"""
Nexus-7 Main Orchestration Loop
Integrates Edge LLM, Voice, Expressive Face Display, and Actuation.
"""

import time
import json
import logging
from servo_controller import ServoController
from motor_driver import TrackMotorDriver
from llm_engine import LocalLLMEngine
from face_display import FaceDisplay

logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')

def main():
    logging.info("Initializing Nexus-7 Edge-AI Systems...")
    with open("config.json", "r") as f:
        config = json.load(f)

    servos = ServoController(
        port=config['hardware']['servo_serial_port'],
        baud=config['hardware']['servo_baudrate']
    )
    chassis = TrackMotorDriver(pins=config['motor_driver'])
    face = FaceDisplay()
    llm = LocalLLMEngine(
        model=config['llm']['model_name'],
        api_url=config['llm']['ollama_api_url']
    )

    face.show_expression("neutral")
    servos.center_all_joints()
    logging.info("Nexus-7 fully calibrated and operational.")

    try:
        while True:
            # Main cycle: Audio wake detection -> LLM processing -> Motion response
            face.show_expression("listening")
            time.sleep(1)
            
            # Demonstration query simulation
            face.show_expression("thinking")
            prompt = "Status check."
            response = llm.generate_response(prompt)
            logging.info(f"LLM Response: {response}")
            
            face.show_expression("happy")
            servos.gesture_wave()
            time.sleep(3)
            face.show_expression("neutral")
            time.sleep(5)

    except KeyboardInterrupt:
        logging.info("Shutdown signal received. Parking robot safely.")
        chassis.stop()
        servos.center_all_joints()
        face.show_expression("sleep")

if __name__ == "__main__":
    main()
