genome = input().lower()
print((int(genome.count('g')) + int(genome.count('c'))) / len(genome) * 100)