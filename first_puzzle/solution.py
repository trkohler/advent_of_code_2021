
with open("input_for_first_puzzle.txt", "r") as input_file:
    lines = input_file.readlines()
    lines = [int(el) for el in lines]


def count_increase(measurement_list: list) -> int:
    count = 0
    for i in range(1, len(measurement_list)):
        if measurement_list[i] > measurement_list[i-1]:
            count += 1
    return count

if __name__ == "__main__":
    count = count_increase(lines)
    print(count)