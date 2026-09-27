# Nexus-7 Pinout Reference Sheet

### 40-Pin Header Configuration (Orange Pi 5 Plus)

| Pin # | Pin Name | Peripheral | Connected Device / Function |
|:---:|:---:|:---:|:---|
| 2 | 5V_VCC | Power | 5V Logic In (from 10A Buck) |
| 4 | 5V_VCC | Power | 5V Display / Mic Array |
| 6 | GND | Power | Common Ground Rail |
| 8 | UART2_TX | Serial | Waveshare Servo Bus RX |
| 10 | UART2_RX | Serial | Waveshare Servo Bus TX |
| 12 | I2S0_SCLK| I2S | MAX98357A BCLK |
| 19 | SPI1_MOSI| SPI | 2.1" IPS Round Display MOSI |
| 23 | SPI1_SCLK| SPI | 2.1" IPS Round Display SCLK |
| 24 | SPI1_CS0 | SPI | 2.1" IPS Round Display Chip Select |
| 27 | I2C3_SDA | I2C | MPU6050 6-Axis IMU SDA |
| 28 | I2C3_SCL | I2C | MPU6050 6-Axis IMU SCL |
| 35 | PWM_0 | GPIO/PWM | BTS7960 Left Motor Forward |
| 36 | PWM_1 | GPIO/PWM | BTS7960 Left Motor Reverse |
| 37 | PWM_2 | GPIO/PWM | BTS7960 Right Motor Forward |
| 38 | PWM_3 | GPIO/PWM | BTS7960 Right Motor Reverse |
| 39 | GND | Power | Digital Ground |
| 40 | I2S0_LRCK| I2S | MAX98357A LRCK (Word Select) |
