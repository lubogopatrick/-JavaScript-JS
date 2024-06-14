def main():
    total = 0
    count = 0

    while True:
        try:
            user_input = input("Enter a number (or 'done' to finish): ")
            if user_input.lower() == 'done':
                break
            number = float(user_input)
            total += number
            count += 1
        except ValueError:
            print("Invalid input. Please enter a valid number or 'done'.")

    if count > 0:
        average = total / count
        print(f"Total: {total}, Count: {count}, Average: {average:.2f}")
    else:
        print("No valid numbers entered.")

if __name__ == "__main__":
    main()
