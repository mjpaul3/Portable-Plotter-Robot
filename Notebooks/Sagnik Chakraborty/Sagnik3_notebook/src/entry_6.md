# Notebook Entry Lab 10/21/2024

### **Objectives**
- Count and finalize components for ordering, including resistors, capacitors, and inductors.
- Prepare the PCB design with necessary footprints for all components.
- Begin testing motor drivers and Raspberry Pi camera functionality.
- Develop and refine the ESP32 Wi-Fi interface and connections for edge-of-board placement.

### **Progress**
1. **Component Selection for PCB**:
   - Identified required values for resistors, capacitors, and inductors:
     - Capacitors: $10 \, \mu F$, $1 \, \mu F$, $4.7 \, \mu F$, $27 \, \mu F$, $180 \, \mu F$.
     - Resistors: $22 \, \Omega$, $100 \, k\Omega$, $49.9 \, k\Omega$, $1 \, k\Omega$, $10 \, k\Omega$.
     - Inductors: $1 \, \mu H$.
   - Included electrolytic capacitors for critical filtering applications, particularly $10 \, \mu F$.

2. **PCB Preparation**:
   - Reviewed the placement of IO, power, ESP32, motor drivers, and sensors on the PCB layout.
   - Noted pin configurations to optimize edge-of-board connectivity and simplify wiring during assembly.
   - Exported necessary component footprints for use in PCB design software.
   - From TA 10/22 meeting: PCB V1 seemed good; it's just that the PCB footprint had the ESP32 wifi antennae on board; this might cause issues

3. **Motor Driver Testing**:
   - Began testing the motor drivers using the ESP32. Confirmed basic operation with servo motors.
   - Encountered minor issues with pin connections, which were resolved during setup.

4. **Raspberry Pi Camera Testing**:
   - Tested the Raspberry Pi camera for position data integration. Results were satisfactory, with clear image captures and reliable interfacing.
   - Ensured compatibility with IMU for future position data calculations.

5. **ESP32 Wi-Fi Interface**:
   - Started developing the ESP32 Wi-Fi interface, focusing on stability for communication with the web app.
   - Ensured basic functionality to handle commands such as shape selection.

6. **Planning for Next Week**:
   - Outlined steps for Week 10/27:
     - Finalize ordering of components.
     - Develop a web board mockup.
     - Continue testing motors and their integration with the ESP32.
     - Work on programming ESP32 for advanced motor functions and servo tool control.

### **Next Steps**
- Complete the PCB layout and simulate the power subsystem to ensure stability under load.
- Continue testing the motor drivers and refine motor control algorithms.
- Work on integrating the Raspberry Pi camera with the web app for position data feedback.