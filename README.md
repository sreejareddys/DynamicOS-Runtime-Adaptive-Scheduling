# DynamicOS-Runtime-Adaptive-Scheduling
 It is an adaptive operating system simulator that dynamically selects CPU scheduling policies based on runtime performance metrics, user-defined thresholds, and policy-based cost evaluation.

Key Features:
->Implements FCFS and Round Robin CPU scheduling
->Dynamic scheduler switching based on system performance
->Runtime metrics collection (average & maximum waiting time)
->User-configurable waiting-time threshold
->Self-learning adaptive threshold (blends user policy + observed behavior)

dynamic_os_simulator/
│
├── main.py
│
├── cpu/
│ ├── scheduler.py
│ ├── fcfs.py
│ └── round_robin.py
│
├── core/
│ ├── metrics.py
│ ├── threshold_manager.py
│ ├── policy_engine.py
│ └── decision_report.py
│
└── workload/process.py
