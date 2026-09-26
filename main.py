class RubberDuckTestHarness:
    def __init__(self):
        # State machine starts in the thinking/diagnostic phase
        self.phase = "DIAGNOSIS"
        self.journal = []

    def process_turn(self, model_output: str):
        print(f"\n[Incoming Model Output]: {model_output[:60]}...")
        
        if self.phase == "DIAGNOSIS":
            # Check if model is trying to skip to code execution too early
            if "def " in model_output or "import " in model_output or len(model_output.split()) < 20:
                print("❌ [Harness Interception]: Model tried to write code or gave insufficient explanation.")
                return False, "Harness Block: You are in Diagnostic Mode. Do not write code yet. Explain your hypothesis first."
            else:
                print("✅ [Harness Success]: Valid diagnosis detected. Unlocking execution tools.")
                self.phase = "EXECUTION"
                self.journal.append(model_output)
                return True, "Diagnosis accepted. You may now modify code."
                
        elif self.phase == "EXECUTION":
            print("⚙️ [Harness Execution]: Processing code change or test command.")
            return True, "Execution step handled."

# --- Local Test Simulation ---
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
