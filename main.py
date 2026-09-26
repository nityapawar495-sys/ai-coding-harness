<<<<<<< Updated upstream
from harness.state_machine import RubberDuckTestHarness

if __name__ == "__main__":
    harness = RubberDuckTestHarness()
    
    print("=== TEST 1: Model tries to cheat and write code immediately ===")
    bad_response = "def fix_bug(): return True"
    success, msg = harness.process_turn(bad_response)
    print(f"Result: Success={success} | Message: {msg}\n")
    
    print("=== TEST 2: Model follows the rules and diagnoses first ===")
    good_response = "I have analyzed the issue. The bug occurs because the input parameter is unvalidated, leading to a NoneType exception in utils.py. My plan is to add a type check before processing."
    success, msg = harness.process_turn(good_response)
    print(f"Result: Success={success} | Message: {msg}\n")
    
    print("=== TEST 3: Model now operates in execution mode ===")
    execution_response = "Running test suite to verify patch..."
    success, msg = harness.process_turn(execution_response)
    print(f"Result: Success={success} | Message: {msg}")
=======
import os
from harness.state_machine import RubberDuckTestHarness
from tools.file_ops import read_file, list_repository_files
from tools.test_runner import run_tests
from prompts.system_prompts import RUBBER_DUCK_SYSTEM_PROMPT

if __name__ == "__main__":
    print("=== INITIALIZING AI CODING HARNESS ===")
    
    # 1. Inspect prompt & repository structure
    print(f"\n[System Prompt Loaded]:\n{RUBBER_DUCK_SYSTEM_PROMPT[:100]}...\n")
    
    files = list_repository_files()
    print(f"📁 Discovered repository files: {files}")
    
    # 2. Initialize Harness State Machine
    harness = RubberDuckTestHarness()
    
    # 3. Simulate Phase 1: Improper Model Response (Trying to code prematurely)
    print("\n--- SIMULATION: Model tries to write code in Diagnosis phase ---")
    bad_response = "def fix_code(): return False"
    success, msg = harness.process_turn(bad_response)
    print(f"Result: Success={success} | Message: {msg}")
    
    # 4. Simulate Phase 1: Proper Diagnostic Response
    print("\n--- SIMULATION: Model provides proper diagnosis ---")
    good_response = "I have analyzed the module structure. The issue stems from an unhandled edge case in the input validation logic. My plan is to introduce a strict type check before execution."
    success, msg = harness.process_turn(good_response)
    print(f"Result: Success={success} | Message: {msg}")
    
    # 5. Simulate Phase 2: Execution & Test Verification
    if harness.phase == "EXECUTION":
        print("\n--- SIMULATION: Running Test Suite via Test Runner ---")
        test_success, test_output = run_tests()
        print(f"Test Execution Success: {test_success}")
        print(f"Test Output Summary:\n{test_output.strip()}")

    print("\n=== HARNESS SIMULATION COMPLETE ===")
>>>>>>> Stashed changes
