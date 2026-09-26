<<<<<<< Updated upstream
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
                return False, "Harness Block: Do not write code yet. Explain your hypothesis first."
            else:
                print("✅ [Harness Success]: Valid diagnosis detected. Unlocking execution tools.")
                self.phase = "EXECUTION"
                self.journal.append(model_output)
                return True, "Diagnosis accepted. You may now modify code."
                
        elif self.phase == "EXECUTION":
            print("⚙️ [Harness Execution]: Processing code change or test command.")
            return True, "Execution step handled."
=======
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
>>>>>>> Stashed changes
