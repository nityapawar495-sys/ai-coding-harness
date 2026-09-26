# AI Coding Harness: Rubber Duck Debugger

An autonomous text-only coding agent harness built for the LCC DevClub AI Coding Harness Hackathon.

## 🎯 The Core Problem
Standard coding agents immediately attempt to patch code and run tests blindly upon receiving an issue. This often leads to infinite looping, excessive token consumption, and hallucinated fixes.

## 🛠️ Our Solution: The Rubber Duck Diagnostic State Machine
Our harness enforces a structured, multi-phase engineering workflow:
1. **The Diagnosis Phase (Thinking First):** 
   - The model is restricted to reading tools and a diagnostic prompt.
   - It is explicitly blocked from writing code or executing terminal commands until it outputs a detailed, logical hypothesis of the bug.
2. **The Execution Phase (Verified Action):** 
   - Once the harness validates the text-based diagnosis, code-editing and test-runner tools are dynamically unlocked.
   - Test tracebacks are parsed and fed back iteratively if failures occur.

## 📐 Architecture & Components
- **State Manager (`state_machine.py`):** Controls tool permissions based on the active phase.
- **Prompt Interceptor (`interceptor.py`):** Validates model outputs before executing tools.
- **Tool Suite (`tools/`):** Text-based repository navigators and test executors.

## 🚀 Evaluation & Efficiency Focus
- Minimizes redundant token waste by forcing structured thought over brute-force trial and error.
- Ensures reliable failure recovery through rigorous traceback aggregation.
