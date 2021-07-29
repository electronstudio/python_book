import os

for filename in os.listdir("."):
    if filename.endswith(".md"):
        # print(os.path.join(directory, filename))
        base = os.path.splitext(filename)[0]
        os.system(f"pandoc {filename} -o {base}.rst")
        continue
    else:
        continue
