# Shinan's Worklog

##9/17/24 Dongming Meeting 1

First meeting with the legendary Dongming. Talked about project idea and asked for several recommendations positioning sensors. 

## 9/20/24 Discussion with Machine Shop

First meeting with Gregg. Discussed project idea as well as tentative timeline for project. Plan to provide part dimensions as well as a basic schematic so that the machine shop can produce a chassis.

##9/24/24 Dongming Meeting 2

Discussion of Design Doc as well as part recommendations. For example, criteria for design doc, how to start working on our circuit schematic, etc.

##9/31/24 Dongming Meeting 3

Discussion of PCB design, main concern was how exactly we should approach making microcontroller connections, as well as other relevant design concerns.

##10/08/24 Design Review

Recieved valuable feedback from professor and staff regarding the state of our project. For example, need power calculations to understand whether or not power source is sufficient enough.

##10/11/24 Circuit Schematic First Serious Draft

Basic circuit schematic designed, need to do power requirement calculations and investigate further into IC chips of choice and other details. Note that other students were running into issues with the LM117 voltage regulator for voltage drops exceeding a particular threshold due to overheating.

##10/15/24 First Round PCB Order/Dongming Meeting 4

Finalized first PCB design, recieved feedback from Dongming regarding PCB design choices. One notable point was that we should place ESP32 microcontroller with wifi module at the edge of future PCB iterations to ensure that wifi signals can be communicated accurately.

# Produced the following power calculations: 

Battery and Voltage Regulators

Battery (5 pack NiCd AA Battery)
- “Real capacity” of battery is 1500-2000 mAh
- Assume worst case battery can output up to 1500 mA continuously for about an hour
- 6 V (batteries connected in series)
- Power output: 9.6 W


6V - 5V Voltage Regulator (LM1117DT-5.0)

- Test condition of 6.5 V and a range from 0 to 800 mA of current indicate 1 mV output voltage variation and max 15 mV outside of junction temperature range
- Under the following test conditions: 5 V difference, room temperature junction:
- Can support up to 1500 mA output current 

5V - 3.3 V Voltage Regulator (TPS62A01DRLR)

- Up to 1000 mA output current
- TPS62A02 has 2000 mA max current

Sensor and Control Modules

Raspberry Pi Zero W
- 5V 230 mA with camera connected and capturing

P = 5 * .23 = 1.15 W

IMU (BMI323)
- 3.3 V	
- A + G normal Mode 690 uA
- P = 3.3 * .00069 = .002277 W
  
ESP32 - S3 WROOM
- 3.3V 500mA rated on datasheet
- Wifi and Bluetooth
- P = 3.3 * .5 1.65 W

Motor Control

Motor Driver TB6612FNG
- 6V Motor 
- 600 mA per channel max
- Need 150 mA per channel for motors x 3
- 5V Logic
- 1.8 mA maximum

Gear motor with Encoder Mouser 6V 200 rpm Adafuit Website x 3
- 6V
- 100mA current, 200mA
- Assume 150mA
- P = 6 * .150 * 3 =  2.7 W 

Servo Motor (HS-318)
- 6V
- 180 mA current, 800mA
- Assume 200mA
- P = 6 * .200 = 1.2 W

Uart Bridge (CP2102)
- 3.3 V
- Max 230 uA
- Assume 200 uA
- P = 3.3V * .0002 = .00066 W

# Total: 6.702937 W


##10/21/24 Dongming Meeting 5

Brief meeting regarding progress, at this point we are looking to order parts, communicate with machine shop.

##10/28/24 Dongming Meeting 6


