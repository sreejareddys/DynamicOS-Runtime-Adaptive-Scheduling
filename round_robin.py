from collections import deque

def round_robin_schedule(processes, quantum=2):
    time = 0
    queue = deque()
    completed = []

    processes = sorted(processes, key=lambda p: p.arrival_time)
    i = 0

    while queue or i < len(processes):
        while i < len(processes) and processes[i].arrival_time <= time:
            queue.append(processes[i])
            i += 1

        if not queue:
            time += 1
            continue

        process = queue.popleft()

        exec_time = min(quantum, process.remaining_time)
        process.remaining_time -= exec_time
        time += exec_time

        while i < len(processes) and processes[i].arrival_time <= time:
            queue.append(processes[i])
            i += 1

        if process.remaining_time > 0:
            queue.append(process)
        else:
            process.waiting_time = time - process.arrival_time - process.burst_time
            completed.append(process)

    return completed
