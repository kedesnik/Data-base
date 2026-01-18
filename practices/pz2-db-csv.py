import csv
import math

# 1
def Task1():
    with open("schedule.csv", "r", encoding="utf-8") as sch:
        reader = csv.reader(sch)
        next(reader)
        results = []

        for row in reader:
            station = row[1]
            hours = int(row[2])
            minutes = int(row[3])

            time_in_hours = hours + minutes / 60
            distance = 60 * time_in_hours
            results.append(f"{station}\t{math.floor(distance)}")

    for result in results:
        print(result)

# 2
def Task2():
    def is_beach_open(equipped, rescuers, pollution, temperature):
        return (equipped == '1' and rescuers == '1' and pollution <= 0.5 and temperature >= 18)

    with open("beaches.csv", "r", encoding="utf-8") as b:
        reader = csv.reader(b, delimiter=';')
        next(reader)
        open_beaches = []

        for row in reader:
            beach_name = row[1]
            equipped = row[2]
            rescuers = row[3]
            pollution = float(row[4])
            temperature = float(row[5])

            if is_beach_open(equipped, rescuers, pollution, temperature):
                open_beaches.append(beach_name)

    for beach in open_beaches:
        print(beach)

# 3
def Task3():
    def read_strikes(file_name):
        with open(file_name, "r", encoding="utf-8") as st:
            return [list(map(int, line.strip().split())) for line in st]

    def calculate_probabilities(strikes):
        rows = len(strikes)
        cols = len(strikes[0])
        probabilities = [[0] * cols for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                strike_sum = 0
                count_cells = 0

                for x in range(i - 1, i + 2):
                    for y in range(j - 1, j + 2):
                        if (0 <= x < rows) and (0 <= y < cols) and (x != i or y != j):
                            strike_sum += strikes[x][y]
                            count_cells += 1
                
                probability = strike_sum / count_cells
                
                if strikes[i][j] == 1:
                    probability = max(0, probability - 0.1)

                probabilities[i][j] = round(probability, 3)
        
        return probabilities

    def write_probabilities(probabilities, file_name):
        with open(file_name, "w", encoding="utf-8", newline='') as pr:
            writer = csv.writer(pr, delimiter=';')
            for row in probabilities:
                writer.writerow(row)

    strikes = read_strikes("strikes.csv")
    probabilities = calculate_probabilities(strikes)
    write_probabilities(probabilities, "predict.csv")

# 4
def Task4():
    def read_waves(file_name):
        with open(file_name, "r", encoding="utf-8") as st:
            return [list(map(int, line.strip().split(','))) for line in st]

    def check_wave_conditions(wave, max_height):
        counts = {}
        for height in wave:
            if height in counts:
                counts[height] += 1
            else:
                counts[height] = 1

        has_two_same = any(count == 2 for count in counts.values())
        has_unique = len(counts) == 5

        max_digit = max_height % 10
        has_matching_digit = any(height % 10 == max_digit for height in wave)

        even_count = sum(1 for height in wave if height % 2 == 0)
        
        return has_two_same and has_unique and has_matching_digit and even_count >= 3

    waves = read_waves("storm.csv")
    max_height = max(height for wave in waves for height in wave)
    suitable_waves_count = 0
    min_peak_height = float('inf')

    for wave in waves:
        if check_wave_conditions(wave, max_height):
            suitable_waves_count += 1
            min_peak_height = min(min_peak_height, min(wave))

    if suitable_waves_count > 0:
        print(suitable_waves_count, min_peak_height)
    else:
        print("Нет подходящих волн")

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