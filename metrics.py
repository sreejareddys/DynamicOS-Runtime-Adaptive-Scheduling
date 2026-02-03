
class Metrics:
    def __init__(self, processes):
        self.processes = processes

    def record(self, processes):
        self.waiting_times = [p.waiting_time for p in processes]

    def average_waiting_time(self):
        total_wait = sum(p.waiting_time for p in self.processes)
        return total_wait / len(self.processes)

    
    def max_waiting_time(self):
        return max(p.waiting_time for p in self.processes)

    def throughput(self, total_time):
        return len(self.processes) / total_time



    


