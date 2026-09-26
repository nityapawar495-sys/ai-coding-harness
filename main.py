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
