
population = {}

total = 0

with open("population.txt") as file:
    for line in file:
        words = line.split()
        dep, pop = words[0], words[-1]

        if len(dep) == 1:
            idep = int(dep)
            dep = f"{idep:02d}"

        pop = int(pop)
        population[dep] = pop
        total += pop

population["France"] = total
