from typing import Protocol

class OpticalDisk(Protocol):
    def read(self):
        pass

    def write(self, data):
        pass


class CD():
    def __init__(self, data: str, storage_mb: int):
        self.data = data
        self.storage_mb = storage_mb

    def read(self):
        print(self.data,  "| Storage:", self.storage_mb, "mb")
    def write(self, data: str):
        self.data += data
        self.storage_mb -= len(data)

    
class DVD():
    def __init__(self, data:str, storage_gb:int):
        self.data = data
        self.storage_gb = storage_gb

    def read(self):
        print(self.data,  "| Storage:", self.storage_gb, "gb")

    def write(self, data:str):
        self.data += data
        self.storage_gb -= len(data) / 8

def main():
    data_cd = "Me: This is a cool CD"
    data_dvd = "Dr. Das: Yeah CDeezNutz"
    my_cd:OpticalDisk = CD(data_cd, 256)
    my_dvd:OpticalDisk = DVD(data_dvd, 12)

    my_cd.read()
    my_dvd.read()

    my_cd.write(". I think I haven autism")
    my_dvd.write(". Damn cuh")
 

    my_cd.read()
    my_dvd.read()

if __name__ == "__main__":
    main()

    

