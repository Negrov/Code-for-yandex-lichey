class Button:

    def __init__(self):
        self.count = 0

    def click(self) -> None:
        self.count += 1
        return

    def click_count(self) -> int:
        return self.count

    def reset(self) -> None:
        self.count = 0
        return
