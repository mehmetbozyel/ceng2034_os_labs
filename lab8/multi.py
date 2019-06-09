import binascii, os, time
import threading

# 0.004537820816040039

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



t1 = threading.Thread(target=seperatefiles, args=(1, 50))
t2 = threading.Thread(target=seperatefiles, args=(50, 100))
t3 = threading.Thread(target=seperatefiles, args=(100, 150))

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()


print("multithreating took: " + str(time.time()- beginning) + " seconds")
