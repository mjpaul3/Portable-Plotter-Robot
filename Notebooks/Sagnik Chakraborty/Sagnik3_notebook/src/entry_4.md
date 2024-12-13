# Notebook Entry Lab 10/07/2024

### **Objectives**
- Begin PCB design calculations for PCB review.
- Perform power analytics calculations to ensure all subsystems are properly powered.

### **Progress**



#### 10/11 meeting:

1. **PCB Design Calculations**:
   - Reviewed the application circuit for the **TPS62140DCLR** voltage regulator.
   - Calculated resistor divider values ($ R_1 $ and $ R_2 $) to achieve an output voltage ($ V_{\text{out}} $) of 3.3V.
     - Used the formula:
       $$
       V_{\text{out}} = 1.2 \times \left( 1 + \frac{R_2}{R_1} \right)
       $$
       Result:
       - $ R_1 = 100 \, k\Omega $
       - $ R_2 = 450 \, k\Omega $
   - Verified that the selected capacitor values meet the TPS62140DCLR's application guidelines.

2. **Power Subsystem Analysis**:
   - Measured current requirements for each subsystem:
     - **ESP32**: 300mA.
     - **Plotter Car Control Subsystem**: 500mA.
     - **Motor Subsystem**: Calculated based on servo and DC motor driver requirements.
   - Ensured the battery and voltage regulator could supply sufficient current for all subsystems under peak load conditions.

3. **Updated Block Diagram**:
   - Created a detailed block diagram to map the power flow and subsystem interconnections.
   - Incorporated feedback from previous TA meetings to ensure all connections were labeled clearly.

4. **Component Placement Considerations**:
   - Added a $ C_3 $ optional capacitor to reduce noise in the power line.
   - Verified placement for efficient routing of power and signal lines, especially for the ESP32 and motor drivers.

### **Next Steps**
- Finalize the PCB layout for review, focusing on minimizing noise and ensuring reliable connections.
- Simulate the power system under various loads to confirm voltage stability.

