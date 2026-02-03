class DecisionReport:
    def __init__(self):
        self.data = {}

    def add(self, key, value):
        self.data[key] = value

    def display(self):
        print("\n========== OS DECISION REPORT ==========")
        for key, value in self.data.items():
            print(f"{key:<20}: {value}")
        print("=======================================\n")
