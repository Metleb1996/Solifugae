import os

def writer(text, name):
    if not os.path.exists(name):
        with open(name, "w") as f:
            f.write(text)
        return True
    return False
