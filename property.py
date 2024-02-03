class Disk:
    def __init__(self, data:str, storage_gb:int):
        self._data = data
        self._storage_gb = storage_gb

    @property
    def data(self):
        return self._data
    
    @property
    def storage_gb(self):
        return self._storage_gb
    
    @storage_gb.setter
    def storage_gb(self, new_storage_gb):
        if new_storage_gb < 0:
            new_storage_gb = 0
        self._storage_gb = new_storage_gb

    @data.setter
    def data(self, new_data):
        self._data = new_data

def main():
    my_disk = Disk("Hola mi nombre es Johnny Sins", 69)
    print(my_disk.data, my_disk.storage_gb)
    my_disk.data = "Now mi nombre es Tu Madre"
    print(my_disk.data, my_disk.storage_gb)
    my_disk.storage_gb = 420
    print(my_disk.data, my_disk.storage_gb)


if __name__ == "__main__":
    main()

    
