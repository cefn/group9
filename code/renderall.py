#!/usr/bin/python3
import os,subprocess

style="monokai"

names = []
for name in os.listdir("."):
    if name.endswith(".py"):
        names.append(name)
        prefix = "".join(name.split(".")[:-1])
        subprocess.call(f"pygmentize -O full,style={style} -o {prefix}.svg {prefix}.py", shell="True")

print(f"Processed {','.join(names)}")
