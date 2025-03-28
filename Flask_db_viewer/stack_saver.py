from pathlib import Path

EXCLUDED_FILES = {"stack_saver.py"}

def root():
    return Path(__file__).parent

def content(dir, level=0):
    for item in dir.iterdir():
        if item.is_dir() and item.name != "__pycache__":
            print("    " * level + "|---" + item.name + "/")
            content(item, level + 1)

    for item in dir.iterdir():
        if item.is_file() and item.name not in EXCLUDED_FILES:
            print("    " * level + "|---" + item.name)

def hierarchy():
    dir = root()
    print(dir.name + "/")
    content(dir)

def format_contents(folder_path, exts):
    content = []
    for file in folder_path.rglob('*'):
        if file.is_file() and file.name not in EXCLUDED_FILES and any(file.name.endswith(ext) for ext in exts):
            try:
                with file.open('r', encoding='utf-8') as f:
                    content.append(f"Filename: {file.name} (Location: {file.parent.name})\n\n{f.read()}\n")
            except (UnicodeDecodeError, Exception) as e:
                content.append(f"Could not read {file.name}: {e}")

    return "\n".join(content)

if __name__ == "__main__":
    folder = root()
    exts = ['.html', '.css', '.js', '.py', '.txt', '.md']
    
    print("```\n")
    print(f"Folder Structure:\n")
    hierarchy()
    print(f"\nContents:\n")
    print(format_contents(folder, exts))
    print("\n```")