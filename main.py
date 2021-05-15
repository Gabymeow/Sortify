import os
home = os.path.expanduser("~")
#print(home)
sdfolder = os.path.join(home, "fakeSD")
#print(sdfolder)

for file in os.listdir(sdfolder):
    if file.endswith(".NEF"):
        print(os.path.join("sdfolder", file))