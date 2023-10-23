# Author: caleb moura

# Function to check if first and last letter of the dish match first letter of the animal
def can_bring_to_feast(animal, dish):
    return animal[0] == dish[0] and animal[0] == dish[-1]

# prompt user input for animal and dish
animal = input("Enter an animal: ").lower()
dish = input("Enter a dish: ").lower()

# Check if beast can bring the dish to the feast
result = can_bring_to_feast(animal, dish)

# Print result
print(result)