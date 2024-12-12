### Notebook Entry Lab 11/25/24

## Objectives
- Checked and developed the mathematical model in PID.

## Progress

### Kinematics Model
The mathematical model in `kinematics.cpp` was derived based on the robot's omniwheel configuration, utilizing the velocity components in the $x$, $y$, and rotational ($\omega$) directions. The equations for the wheel linear speeds were:

$$
\text{wheelLinearSpeeds}[i] = V_x \cdot \sin(\theta_i) + V_y \cdot \cos(\theta_i) + \omega \cdot r
$$

Here:
- $V_x$ and $V_y$ are the linear velocities in the $x$ and $y$ directions.
- $\theta_i$ is the angle of the $i$-th wheel relative to the robot's frame.
- $\omega$ is the angular velocity of the robot.
- $r$ is the wheelbase radius.

The wheel linear speeds were converted to angular speeds using the relationship:

$$
\omega_{\text{wheel}} = \frac{\text{wheelLinearSpeeds}[i]}{\frac{d}{2}}
$$

Where:
- $d$ is the diameter of the wheel.

The angular speeds were then converted to RPM using the formula:

$$
\text{wheelSpeeds}[i] = \omega_{\text{wheel}} \cdot \frac{60}{2\pi}
$$

This ensured that the motor speed commands were proportional to the desired robot movement.

### PID Model
The PID model was implemented to control the motor speeds. The PID controller equation used in `pid_control.cpp` is:

$$
u(t) = K_p \cdot e(t) + K_i \cdot \int e(t) \, dt + K_d \cdot \frac{de(t)}{dt}
$$

Where:
- $u(t)$ is the control signal (PWM value).
- $e(t)$ is the error, calculated as:
  $$
  e(t) = \text{setpointRPM} - \text{actualRPM}
  $$
- $K_p$, $K_i$, and $K_d$ are the proportional, integral, and derivative gains, respectively.

The pseudocode for the PID implementation was as follows:
```cpp
int computePID(int motor, float setpointRPM, float actualRPM) {
    error = setpointRPM - actualRPM;
    integral += error;
    derivative = error - previousError;
    previousError = error;
    output = Kp * error + Ki * integral + Kd * derivative;
    return constrain(output, -MOTOR_MAX_SPEED, MOTOR_MAX_SPEED);
}
```

### Mathematical Breakdown
1. **Proportional Term ($K_p \cdot e(t)$):**
   - Provides immediate response proportional to the current error.
   - Adjusted $K_p$ to minimize overshoot during testing.

2. **Integral Term ($K_i \cdot \int e(t) \, dt$):**
   - Accounts for cumulative errors over time.
   - Avoided integral windup by clamping the output in the `computePID` function.

3. **Derivative Term ($K_d \cdot \frac{de(t)}{dt}$):**
   - Dampens the response by anticipating future errors.
   - Balanced $K_d$ to prevent excessive delay in motor responses.

This model ensured smooth and accurate motor control, aligning with the robot's motion requirements.