from collections import deque

with open("second_puzzle/input_for_second_puzzle.txt", "r") as input_file:
    lines = input_file.readlines()
    lines = [int(el) for el in lines]
    
def count_increase_with_window(measurements: list, window_size: int) -> int:
    d = deque(maxlen=window_size)
    previous_sum = None
    count = 0
    
    for i in range(len(measurements)):
        d.append(measurements[i])
        current_deque_sum = sum(d)
        
        if len(d) == window_size:
            if previous_sum and current_deque_sum > previous_sum:
                count += 1
            previous_sum = current_deque_sum
        
    
    return count

if __name__ == "__main__":
    count = count_increase_with_window(lines, 3)
    print(count)