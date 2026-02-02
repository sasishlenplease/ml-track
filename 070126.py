def two_sum(nums, target):
    prev_map = {}
    for i, n in enumerate(nums):
        diff = target - n
        if diff in prev_map:
            return [prev_map[diff], i]
        prev_map[n] = i
    return ['соси'] # на случай, если решение не найдено

# Проверка
if __name__ == "__main__":
    # Тест 1
    print(f"Тест 1 (Ожидаем [0, 1]): {two_sum([2, 7, 11, 15], 9)}")
    # Тест 2
    print(f"Тест 2 (Ожидаем [1, 2]): {two_sum([3, 4], 6)}")