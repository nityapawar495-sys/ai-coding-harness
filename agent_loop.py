import os
import sys
import time
from harness.state_machine import RubberDuckTestHarness
from tools.file_ops import read_file, write_file, list_repository_files
from tools.test_runner import run_tests
from prompts.system_prompts import RUBBER_DUCK_SYSTEM_PROMPT

# Toggle this to False when your API quota resets to use the live Gemini model with tools!
USE_MOCK = True

def run_agent(task_prompt: str):
    if USE_MOCK:
        print("=== INITIALIZING AI CODING AGENT (MOCK MODE) ===")
    else:
        print("=== INITIALIZING LIVE TOOL-ENABLED AI AGENT ===")
        from google import genai
        api_key = os.environ.get("GEMINI_API_KEY")
        if not api_key:
            print("❌ Error: GEMINI_API_KEY environment variable not found.")
            return
        client = genai.Client(api_key=api_key)
        model_name = "gemini-3.5-flash"
        my_tools = [read_file, write_file, list_repository_files, run_tests]

    harness = RubberDuckTestHarness()
    repo_files = list_repository_files()
    print(f"📁 Repository Files: {repo_files}")
    
    # 1. Phase 1: Diagnosis
    print(f"\n--- [PHASE 1: DIAGNOSIS] Analyzing task: '{task_prompt}' ---")
    
    if USE_MOCK:
        diagnosis_text = "To address the repository task, I will first list the repository files to confirm their structure, then read the contents of requirements.txt to understand the dependencies, and finally run the test suite to verify system health."
    else:
        diagnosis_prompt = f"""
{RUBBER_DUCK_SYSTEM_PROMPT}

REPOSITORY TASK:
{task_prompt}

Available files in repository: {repo_files}

Remember your instructions for Phase 1: Explain your hypothesis and plan in detail (at least 20 words). DO NOT call tools or write code blocks yet.
"""
        response = client.models.generate_content(
            model=model_name,
            contents=diagnosis_prompt,
            config={"tools": my_tools, "temperature": 0.2}
        )
        diagnosis_text = response.text or "Model responded with tool invocation."

    print(f"\n[Diagnosis Response]:\n{diagnosis_text}\n")
    
    success, message = harness.process_turn(diagnosis_text)
    print(f"Harness State Validation: Success={success} | Message={message}")
    
    if not success:
        print("❌ Harness blocked the model.")
        return

    # 2. Phase 2: Execution
    print("\n--- [PHASE 2: EXECUTION] ---")
    if USE_MOCK:
        print("🛠️ Model invoked tool: list_repository_files() -> Found 10 files")
        print("🛠️ Model invoked tool: read_file('requirements.txt') -> Read successfully")
        test_success, test_output = run_tests()
        print(f"Test Execution Success: {test_success}")
        print(f"Test Output:\n{test_output.strip()}")
    else:
        execution_prompt = f"""
{RUBBER_DUCK_SYSTEM_PROMPT}

Your previous diagnosis was accepted:
{diagnosis_text}

You are now in PHASE 2: EXECUTION. You have access to tools (`read_file`, `write_file`, `list_repository_files`, `run_tests`). Use them to complete the task.
"""
        exec_response = client.models.generate_content(
            model=model_name,
            contents=execution_prompt,
            config={"tools": my_tools, "temperature": 0.2}
        )
        if hasattr(exec_response, 'function_calls') and exec_response.function_calls:
            for call in exec_response.function_calls:
                print(f"🛠️ Model invoked tool: {call.name} with arguments {call.args}")
        else:
            print(exec_response.text)

    print("\n=== AGENT SESSION COMPLETE ===")

if __name__ == "__main__":
    task = "List repository files, read requirements.txt, and verify system health."
    run_agent(task)
