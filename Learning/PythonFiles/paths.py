from pathlib import Path

path = Path("Learning/PythonFiles/Modules/__init__.py")

print(path.exists())
print(path.is_dir())
print(path.is_file())
print(path.name)
print(path.parent)
print(path.suffix)
print(path.absolute())
# path = path.with_name("file.txt")
path = path.with_suffix(".txt")
print(path.absolute())
