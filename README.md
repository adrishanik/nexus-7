# Nexus-7: Autonomous Humanoid Edge-AI Robotic Assistant

Nexus-7 is an autonomous upper-torso humanoid robotic assistant mounted on a high-stability crawler chassis. Designed for complete edge intelligence, it runs local small language models (TinyLlama / Llama-3.2-1B) and neural voice processing entirely offline using the onboard 6 TOPS NPU of an Orange Pi 5 Plus (16GB RAM).

---

## Key Features

- **Offline Edge LLM:** Runs quantized local language models via `llama.cpp` / Ollama with zero cloud API dependencies.
- **Far-Field Voice Interaction:** 4-microphone beamforming array with Direction of Arrival (DoA) audio tracking and offline Whisper speech recognition.
- **Expressive 2.1" Round IPS Face:** Dynamic animated expressions rendered via LVGL reflecting real-time conversational states and telemetry.
- **Stereo Spatial Vision:** Dual IMX219 cameras feeding OpenCV and ROS 2 nodes for depth estimation and obstacle identification.
- **High-Torque 10-DOF Serial Bus Actuation:** Waveshare ST3215 magnetic encoder servos (30 kg·cm) with real-time positional and thermal telemetry.
- **Compliant Underactuated Grippers:** Tendon-driven finger linkages capable of dynamically wrapping around varied geometric objects.
- **Dynamic Tracked Mobility Base:** Dual metal-gear DC motors driving continuous rubber tracks to eliminate bipedal tipping hazards.
- **Self-Contained Power Subsystem:** 12V 3S Li-ion cell with integrated BMS and hardware push-latch emergency cutoff.

---

## System Architecture & Hardware Pinout

| Module | Interface / Protocol | Host Pin / Port | Function |
| :--- | :--- | :--- | :--- |
| **ST3215 Servo Bus** | Hardware UART | UART2 (TX/RX) via Driver Board | 10x Daisy-chained body servos |
| **BTS7960 Driver** | PWM / Digital GPIO | GPIO1_A3, GPIO1_A4, GPIO1_B0, GPIO1_B1 | Track base speed & steering |
| **2.1" IPS Screen** | High-Speed SPI | SPI1 (SCK, MOSI, CS, DC, RST) | Facial animations (LVGL) |
| **IMX219 Stereo Cam**| MIPI-CSI / USB Bridge | Dual CSI-2 Ports / USB 3.0 | 3D Depth Perception & SLAM |
| **ReSpeaker 4-Mic** | USB / I2S | USB 2.0 Host Port | Beamformed audio capture |
| **MAX98357A DAC** | I2S Digital Audio | I2S0 (BCLK, LRCK, DIN) | Offline Piper TTS voice audio |
| **MPU6050 IMU** | I2C | I2C3 (SDA, SCL) | Torso stabilization & tilt safety |

---

## Power Distribution Architecture

- **Primary Source:** 12V (11.1V nominal) 6000mAh 3S high-drain Li-ion battery pack protected by onboard BMS.
- **Direct 12V Bus:** Directly powers the 10x ST3215 serial servos and BTS7960 motor driver.
- **Regulated 5V 10A Bus:** Synchronous buck converter steps down 12V to clean 5V to run the Orange Pi 5 Plus, displays, and audio electronics.
- **Safety Interlock:** Heavy-duty physical E-stop switch located inline on the main positive battery terminal.

---

## Project Structure

├── BOM.csv
├── README.md
├── LICENSE
├── requirements.txt
├── config.json
├── hardware/
│   ├── SCHEMATIC.md
│   ├── PINOUT.md
│   └── 3D_PRINTING_GUIDE.md
├── scripts/
│   ├── main_robot.py
│   ├── llm_engine.py
│   ├── servo_controller.py
│   ├── motor_driver.py
│   └── face_display.py

---

## Bill of Materials

All itemized components, part links, and costs are documented in [`BOM.csv`](./BOM.csv).
