class Test:
    def __init__(self, fin):
        self.reqi_fin = fin

    def run(self):
        result = self.reqi_fin.get_current_balance()
        print(result)