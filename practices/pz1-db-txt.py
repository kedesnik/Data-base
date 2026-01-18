# 1
def Task1():
    with open("poem.txt", "r", encoding="utf-8") as p, \
        open("counting.txt", "w", encoding="utf-8") as c:
        for i, line in enumerate(p, start=1):
            c.write(f"{i} - {line}")

# 2
def Task2():
    with open("todo.txt", "r", encoding="utf-8") as to, \
        open("no_repeat.txt", "w", encoding="utf-8") as no:
        unique_tasks = set(line.rstrip() for line in to)
        for task in unique_tasks:
            no.write(f"{task}\n")

# 3 butt1.txt; butt2.txt; butt3.txt; butt4.txt
def Task3():
    from collections import defaultdict

    file_input = input("Введите имена файлов через точку с запятой и пробел: ")
    file_names = [file.strip() for file in file_input.split(';')]

    butterfly_count = defaultdict(int)

    for file_name in file_names:
        with open(file_name, "r", encoding="utf-8") as file:
                unique_butterflies = set(line.rstrip() for line in file)
                for butterfly in unique_butterflies:
                    butterfly_count[butterfly] += 1

    result = [butterfly for butterfly, count in butterfly_count.items() if count == 2]
    for butterfly in result:
        print(butterfly)

# 4
def Task4():
    def check_conditions(numbers):
        unique_numbers = list(set(numbers))
        if len(unique_numbers) != 4: 
            return False
        for num in unique_numbers:
            if numbers.count(num) == 3:
                repeating_number = num
                break
        else:
            return False
        avg_unique = sum(unique_numbers) / 4
        max_num = max(numbers)
        min_num = min(numbers)
        return (avg_unique >= repeating_number) and (max_num % min_num != 0)

    min_sum = float('inf')
    desired_line_number = -1

    with open("numbers.txt", "r", encoding="utf-8") as file:
        for index, line in enumerate(file.readlines(), start=1):
            numbers = list(map(int, line.split()))
            if len(numbers) == 6 and check_conditions(numbers):
                current_sum = sum(numbers)
                if current_sum < min_sum:
                    min_sum = current_sum
                    desired_line_number = index

    if desired_line_number != -1:
        print(f"Номер строки с наименьшей суммой: {desired_line_number}")
    else:
        print("Нет строк, удовлетворяющих условиям.")

def main():
    n = int(input("Номер задания: "))
    match n:
        case 1:
            Task1()
        case 2:
            Task2()
        case 3:
            Task3()
        case 4:
            Task4()

main()
