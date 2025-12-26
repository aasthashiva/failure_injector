class Metrics:
    def __init__(self):
        self.total_calls = 0
        self.successes = 0
        self.timeouts = 0
        self.exceptions = 0
        self.slowdowns = 0

    def snapshot(self):
        return {
            "total_calls": self.total_calls,
            "successes": self.successes,
            "timeouts": self.timeouts,
            "exceptions": self.exceptions,
            "slowdowns": self.slowdowns,
        }


metrics = Metrics()

