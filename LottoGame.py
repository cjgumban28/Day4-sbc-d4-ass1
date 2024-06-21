import random


numbers = [int(input(f"Please enter the {i+1} number: ")) for i in range(3)]


lottery_numbers = [random.randint(1, 3), random.randint(1, 2), random.randint(2, 3)]


print("Your numbers are:", numbers)
print("And the lottery results are:", lottery_numbers)


if numbers == lottery_numbers:
    print("Jackpot!")
elif len(set(numbers) & set(lottery_numbers)) == 3:
    print("You partially win some rewards.")
else:
    print("Better luck next time.")
