# Завдання 3
# Порівняти ефективність алгоритмів пошуку підрядка:
# Боєра-Мура, Кнута-Морріса-Пратта та Рабіна-Карпа на основі двох текстових файлів


import timeit

# Алгоритм Боєра-Мура
def boyer_moore(text, pattern):
    m = len(pattern)
    n = len(text)
    if m == 0:
        return 0
    last = {}
    for i in range(m):
        last[pattern[i]] = i
    i = m - 1
    k = m - 1
    while i < n:
        if text[i] == pattern[k]:
            if k == 0:
                return i
            else:
                i -= 1
                k -= 1
        else:
            j = last.get(text[i], -1)
            i += m - min(k, j + 1)
            k = m - 1
    return -1

# Алгоритм Кнута-Морріса-Пратта
def kmp_search(text, pattern):
    n = len(text)
    m = len(pattern)
    lps = [0] * m
    j = 0
    compute_lps_array(pattern, m, lps)
    i = 0
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == m:
            return i - j
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1

def compute_lps_array(pattern, m, lps):
    length = 0
    i = 1
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

# Алгоритм Рабіна-Карпа
def rabin_karp(text, pattern, q=101):
    d = 256
    m = len(pattern)
    n = len(text)
    p = 0
    t = 0
    h = 1
    for i in range(m - 1):
        h = (h * d) % q
    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q
    for i in range(n - m + 1):
        if p == t:
            for j in range(m):
                if text[i + j] != pattern[j]:
                    break
            j += 1
            if j == m:
                return i
        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
            if t < 0:
                t += q
    return -1

# Завантаження текстів
with open(r"C:\Users\WORK\Desktop\GoIT\Repository\Algorithms\Homework\goit-algo-hw-05\text1.txt", "r", encoding="utf-8") as file1:
    text1 = file1.read()

with open(r"C:\Users\WORK\Desktop\GoIT\Repository\Algorithms\Homework\goit-algo-hw-05\text2.txt", "r", encoding="utf-8") as file2:
    text2 = file2.read()

# Підрядки для тестування
existing_substring = "алгоритми"  # існуючий підрядок
non_existing_substring = "вигаданийпідрядок"  # неіснуючий підрядок

# Функції для вимірювання часу
def measure_time_boyer_moore(text, pattern):
    return boyer_moore(text, pattern)

def measure_time_kmp(text, pattern):
    return kmp_search(text, pattern)

def measure_time_rabin_karp(text, pattern):
    return rabin_karp(text, pattern)

# Вимірювання часу
time_boyer_moore_existing = timeit.timeit(lambda: measure_time_boyer_moore(text1, existing_substring), number=100)
time_kmp_existing = timeit.timeit(lambda: measure_time_kmp(text1, existing_substring), number=100)
time_rabin_karp_existing = timeit.timeit(lambda: measure_time_rabin_karp(text1, existing_substring), number=100)

time_boyer_moore_non_existing = timeit.timeit(lambda: measure_time_boyer_moore(text1, non_existing_substring), number=100)
time_kmp_non_existing = timeit.timeit(lambda: measure_time_kmp(text1, non_existing_substring), number=100)
time_rabin_karp_non_existing = timeit.timeit(lambda: measure_time_rabin_karp(text1, non_existing_substring), number=100)

# Виведення результатів
print(f"Boyer-Moore (existing): {time_boyer_moore_existing}")
print(f"KMP (existing): {time_kmp_existing}")
print(f"Rabin-Karp (existing): {time_rabin_karp_existing}")

print(f"Boyer-Moore (non-existing): {time_boyer_moore_non_existing}")
print(f"KMP (non-existing): {time_kmp_non_existing}")
print(f"Rabin-Karp (non-existing): {time_rabin_karp_non_existing}")
