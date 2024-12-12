# Notebook Entry Lab 12/02/24

## Objectives
- Finish Kinematics code + PID
- Debug and test kinematics
- Finish Communication with robot to Web App at demo level
- Create github repo for code

## Progress

#### **12/02 Evening**
- **Finalized Kinematics Code**  
  - Verified the mathematical model in `kinematics.cpp`.  
  - Tested conversions from linear to angular velocity using wheel parameters.  
  - Debugged issues such as incorrect wheelbase radius or wheel diameter values and resolved unit mismatches causing overflow errors in `wheelSpeeds` computation.  

- **Tuned PID Controllers**  
  - Used test scenarios with motors to adjust `Kp`, `Ki`, and `Kd` values.  
  - Fixed instability caused by improper proportional (oscillation) and derivative (sluggish response) tuning.  
  - Addressed integral windup for large errors.  

#### **12/03 Morning**
- **Tested Core Functions**  
  - Unit tested functions like `moveForward`, `rotateRobot`, `drawCircle`, and `drawSquare`.  
  - Debugged timing calculation issues in `esp_timer_get_time()` that caused skipped execution or unexpected delays.  
  - Resolved alignment drift in `rotateRobot` by calibrating encoder accuracy.  

- **Validated Web App Communication**  
  - Verified that the Flask app and ESP32 communicated correctly.  
  - Ensured the `sendIPToFlaskServer` function registered the ESP32 as expected.  
  - Tested the `/draw` POST endpoint to confirm proper JSON payload handling.  
  - Fixed deserialization errors in `web_server.cpp` and `app.py`.  

#### **12/03 Evening**
- **Performed Integration Testing**  
  - Integrated kinematics, motor control, and PID feedback loops with drawing commands like `circle`, `square`, and `triangle`.  
  - Resolved issues with PWM values exceeding limits (`MOTOR_MAX_SPEED`) due to PID outputs.  
  - Fixed motor misbehavior caused by incorrect encoder ISR implementations.  

- **Refined Web UI**  
  - Finalized login/logout workflows in `app.py` and enforced single-user session rules.  

#### **12/04 Early Morning**
- **Created GitHub Repository**  
  - Organized the repository with clear module folders:  
    - `/src` for C++ code (`motor_control`, `pid_control`, `kinematics`).  
    - `/web` for the Flask app.  
    - `/docs` for project documentation.  

- **Conducted Final System Testing**  
  - Tested commands issued through the web interface, ensuring the robot drew shapes as expected.  
  - Verified communication reliability over Wi-Fi.  
  - Addressed latency issues in HTTP requests and resolved occasional connection timeouts caused by weak Wi-Fi signals.  

### Additional Notes for Debugging
- **Hardware-Specific Issues**  
  - Resolved encoder ISR bounce by implementing software debouncing.  
  - Verified motor driver wiring and ensured proper STDBY pin configuration.  

- **Communication Issues**  
  - Used debug logs on the ESP32 to trace packet failures and addressed connection inconsistencies.  

- **Logging and Monitoring**  
  - Implemented verbose logging for PID values, calculated wheel speeds, and HTTP responses to streamline troubleshooting.  


### Issues:
Kinematics for PID on front 2 wheels is correct; Fiddling with the connections on the back motor shows that the issue lies behind the blue/white lines connecting to the encoder, meaning encoder feedback does not work correctly. We verified this on the morning of 12/04.