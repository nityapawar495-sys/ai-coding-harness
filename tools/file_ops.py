<<<<<<< Updated upstream
import os

def read_file(file_path: str) -> str:
    """
    Safely reads and returns the contents of a given file path.
    """
    try:
        if not os.path.exists(file_path):
            return f"Error: File '{file_path}' does not exist."
            
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        return content
    except Exception as e:
        return f"Error reading file {file_path}: {str(e)}"

def list_repository_files(base_dir: str = ".") -> list:
    """
    Recursively lists all relevant source files in the repository,
    skipping hidden folders like .git or __pycache__.
    """
    code_files = []
    for root, dirs, files in os.walk(base_dir):
        # Exclude hidden directories
        dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ['venv', 'env', 'harness.egg-info']]
        
        for file in files:
            # Skip hidden files or compiled pyc files
            if not file.startswith('.') and not file.endswith('.pyc'):
                code_files.append(os.path.join(root, file))
                
    return code_files

if __name__ == "__main__":
    print("=== Testing File Ops Tool ===")
    
    # Test listing repository files
    files = list_repository_files()
    print(f"Discovered repository files: {files}")
    
    # Test reading main.py
    if "main.py" in files or os.path.exists("main.py"):
        content = read_file("main.py")
        print(f"\nSuccessfully read main.py (first 60 chars): {content[:60]}...")
=======
import os

def read_file(file_path: str) -> str:
    try:
        if not os.path.exists(file_path):
            return f"Error: File '{file_path}' does not exist."
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        return f"Error reading file {file_path}: {str(e)}"

def write_file(file_path: str, content: str) -> str:
    """
    Safely writes content to a given file path. Creates intermediate directories if needed.
    Returns a success message or an error string.
    """
    try:
        directory = os.path.dirname(file_path)
        if directory and not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)
            
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        return f"Successfully wrote to {file_path}"
    except Exception as e:
        return f"Error writing to file {file_path}: {str(e)}"

def list_repository_files(base_dir: str = ".") -> list:
    code_files = []
    for root, dirs, files in os.walk(base_dir):
        dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ['venv', 'env', 'harness.egg-info']]
        for file in files:
            if not file.startswith('.') and not file.endswith('.pyc'):
                code_files.append(os.path.join(root, file))
    return code_files

if __name__ == "__main__":
    print("=== Testing File Ops Tool (Read, Write, List) ===")
    
    # Test writing a temporary scratch file
    test_path = "tools/scratchpad.txt"
    write_result = write_file(test_path, "Hello from the AI coding harness write tool!")
    print(write_result)
    
    # Test reading it back
    if os.path.exists(test_path):
        content = read_file(test_path)
        print(f"Successfully read back: {content}")
        # Clean up test file
        os.remove(test_path)
    
    files = list_repository_files()
    print(f"Discovered repository files count: {len(files)}")
>>>>>>> Stashed changes
