class Task1B:
    def __init__(self):
        self.x = 1


class Task1A(Task1B):
    def __init__(self):
        super().__init__()
        self.x = 2


class Task1D:
    def __init__(self):
        self.x = 3


class Task1C(Task1B, Task1D):
    def __init__(self):
        super().__init__()


class Task1E(Task1D):
    def __init__(self):
        super().__init__()
