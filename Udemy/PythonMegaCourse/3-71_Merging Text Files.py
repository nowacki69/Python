from glob2 import glob
from datetime import datetime

filelist = glob("file[0-9].txt")

with open(datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f") + ".txt", 'w') as outfile:
    for afile in filelist:
        with open(afile, "r") as inputfile:
            outfile.write(inputfile.read() + '\n')
