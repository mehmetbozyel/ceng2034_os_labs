import binascii, os, time

beginning = time.time()
def seperatefiles(start,end,folder = "files/"):
    jpg = "ffd8ffe0"
    png = "89504e470d0a1a0a"
    mp3 = "494433"
    try:
        os.mkdir("jpg")
        os.mkdir("png")
        os.mkdir("mp3")
        os.mkdir("txt")
    except(FileExistsError):
        pass

    for i in range(start,end):
        file ="file" + str(i)
        with open(folder + file,"rb") as thisfile:
            header = thisfile.read(8)
            header = str(binascii.hexlify(header))[2:-1]
            if header.startswith(jpg):
                os.rename(folder + file,"jpg/" + file)
            elif header.startswith(png):
                os.rename(folder + file,"png/" + file)
            elif header.startswith(mp3):
                os.rename(folder + file,"mp3/" + file)
            else:
                os.rename(folder + file, "txt/" + file)

seperatefiles(1,150)
print("single threating took: " + str(time.time()- beginning) + " seconds")
