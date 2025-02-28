
# Порівняння ефективності алгоритмів пошуку підрядка

## Опис
Цей документ містить порівняння ефективності трьох алгоритмів пошуку підрядка: Боєра-Мура, Кнута-Морріса-Пратта та Рабіна-Карпа. Тестування проводилось на основі двох текстових файлів ("text1.txt" та "text2.txt"). Для кожного алгоритму вимірювався час виконання для двох видів підрядків: одного, що дійсно існує в тексті, та іншого — вигаданого.

## Результати

### text1.txt

#### Існуючий підрядок ("алгоритми")
- **Boyer-Moore**: 0.002428 секунд
- **KMP**: 0.011855 секунд
- **Rabin-Karp**: 0.014893 секунд

#### Неіснуючий підрядок ("вигаданийпідрядок")
- **Boyer-Moore**: 0.062694 секунд
- **KMP**: 0.630514 секунд
- **Rabin-Karp**: 0.856700 секунд

### text2.txt

#### Існуючий підрядок ("алгоритми")
- **Boyer-Moore**: 0.167061 секунд
- **KMP**: 0.850132 секунд
- **Rabin-Karp**: 1.121248 секунд

#### Неіснуючий підрядок ("вигаданийпідрядок")
- **Boyer-Moore**: 0.100818 секунд
- **KMP**: 0.788861 секунд
- **Rabin-Karp**: 1.061358 секунд

## Висновки
- Найшвидший алгоритм для "text1.txt" (існуючий підрядок): Boyer-Moore (0.002428 секунд)
- Найшвидший алгоритм для "text1.txt" (неіснуючий підрядок): Boyer-Moore (0.062694 секунд)
- Найшвидший алгоритм для "text2.txt" (існуючий підрядок): Boyer-Moore (0.167061 секунд)
- Найшвидший алгоритм для "text2.txt" (неіснуючий підрядок): Boyer-Moore (0.100818 секунд)

В цілому, алгоритм Boyer-Moore виявився найшвидшим для обох текстів.
