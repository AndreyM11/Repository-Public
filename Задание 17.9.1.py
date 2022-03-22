def num_sort(list_int):
    for i in range(1, len(list_int)):
        x = list_int[i]
        idx = i
        while idx > 0 and list_int[idx - 1] > x:
            list_int[idx] = list_int[idx - 1]
            idx -= 1
        list_int[idx] = x
    return list_int

def index_search(array, element, left, right):
    if left > right:
        return right
    middle = (right + left) // 2
    if array[middle] == element:
        return middle
    elif element < array[middle]:
        return index_search(array, element, left, middle - 1)
    else:
        return index_search(array, element, middle + 1, right)

numbers_str = input("Введите последовательность чисел через пробел: ")
numbers_list = list(map(int, numbers_str.split()))
numbers_sorted =num_sort(numbers_list)
element = int(input("Введите любое число: "))

for i in numbers_sorted:
   if  min(numbers_sorted) > element:
     print("Число не соответствует заданному условию задачи, повторите ввод: ")
     element = int(input("Введите любое число: "))
   elif  max(numbers_sorted)< element:
       print("Число не соответствует заданному условию задачи, повторите ввод: ")
       element = int(input("Введите любое число: "))
   elif i== element:
       break
print("Числа по возрастанию: ", numbers_sorted)
element_index = index_search(numbers_sorted, element, 0, len(numbers_sorted))
print("Индекс элемента: ", element_index)