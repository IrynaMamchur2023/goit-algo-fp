def greedy_algorithm(items, budget):
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)

    selected_items = []
    total_calories = 0
    total_cost = 0

    for item, properties in sorted_items:
        if total_cost + properties['cost'] <= budget:
            total_cost += properties['cost']
            total_calories += properties['calories']
            selected_items.append(item)

    return selected_items, total_calories


def dynamic_programming(items, budget):
    n = len(items)
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, budget + 1):
            cost = items[i - 1][1]["cost"]  
            calories = items[i - 1][1]["calories"] 
            if cost <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - cost] + calories)
            else:
                dp[i][j] = dp[i - 1][j]

    result = []
    i, j = n, budget
    while i > 0 and j > 0:
        if dp[i][j] != dp[i - 1][j]:
            result.append(items[i - 1][0])  
            j -= items[i - 1][1]["cost"]  
        i -= 1

    return result, dp[n][budget]


items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 100

selected_items, total_calories_greedy = greedy_algorithm(items, budget)
print("Greedy Algorithm:")
print("Selected items:", selected_items)
print("Total calories:", total_calories_greedy)

selected_items_dp, total_calories_dp = dynamic_programming(list(items.items()), budget)
print("\nDynamic Programming:")
print("Selected items:", selected_items_dp)
print("Total calories:", total_calories_dp)