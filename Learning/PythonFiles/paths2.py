from pathlib import Path

# from ..exceptions import calculate_xFacypr

path = Path("Learning/PythonFiles/Modules")

print(path.exists())
# path.mkdir("Modules")
# path.rmdir()
# path.rename()

# for i in path.iterdir():
#     print(i)

fullpath = [p for p in path.iterdir() if p.is_dir()]

# print(fullpath)

# to search recursively as well 
pyFile = [p for p in path.rglob("*.py")]
# to search based on pattern only
pyFile = [p for p in path.glob("*.py")]
print(pyFile)