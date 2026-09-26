<<<<<<< Updated upstream
import subprocess

def run_tests(test_path: str = ".") -> tuple:
    """
    Executes tests using pytest via subprocess, capturing output and return codes.
    Returns a tuple of (success: bool, output: str).
    """
    try:
        # Run pytest command securely
        result = subprocess.run(
            ["pytest", test_path],
            capture_output=True,
            text=True,
            timeout=30
        )
        
        output = result.stdout + "\n" + result.stderr
        success = (result.returncode == 0)
        return success, output

    except FileNotFoundError:
        return False, "Error: 'pytest' command not found in the environment."
    except subprocess.TimeoutExpired:
        return False, "Error: Test execution timed out after 30 seconds."
    except Exception as e:
        return False, f"Error running test runner: {str(e)}"

if __name__ == "__main__":
    print("=== Testing Test Runner Tool ===")
    success, output = run_tests()
    print(f"Test Execution Success: {success}")
    print(f"Test Output:\n{output}")
=======
import subprocess

def run_tests(test_path: str = ".") -> tuple:
    """
    Executes tests using pytest via subprocess, capturing output and return codes.
    Returns a tuple of (success: bool, output: str).
    """
    try:
        # Run pytest command securely
        result = subprocess.run(
            ["pytest", test_path],
            capture_output=True,
            text=True,
            timeout=30
        )
        
        output = result.stdout + "\n" + result.stderr
        success = (result.returncode == 0)
        return success, output

    except FileNotFoundError:
        return False, "Error: 'pytest' command not found in the environment."
    except subprocess.TimeoutExpired:
        return False, "Error: Test execution timed out after 30 seconds."
    except Exception as e:
        return False, f"Error running test runner: {str(e)}"

if __name__ == "__main__":
    print("=== Testing Test Runner Tool ===")
    success, output = run_tests()
    print(f"Test Execution Success: {success}")
    print(f"Test Output:\n{output}")
>>>>>>> Stashed changes
