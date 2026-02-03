from cpu.fcfs import fcfs_schedule
from cpu.round_robin import round_robin_schedule


class CPUScheduler:
    def __init__(self, algorithm="FCFS"):
        self.algorithm = algorithm

    def schedule(self, processes):
        if self.algorithm == "FCFS":
            return fcfs_schedule(processes)

        elif self.algorithm == "RR":
            return round_robin_schedule(processes)

        else:
            raise ValueError("Unknown scheduling algorithm")
