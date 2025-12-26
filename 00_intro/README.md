# 00_intro – Why Control First

This chapter explains **why this course starts from control**,  
and how physical models and FSM fit into the overall design philosophy.

No equations.  
No implementation details.  
Only structure and intent.

---

## Message 1: Control is Design, Not Tuning

In this course, control is not treated as parameter tuning.

Control is a **design activity**:
- You decide what behavior is acceptable
- You decide how the system should respond over time
- You design structure before optimizing numbers

PID is used because it is:
- Simple
- Observable
- Immediately executable

Not because it is “easy”.

---

## Message 2: Physical Models Define Structure

Physical models are introduced **after control**, not before.

Why:
- Physics defines **constraints**
- Physics defines **nonlinearity**
- Physics defines **what cannot be controlled away**

V–I characteristics are treated as:
- Control objects
- Structural limitations
- Sources of mode changes

Not as device equations to be memorized.

---

## Message 3: FSM Is a Supervisory Layer

FSM is not an advanced control method.

FSM is a **decision layer**:
- Selecting modes
- Enabling or disabling controllers
- Handling saturation, limits, and abnormal conditions

PID controls *within* a mode.  
FSM decides *which* mode is active.

This separation is intentional.

---

## How to Use This Repository

1. Run code first
2. Observe behavior
3. Ask *why* structure matters
4. Add complexity only when necessary

Understanding comes from **execution**, not from reading.

---

## What This Course Is Not

At this stage, this course intentionally avoids:
- Detailed semiconductor physics
- AI / LLM-based control
- Heavy mathematical derivations

These topics belong to extended materials, not to the core learning path.

---

## Guiding Principle

> Do not optimize for completeness.  
> Optimize for **continuity and completion**.

If you can:
- Run the code
- See system behavior
- Understand why structure matters

Then this course is doing its job.

---

Next:  
➡ `01_pid/` – Run your first executable control example.

