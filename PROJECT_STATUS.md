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
The initial lecture-oriented structure is established:

```text
00_intro        # Motivation and design philosophy
01_pid          # PID control fundamentals and simulation
02_fsm          # FSM-based supervisory control
03_phys_model   # Physical and V–I based models (nonlinear)
assets          # Figures and diagrams
```

Each directory contains its own `README.md` as a lecture anchor.

### Environment
- Python-based
- Minimal dependencies
- `requirements.txt` is created and committed

---

## 2. Design Decisions (Why it looks like this)

### Why control first
- Immediate feedback via simulation and plots
- Low entry cost for Udemy learners
- Control is treated as a **design tool**, not tuning

### Why physical models come later
- Physics and semiconductor concepts are introduced
  as **constraints and structure**, not prerequisites
- V–I characteristics are treated as control objects

### What is intentionally excluded (for now)
- Detailed semiconductor physics
- AI / LLM topics
- Excessive mathematics

These are postponed to keep the course **finish-able**.

---

## 3. Relationship to Samizo-AITL

- This repository is a **minimal, linear extraction**
- Samizo-AITL Portal remains the place for:
  - Full system architecture
  - Extended theory
  - Advanced and exploratory content

This repo prioritizes **execution and experience**.

---

## 4. Immediate Next Actions (When resuming)

### Priority 1
Create a **single clean working example**:

- Location: `01_pid/`
- File: `pid_sim.py`
- Features:
  - Step response
  - Clear variable naming
  - Simple plotting

Goal: Prove that the course “moves and responds”.

### Priority 2
Refine `00_intro/README.md`:

- Limit to 3 core messages:
  - Control is design
  - Physical models define structure
  - FSM is a supervisory layer

### Priority 3
Keep `03_phys_model/` lightweight:

- Nonlinearity
- Saturation
- V–I curve intuition
- No device equations yet

---

## 5. Slides (Marp) – Deferred Decision

- Marp-based HTML slides are **not required at this stage**
- Option to add later under `slides/`
- Decision to be revisited after core lectures stabilize

---

## 6. Guiding Principle Going Forward

> Do not optimize for completeness.  
> Optimize for **continuity and completion**.

This repository is successful if:
- A learner can run code
- See behavior
- Understand why structure matters

---

_End of current checkpoint._
