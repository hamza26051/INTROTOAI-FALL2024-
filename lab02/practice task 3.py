def find_maximum(*numbers):
    return max(numbers)

if __name__ == "__main__":
    numbers = input("Enter numbers ").split()
    numbers = [float(num) for num in numbers]
    max_value = find_maximum(*numbers)
    print("The maximum value is:", max_value)