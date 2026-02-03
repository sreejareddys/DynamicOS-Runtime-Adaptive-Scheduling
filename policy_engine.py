class PolicyEngine:
    @staticmethod
    def score_fcfs(avg_wait, max_wait):
        return avg_wait + max_wait

    @staticmethod
    def score_rr(avg_wait):
        return avg_wait * 0.7
