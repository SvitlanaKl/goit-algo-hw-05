# Завдання 2

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    iterations = 0
    upper_bound = None

    while low <= high:
        iterations += 1
        mid = (high + low) // 2

        # якщо x більше за значення посередині списку, ігноруємо ліву половину
        if arr[mid] < x:
            low = mid + 1

        # якщо x менше за значення посередині списку, ігноруємо праву половину
        elif arr[mid] > x:
            high = mid - 1

        # інакше x присутній на позиції і повертаємо його
        else:
            return (iterations, arr[mid])
    
    # Якщо не знайшли точного значення, визначаємо upper_bound
    if low < len(arr):
        upper_bound = arr[low]
    else:
        upper_bound = None
    
    return (iterations, upper_bound)

# Тестуємо нашу функцію:
arr = [1.1, 2.5, 3.3, 4.8, 6.7, 8.0]
x = 5.0
result = binary_search(arr, x)
print(f"Iterations: {result[0]}, Upper bound: {result[1]}")

# функція binary_search повертає кортеж, де першим елементом є кількість ітерацій, необхідних для знаходження елемента,
# а другим — найменший елемент, який є більшим або рівним заданому значенню.
# Ми зберігаємо кількість ітерацій у змінній iterations та перевіряємо умови у циклі.
# Якщо ми не знаходимо точного збігу, то визначаємо верхню межу upper_bound на основі значення low після виходу з циклу.