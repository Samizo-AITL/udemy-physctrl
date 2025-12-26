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
The lecture-oriented structure is **fully established and validated**:

```text
00_intro        # Motivation and design philosophy
01_pid          # PID control fundamentals and simulation
02_fsm          # FSM-based supervisory control
03_phys_model   # Physical and V–I based models (nonlinear)
assets          # Figures and diagrams
```

Each directory contains:
- `README.md` : learner-facing lecture anchor  
- `SCRIPT_*.md` : instructor-facing Udemy recording script  

---

### Execution Status (Important)

- ✅ **01_pid/pid_sim.py implemented and frozen**
- ✅ Script executes successfully and produces a step response plot
- ✅ Minimal PID example confirmed to “move and respond”
- ✅ `02_fsm/` implemented with minimal FSM examples
- ✅ `03_phys_model/` implemented with nonlinear, saturation, and V–I intuition models
- ✅ All scripts execute correctly and demonstrate intended behavior
- ✅ All changes committed and pushed to GitHub (`main`)

The repository is now **executable, reproducible, and recording-ready**.

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
- Control is treated as a **design activity**, not parameter tuning

### Why FSM is introduced next
- PID is not always sufficient in all operating conditions
- FSM is positioned as a **supervisory decision layer**
- Focus is on *why switching is needed*, not on formal FSM theory

### Why physical models come last
- Physics and semiconductor concepts are introduced
  as **constraints and structure**, not prerequisites
- V–I characteristics are treated as control objects
- Nonlinearity and saturation are presented **without equations**

### What is intentionally excluded
- Detailed semiconductor device physics
- AI / LLM topics
- Heavy mathematical formalism
- Complex control theory extensions

These are excluded to keep the course **finish-able, executable, and intuitive**.

---

## 3. Relationship to Samizo-AITL

- This repository is a **minimal, linear extraction**
- Samizo-AITL Portal remains the place for:
  - Full system architecture
  - Extended theory
  - Advanced and exploratory content

This repo prioritizes **execution, intuition, and continuity** over completeness.

---

## 4. Completed Actions (Milestones Reached)

### ✔ Priority 1 — Completed
A **single clean working baseline** has been established:

- Location: `01_pid/`
- File: `pid_sim.py`
- Status: **Frozen reference**
- Role: Baseline executable for the entire course

Result:
> The course demonstrably “moves and responds”.

---

### ✔ Priority 2 — Completed
FSM layer implemented and validated:

- Location: `02_fsm/`
- Focus: Mode selection and supervisory logic
- Implementation:
  - `fsm_basic.py`
  - `fsm_with_pid.py`
- Emphasis: Role separation (PID vs FSM)

---

### ✔ Priority 3 — Completed
Physical model intuition layer implemented:

- Location: `03_phys_model/`
- Topics:
  - Nonlinearity
  - Saturation
  - V–I characteristics
- Implementation:
  - `nonlinear_element.py`
  - `saturation_model.py`
  - `vi_curve_demo.py`

FSM necessity is fully justified by physical constraints.

---

### ✔ Priority 4 — Completed
Udemy recording scripts prepared:

- `SCRIPT_00_intro.md`
- `SCRIPT_01_pid.md`
- `SCRIPT_02_fsm.md`
- `SCRIPT_03_phys_model.md`

Each script is:
- Recording-ready
- README-aligned
- Designed for natural spoken delivery

---

## 5. Current Next Actions (Optional)

### Priority 1 — Udemy Recording
- Use GitHub repository as **visual map**
- Perform execution and explanation locally (VS Code)
- Scripts act as instructor teleprompter

### Priority 2 — Optional Refinement
- Minor wording adjustments in README or scripts
- No technical expansion recommended

---

## 6. Slides (Marp) – Deferred by Design

- Marp-based HTML slides are **intentionally omitted**
- Repository-first, execution-first approach is prioritized
- Slides may be added later **only if needed**

---

## 7. Guiding Principle Going Forward

> Do not optimize for completeness.  
> Optimize for **continuity and completion**.

This repository is successful if:
- A learner can run code
- See behavior
- Understand why structure matters

---

_End of current checkpoint (Updated)._  
