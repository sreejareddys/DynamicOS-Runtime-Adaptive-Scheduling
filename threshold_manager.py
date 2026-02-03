class ThresholdManager:
    def __init__(self, user_threshold, alpha=0.6):
        self.user_threshold = user_threshold
        self.alpha = alpha
        self.current_threshold = user_threshold

    def update(self, observed_avg_wait):
        self.current_threshold = (
            self.alpha * self.user_threshold +
            (1 - self.alpha) * observed_avg_wait
        )
        return self.current_threshold
