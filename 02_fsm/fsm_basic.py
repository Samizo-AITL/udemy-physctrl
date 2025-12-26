"""
fsm_basic.py
Minimal FSM example using conditional logic
"""

# Define states
STATE_STARTUP = "startup"
STATE_NORMAL  = "normal"
STATE_SAFE    = "safe"

# Initial state
state = STATE_STARTUP

# Example condition values (placeholders)
error = 5.0
threshold = 1.0
overcurrent = False

print(f"Initial state: {state}")

# FSM logic
if state == STATE_STARTUP:
    if error < threshold:
        state = STATE_NORMAL

elif state == STATE_NORMAL:
    if overcurrent:
        state = STATE_SAFE

elif state == STATE_SAFE:
    if not overcurrent:
        state = STATE_NORMAL

print(f"Next state: {state}")
