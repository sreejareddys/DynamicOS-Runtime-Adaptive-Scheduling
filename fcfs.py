def fcfs_schedule(processes):
    print("\n--- DEBUG: PROCESSES RECEIVED BY FCFS ---")
    for p in processes:
        print(p.pid, "arrival =", p.arrival_time, "burst =", p.burst_time)

    time = 0
    completed = []

    processes = sorted(processes, key=lambda p: p.arrival_time)

    print("\n--- DEBUG: AFTER SORTING BY ARRIVAL ---")
    for p in processes:
        print(p.pid, "arrival =", p.arrival_time)

    for process in processes:
        if time >= process.arrival_time:
            process.waiting_time = time - process.arrival_time
        else:
            process.waiting_time = 0
            time = process.arrival_time

        time += process.burst_time
        completed.append(process)

    return completed
