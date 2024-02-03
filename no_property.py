class Disk:
    def __init__(self, data:str, storage_gb:int):
        self.set_data(data)
        self.set_storage_gb(storage_gb)

    def get_data(self):
        return self._data
    
    def get_storage_gb(self):
        return self._storage_gb

    def set_data(self, new_data):
        self._data = new_data

    def set_storage_gb(self, lol):
        if lol < 0:
            lol = 0
        self._storage_gb = lol
   

def main():
    my_disk = Disk("Hola mi nombre es Johnny Sins", 69)
    print(my_disk.get_data(), my_disk.get_storage_gb())
    my_disk.set_data("Now mi nombre is Tu Madre")
    print(my_disk.get_data(), my_disk.get_storage_gb())
    my_disk.set_storage_gb(420)
    print(my_disk.get_data(), my_disk.get_storage_gb())


if __name__ == "__main__":
    main()

    
