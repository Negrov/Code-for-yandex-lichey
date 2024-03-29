class BigBell:

    def __init__(self):
        self.count = 1

    def sound(self) -> None:
        if self.count == 1:
            print("ding")
        else:
            print("dong")
        self.count *= -1
        return
