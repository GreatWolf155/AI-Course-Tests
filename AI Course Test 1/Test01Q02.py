unsorted = [[3, 1, 4, 1, 5], [7, 2, 10, 9], [42]]

def find_median(numbers: list) -> float:
    numbers.sort()
    if len(numbers) % 2 == 0:
        median = (numbers[len(numbers) // 2] + numbers[len(numbers) // 2 - 1]) / 2
    else:
        median = numbers[len(numbers) // 2]
    return float(median)

for num_list in unsorted:
    print(find_median(num_list))