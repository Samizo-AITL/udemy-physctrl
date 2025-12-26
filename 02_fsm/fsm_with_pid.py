"""
fsm_with_pid.py
FSM selecting between different PID modes
"""

STATE_FAST = "fast_response"
STATE_SLOW = "stable_response"

state = STATE_FAST

# Example conditions
error = 0.2

# PID parameter sets
pid_fast = {"Kp": 2.0, "Ki": 1.0, "Kd": 0.1}
pid_slow = {"Kp": 0.5, "Ki": 0.2, "Kd": 0.05}

if state == STATE_FAST:
    pid = pid_fast
    if abs(error) < 0.5:
        state = STATE_SLOW

elif state == STATE_SLOW:
    pid = pid_slow
    if abs(error) > 1.0:
        state = STATE_FAST

print(f"Selected state: {state}")
print(f"Using PID gains: {pid}")
