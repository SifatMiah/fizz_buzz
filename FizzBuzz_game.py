def get_fizzbuzz_value(n):
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)

def fizzbuzz_game():
    print("🎮 Welcome to the FizzBuzz Game!")
    print("👉 Instructions:")
    print(" - Say 'Fizz' if the number is divisible by 3")
    print(" - Say 'Buzz' if the number is divisible by 5")
    print(" - Say 'FizzBuzz' if divisible by both")
    print(" - Otherwise, just enter the number itself")
    print(" - Type 'quit' anytime to exit the game early")
    print("Let's begin!\n")

    score = 0
    for number in range(1, 21):  # You can increase the range for a longer game
        user_input = input(f"What should you say for {number}? ").strip()

        if user_input.lower() == "quit":
            print("👋 Game exited by user.")
            break

        correct_answer = get_fizzbuzz_value(number)

        if user_input.lower() == correct_answer.lower():
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer was: {correct_answer}\n")

    print(f"🏁 Game Over! Your final score: {score}/{number if user_input.lower() != 'quit' else number - 1}")

if __name__ == "__main__":
    fizzbuzz_game()
