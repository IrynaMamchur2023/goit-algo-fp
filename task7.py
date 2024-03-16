import random

def monte_carlo_simulation(num_trials):
    sums = [0] * 13  
    for _ in range(num_trials):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        total = dice1 + dice2
        sums[total] += 1  
    probabilities = [(i, count / num_trials * 100) for i, count in enumerate(sums) if i > 0]
    return probabilities

def print_table(probabilities):
    print("Сума\tІмовірність")
    for total, probability in probabilities:
        print(f"{total}\t{probability:.2f}% ({probability / 100 * 36}/36)")

def main():
    num_trials = 1000000
    probabilities = monte_carlo_simulation(num_trials)
    print_table(probabilities)

if __name__ == "__main__":
    main()