import random

class numar:
    def generate(self):
        return random.randint(1, 49)
    
lotto = numar()
print(lotto.generate())