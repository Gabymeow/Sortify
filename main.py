import os
os.path.join()
path = '~/fakeSD'
for file in os.listdir("path"):
    if file.endswith(".nef"):
        print(os.path.join("path", file))