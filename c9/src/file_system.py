import os.path

path = os.path.abspath(
    os.sep.join(
        ["", "Users", "dusty", "subdir", "subsubdir", "file.ext"]
    )
)
print(path)
