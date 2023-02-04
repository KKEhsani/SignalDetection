import scipy

class SignalDetection:
    def __init__(self, hits, misses, false_alarms, correct_rejections):
        self.hits = hits
        self.misses = misses
        self.false_alarms = false_alarms
        self.correct_rejections = correct_rejections
        self.H = hits / (hits + misses)
        self.FA = false_alarms / (false_alarms + correct_rejections)
        self.ZH = scipy.special.ndtri(self.H)
        self.ZFA = scipy.special.ndtri(self.FA)

    def d_prime(self):
        d_prime = self.ZH - self.ZFA
        return d_prime

    def criterion(self):
        criterion = -0.5 * (self.ZH + self.ZFA)
        return criterion
