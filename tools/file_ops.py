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
