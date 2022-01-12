class Starter:
    def __init__(self, fn, *args, **kwargs):
        self.fn = fn
        self.args = args
        self.kwargs = kwargs

    def start(self):
        return self.fn(*self.args, **self.kwargs)
