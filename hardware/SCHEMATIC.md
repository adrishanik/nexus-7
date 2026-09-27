# Nexus-7 Electrical & Wiring Schematic

## 1. System Power Architecture

Nexus-7 utilizes a dual-rail power topology to completely isolate high-current inductive motor spikes from sensitive digital logic.

```
                  [ 12V 3S 6000mAh Li-ion Battery Pack ]
                                    │
                       [ Panel E-Stop Switch (40A) ]
                                    │
          ┌─────────────────────────┴─────────────────────────┐
          │                                                   │
   [ Direct 12V Rail ]                                 [ Direct 12V Rail ]
          │                                                   │
          ▼                                                   ▼
┌──────────────────┐                                ┌──────────────────┐
│ Waveshare ST3215 │                                │ BTS7960 43A Dual │
│ Servo Bus Board  │                                │ H-Bridge Driver  │
└────────┬─────────┘                                └────────┬─────────┘
         │                                                   │
         ▼                                                   ▼
[ 10x ST3215 Servos ]                             [ 2x 12V DC Track Motors ]
(Arms, Grippers, Neck)                            (Left & Right Drive Tracks)

                                    │
                                    ▼
                 [ 12V-to-5V 10A Synchronous Buck Converter ]
                                    │
          ┌─────────────────────────┴─────────────────────────┐
          │                                                   │
   [ Regulated 5V Rail ]                               [ Regulated 5V Rail ]
          │                                                   │
          ▼                                                   ▼
┌───────────────────────┐                           ┌──────────────────┐
│ Orange Pi 5 Plus SBC  │                           │ 2.1" IPS Screen  │
│ (Type-C / 5V GPIO In) │                           │ ReSpeaker 4-Mic  │
└───────────────────────┘                           │ MAX98357A I2S    │
                                                    └──────────────────┘
```

---

## 2. Power Rail Specifications

| Rail Voltage | Source / Regulator | Maximum Current | Connected Subsystems |
| :--- | :--- | :--- | :--- |
| **12.0V Direct** | 3S Li-ion Battery via E-Stop | 25A Peak | 10x ST3215 Bus Servos, BTS7960 Track Motor Driver |
| **5.0V Regulated**| 12V-to-5V Buck Converter | 10A Continuous | Orange Pi 5 Plus, 2.1" IPS Round Display, ReSpeaker Mic Array, MAX98357A DAC Amp |
| **3.3V Logic** | Orange Pi Onboard LDO | 500mA | MPU6050 6-Axis IMU, SPI/I2C Level Shift |

---

## 3. Communication & Signal Interconnects

### A. High-Torque Servo Bus (UART2)
* **Protocol:** Half-Duplex Asynchronous Serial (1,000,000 baud)
* **Controller Interface:**
  * Orange Pi Pin 8 (`UART2_TX`) ───> Waveshare Servo Board `RX`
  * Orange Pi Pin 10 (`UART2_RX`) ───> Waveshare Servo Board `TX`
  * Orange Pi Pin 6 (`GND`) ────────> Waveshare Servo Board `GND`
* **Bus Routing:** Daisy-chain wiring harness across all 10 ST3215 servos with power supplied directly from the 12V rail.

### B. Track Mobility Driver (BTS7960 43A Dual DC)
* **Control Lines:**
  * `VCC` ───> 5V Regulated Rail
  * `GND` ───> Common Digital Ground
  * `L_EN` & `R_EN` ───> 5V Logic Rail (Permanently Enabled)
  * `RPWM1` (Left Track Forward)  ───> Orange Pi Pin 35 (`PWM0`)
  * `LPWM1` (Left Track Reverse)  ───> Orange Pi Pin 36 (`PWM1`)
  * `RPWM2` (Right Track Forward) ───> Orange Pi Pin 37 (`PWM2`)
  * `LPWM2` (Right Track Reverse) ───> Orange Pi Pin 38 (`PWM3`)

### C. Expressive Face Display (2.1-inch Round IPS Display)
* **Protocol:** High-Speed SPI (SPI1)
* **Wiring:**
  * `VCC` ───> 5V Regulated Rail
  * `GND` ───> Digital Ground
  * `DIN` (MOSI) ───> Orange Pi Pin 19 (`SPI1_MOSI`)
  * `CLK` (SCLK) ───> Orange Pi Pin 23 (`SPI1_SCLK`)
  * `CS`  (Chip Select) ───> Orange Pi Pin 24 (`SPI1_CS0`)
  * `DC`  (Data/Command) ───> Orange Pi Pin 22 (`GPIO3_C3`)
  * `RST` (Reset) ───> Orange Pi Pin 18 (`GPIO3_C2`)
  * `BL`  (Backlight) ───> 3.3V / PWM Dimming

### D. Stereo Vision Camera (Dual IMX219 Depth Module)
* **Interface:** Dual 2-Lane MIPI CSI-2 Camera Ribbon Interfaces
* **Connection:** Plugged directly into `CAM1` and `CAM2` FPC connectors on the Orange Pi 5 Plus carrier board.

### E. Audio Ingestion & Acoustic Direction (ReSpeaker 4-Mic Array)
* **Interface:** High-Speed USB 2.0 / I2S Bus
* **Connection:** Standard low-profile USB 2.0 port on the Orange Pi 5 Plus.

### F. Speech Output Amplifier (MAX98357A I2S Class-D DAC)
* **Protocol:** Digital I2S Audio Bus
* **Wiring:**
  * `VIN`  ───> 5V Regulated Rail
  * `GND`  ───> Digital Ground
  * `LRC`  (Word Select) ───> Orange Pi Pin 40 (`I2S0_LRCK`)
  * `BCLK` (Bit Clock)    ───> Orange Pi Pin 12 (`I2S0_SCLK`)
  * `DIN`  (Serial Data)  ───> Orange Pi Pin 33 (`I2S0_SDI / DOUT`)
  * Speaker output terminals connected to 4Ω 3W cavity micro-speaker.

### G. Spatial Pose & Tilt Safety (MPU6050 6-Axis IMU)
* **Protocol:** I2C Bus (Address: `0x68`)
* **Wiring:**
  * `VCC` ───> 3.3V Logic Rail
  * `GND` ───> Digital Ground
  * `SDA` ───> Orange Pi Pin 27 (`I2C3_SDA`)
  * `SCL` ───> Orange Pi Pin 28 (`I2C3_SCL`)

---

## 4. Grounding & Safety Implementation

1. **Star Grounding:** All subsystem grounds (12V Battery Ground, 5V Buck Output Ground, and Orange Pi Logic Ground) terminate at a central heavy-gauge star ground junction point to eliminate ground loops.
2. **Emergency Cutoff (E-Stop):** A latching mushroom emergency push switch is installed directly between the 12V Li-ion battery positive terminal and the primary distribution bus to disconnect all power instantly if triggered.
3. **Decoupling Capacitors:** A 1000µF 25V low-ESR electrolytic capacitor is placed across the 12V input terminals of the servo bus and motor driver to suppress transient back-EMF spikes during rapid arm acceleration or track braking.
