---
title: Project Status - udemy-physctrl
author: Samizo-AITL
---

# udemy-physctrl – Project Status

This document summarizes the **current state**, **design decisions**, and **next steps**
for the Udemy course repository `udemy-physctrl`.

It is intended as a **pause / resume anchor** for the author.

---

## 1. Current Status (Checkpoint)

### Repository
- Repository name: **udemy-physctrl**
- Purpose: Udemy course companion repository
- Scope: Physical-model-based control design (PID / FSM)

### Structure
The lecture-oriented structure is established and validated:

```text
00_intro        # Motivation and design philosophy
01_pid          # PID control fundamentals and simulation
02_fsm          # FSM-based supervisory control
03_phys_model   # Physical and V–I based models (nonlinear)
assets          # Figures and diagrams
```

Each directory contains its own `README.md` as a lecture anchor.

---

### Execution Status (Important)

- ✅ **01_pid/pid_sim.py implemented**
- ✅ Script executes successfully and produces a step response plot
- ✅ Minimal PID example confirmed to “move and respond”
- ✅ `01_pid/README.md` updated as an execution guide
- ✅ Changes committed and pushed to GitHub (`main`)

The repository is now **executable, reproducible, and learner-ready**.

---

### Environment
- Python-based
- Minimal dependencies
- `requirements.txt` is created and committed
- Verified on a clean local Python environment

---

## 2. Design Decisions (Why it looks like this)

### Why control comes first
- Immediate feedback via simulation and plots
- Low entry cost for Udemy learners
- Control is treated as a **design tool**, not parameter tuning

### Why physical models come later
- Physics and semiconductor concepts are introduced
  as **constraints and structure**, not prerequisites
- V–I characteristics are treated as control objects
- Nonlinearity is presented conceptually before equations

### What is intentionally excluded (for now)
- Detailed semiconductor device physics
- AI / LLM topics
- Heavy mathematical formalism

These are postponed to keep the course **finish-able and executable**.

---

## 3. Relationship to Samizo-AITL

- This repository is a **minimal, linear extraction**
- Samizo-AITL Portal remains the place for:
  - Full system architecture
  - Extended theory
  - Advanced and exploratory content

This repo prioritizes **execution, intuition, and continuity**.

---

## 4. Completed Actions (Milestones Reached)

### ✔ Priority 1 — Completed
A **single clean working example** has been created:

- Location: `01_pid/`
- File: `pid_sim.py`
- Features:
  - Step response
  - Clear variable naming
  - Simple plotting

Result:
> The course demonstrably “moves and responds”.

This serves as the **baseline executable reference** for the entire course.

---

## 5. Immediate Next Actions (When resuming)

### Priority 1 — Stabilize the Baseline
- Treat `01_pid/pid_sim.py` as a **frozen reference**
- Do not modify it directly
- Add variants as separate files if needed:
  - Saturation
  - Faster response
  - Noise / disturbance

---

### Priority 2 — Refine `00_intro/README.md`
Limit to **three core messages** only:

- Control is a design activity
- Physical models define structure and constraints
- FSM acts as a supervisory decision layer

No equations. No implementation details.

---

### Priority 3 — Develop `02_fsm/`
- Introduce FSM as a **mode-selection layer**
- Start from simple conditional logic
- Emphasize *why* switching is needed, not how complex it is

---

### Priority 4 — Keep `03_phys_model/` lightweight
- Nonlinearity
- Saturation
- V–I curve intuition
- No device equations at this stage

---

## 6. Slides (Marp) – Deferred Decision

- Marp-based HTML slides are **not required at this stage**
- Option to add later under `slides/`
- Decision to be revisited after lecture flow stabilizes

---

## 7. Guiding Principle Going Forward

> Do not optimize for completeness.  
> Optimize for **continuity and completion**.

This repository is successful if:
- A learner can run code
- See behavior
- Understand why structure matters

---

_End of current checkpoint._
