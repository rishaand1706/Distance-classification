import json
import os
import sys

def extract_file_references(notebook_path):
    """Extracts image and file references from a Jupyter Notebook."""
    if not os.path.exists(notebook_path):
        print(f"Error: File '{notebook_path}' not found.")
        sys.exit(1)

    with open(notebook_path, 'r', encoding='utf-8') as f:
        notebook = json.load(f)

    file_references = []

    # Extract references from markdown and code cells
    for cell in notebook.get("cells", []):
        if cell["cell_type"] == "markdown":
            for line in cell["source"]:
                if "![" in line and "](" in line:
                    file_path = line.split("](")[-1].strip(")\n ")
                    file_references.append(file_path)
        elif cell["cell_type"] == "code":
            for line in cell["source"]:
                if "open(" in line or "read_csv(" in line:
                    parts = line.split("(")[-1].split(")")[0].replace('"', '').replace("'", "")
                    if parts.endswith((".png", ".jpg", ".jpeg", ".csv", ".txt", ".json")):
                        file_references.append(parts)

    return file_references

def check_files_exist(files):
    """Checks if the extracted files exist in the directory."""
    missing_files = []
    for file in files:
        if not os.path.exists(file):
            missing_files.append(file)
    
    if missing_files:
        print("Missing Files:")
        for file in missing_files:
            print(f"- {file}")
    else:
        print("All files are present.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python check_notebook_files.py <notebook.ipynb>")
        sys.exit(1)

    notebook_path = sys.argv[1]
    file_references = extract_file_references(notebook_path)
    
    if not file_references:
        print("No images or files found in the notebook.")
    else:
        print(f"Found {len(file_references)} file references. Checking their existence...")
        check_files_exist(file_references)
