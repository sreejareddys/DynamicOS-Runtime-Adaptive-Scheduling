from cpu.scheduler import CPUScheduler
from workload.process import Process
from core.metrics import Metrics
from core.threshold_manager import ThresholdManager
from core.policy_engine import PolicyEngine
from core.decision_report import DecisionReport


def main():
    print("=== OS Under Pressure Simulator ===\n")

   
    # 1. Create workload
    
    processes = [
        Process("P1", burst_time=5, arrival_time=0),
        Process("P2", burst_time=3, arrival_time=1),
        Process("P3", burst_time=8, arrival_time=2),
        Process("P4", burst_time=6, arrival_time=3),
    ]

    
    # 2. User-defined threshold
    
    user_threshold = float(input("Enter waiting time threshold: "))

    threshold_manager = ThresholdManager(user_threshold)

   
    # 3. Initialize scheduler & report
    
    scheduler = CPUScheduler(algorithm="FCFS")
    report = DecisionReport()

    report.add("Initial Scheduler", "FCFS")
    report.add("User Threshold", user_threshold)

    
    # 4. Run FCFS scheduling
    
    completed_processes = scheduler.schedule(processes)

    metrics = Metrics(completed_processes)
    avg_wait = metrics.average_waiting_time()
    max_wait = metrics.max_waiting_time()

    print(f"\nAverage Waiting Time: {avg_wait:.2f}")

    
    # 5. Update adaptive threshold
    adaptive_threshold = threshold_manager.update(avg_wait)

    report.add("Average Waiting Time", round(avg_wait, 2))
    report.add("Max Waiting Time", max_wait)
    report.add("Adaptive Threshold", round(adaptive_threshold, 2))

   
    # 6. Policy scoring
    
    score_fcfs = PolicyEngine.score_fcfs(avg_wait, max_wait)
    score_rr = PolicyEngine.score_rr(avg_wait)

    report.add("FCFS Score", round(score_fcfs, 2))
    report.add("RR Score", round(score_rr, 2))

    
    # 7. Decision making
    
    if score_rr < score_fcfs and avg_wait > adaptive_threshold:
        print("\n⚠ CPU under pressure!")
        print("Switching scheduler: FCFS → Round Robin")

        scheduler.algorithm = "RR"

        # Reset process state for RR
        for p in processes:
            p.remaining_time = p.burst_time
            p.waiting_time = 0

        scheduler.schedule(processes)

        report.add("Final Scheduler", "Round Robin")
        report.add("Decision Reason", "Lower composite scheduling cost")

    else:
        report.add("Final Scheduler", "FCFS")
        report.add("Decision Reason", "FCFS performance within acceptable limits")

    
    # 8. Display explainable report
   
    report.display()


if __name__ == "__main__":
    main()
