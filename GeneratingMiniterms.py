class MinitermGenerator:
    def __init__(self, predicates):
        self.predicates = predicates
    def generate_miniterms(self):
        miniterms = []
        n = len(self.predicates)
        for i in range(1 << n):  
            miniterm = []
            for j in range(n):
                if i & (1 << j): 
                    miniterm.append(self.predicates[j])
            if miniterm: 
                miniterms.append(miniterm)
        return miniterms

predicates = ["P1", "P2", "P3"]
generator = MinitermGenerator(predicates)
miniterms = generator.generate_miniterms()
print("Generated Miniterms:")
for miniterm in miniterms:
    print(" AND ".join(miniterm))
