### Notebook Entry Lab 11/18/24

## Objectives
- Set up a test bench on the development board for basic servo motor control code.
- Verify the functionality of servo motor control using PWM signals with an ESP32.

## Progress
This week, I focused on implementing and testing servo motor control using an ESP32 development board. The servo was controlled through a PWM signal configured with a 50Hz frequency and 14-bit resolution. Below are the key components of the implementation:

---

### Code Explanation

#### **1. Pin Configuration**
The servo was connected to GPIO 13. Additionally, GPIOs 36, 35, and 1 were set to always output `HIGH` to stabilize auxiliary components.

```cpp
// Pin definitions
#define SERVO_PIN 13
#define SERVO_HIGH_1 36
#define SERVO_HIGH_2 35
#define GPIO_HIGH_1 1
```

#### **2. PWM Timer Configuration**
A PWM signal with a frequency of 50Hz (20ms period) was used to control the servo motor. The timer was set to 14-bit resolution, allowing a duty cycle range of 0 to 16383.

```cpp
ledc_timer_config_t ledc_timer = {
    .speed_mode = PWM_MODE,
    .duty_resolution = PWM_RESOLUTION,
    .timer_num = PWM_TIMER,
    .freq_hz = PWM_FREQ,
    .clk_cfg = LEDC_AUTO_CLK
};
esp_err_t timer_err = ledc_timer_config(&ledc_timer);
```

#### **3. Duty Cycle Calculation**
The pulse width for the servo was calculated based on the desired angle, mapped to the servo’s minimum and maximum pulse widths (544µs to 2400µs). The calculated pulse width was converted to the appropriate duty cycle for the PWM signal.

Mathematically:
$$
\text{Pulse Width (µs)} = \text{SERVO\_MIN\_PULSEWIDTH} + \left(\frac{\text{SERVO\_MAX\_PULSEWIDTH} - \text{SERVO\_MIN\_PULSEWIDTH}}{180} \cdot \text{Angle}\right)
$$

$$
\text{Duty Cycle} = \frac{\text{Pulse Width (µs)} \cdot \text{Max Resolution}}{\text{PWM Period (µs)}}
$$

For example:
- At 0°: Pulse width = 544µs, duty = 445.
- At 180°: Pulse width = 2400µs, duty = 1966.

#### **4. Angle Testing**
The `setServoAngle` function was implemented to move the servo to specified angles between 0° and 180°:
```cpp
void setServoAngle(uint8_t angle) {
    // Convert angle to pulse width
    uint32_t pulseWidth = SERVO_MIN_PULSEWIDTH + (((SERVO_MAX_PULSEWIDTH - SERVO_MIN_PULSEWIDTH) * angle) / 180);

    // Convert pulse width to duty cycle
    uint32_t duty = (uint32_t)((float)pulseWidth * 16383.0f / 20000.0f);

    // Update duty cycle
    ledc_set_duty(PWM_MODE, PWM_CHANNEL, duty);
    ledc_update_duty(PWM_MODE, PWM_CHANNEL);
}
```

The `loop` function tested the full range of motion by moving the servo to angles 0°, 45°, 90°, 135°, and 180°, pausing 2 seconds between each move.

---

### Observations
- The servo motor successfully moved to the specified angles as expected.
- Duty cycle calculations matched the required pulse widths for standard servo motors, ensuring smooth operation.
- Minor debugging was required to correct initial configurations of the `SERVO_HIGH` pins and ensure proper timer initialization.

---

### Debugging and Improvements
1. **Timer Configuration Errors**:  
   Encountered a failure in `ledc_timer_config`. Resolved by ensuring correct timer frequency and clock settings.

2. **Servo Jitter**:  
   Observed slight jitter at certain angles, likely due to noise in the PWM signal. Planned to add capacitors for hardware noise reduction.

3. **Angle Limitation**:  
   Restricted the range to 0°–180° for compatibility with the servo’s specifications. Additional testing was done to ensure smooth operation at boundary values (0° and 180°).

---

### Future Steps
- Optimize signal stability by testing with hardware filtering.
- Implement feedback control using a potentiometer for precise angle measurements.