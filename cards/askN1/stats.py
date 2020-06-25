import glob

# get all .ankle files and sort them
ankles = []
for file in glob.glob("*.ankle"):
    num = int(file.split(".")[0])
    ankles.append({"index":num, "name":file})
ankles.sort(key=lambda x: x["index"])

class stats():
    def __init__(self):
        self.count = 0
    def display(self):
        print("Count: {}".format(self.count))

s = stats()
s.count = len(ankles)
s.display()