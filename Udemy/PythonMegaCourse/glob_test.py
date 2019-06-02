from glob2 import glob

def main ():
    files = glob("file[0-9].txt")
    for afile in files:
        print(afile)

if(__name__ == "__main__"):
    main()
