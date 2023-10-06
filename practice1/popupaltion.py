"""
This data represents the population growth of a small town over the years. Load the data into your program, and print a bar graph demonstrating the population for each year, with one asterisk representing 100 people.

"""
def load_data():
    population = {}
    with open("practice1\\population.txt") as file:
        for line in file:
            year, pop = line.split()
            population[year] = pop

    return population


def print_population():
    population = load_data()
    for p, a in population.items():
        a = int(a)
        ast = "*" * (a//100)
        print(f"{p}: {ast}")



print_population()