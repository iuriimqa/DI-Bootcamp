class Door:
    def __init__(self) -> None:
        self.is_opened = False

    def open(self):
        self.is_opened = True
    
    def close(self):
        self.is_opened = False


class BlockedDoor(Door):
    
    def open(self):
        func_name = open.__name__
        raise TypeError(f'{func_name}: Blocked Door cannot be opened!')

    def close(self):
        raise TypeError('Blocked Door cannot be closed!')
    

blocked = BlockedDoor()

try:
    blocked.open()
except TypeError as error:
    print(error.with_traceback())
    print('Someone is trying to open a Blocked Door!')
except KeyError: 
    print("Invalid Key!")
except ValueError: 
    print("Invalid Value!")
finally:
    print("RUNS ANYWAY")

