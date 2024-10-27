# Nardos Gebremedhin
# Module 3. 1
# creating a program that asks the user how many bottles of beer are on the wall.
# and Pass that input to a function that manages the countdown.
# The function should take
# the input and count backwards to 1 while displaying the number of remaining bottles of beer on the wall.
# Once the count is down to 1, change lyrics to show "1 bottle of beer..."
# At the end of the countdown, get back to the main program and remind the user to buy more beer.

# got the lyrics from this website https://www.99-bottles-of-beer.net/lyrics.html
def countdown_bottles(num_bottles):
    # doing an if statment for the range and countdown function
    for i in range(num_bottles, 0, -1):
        if i > 1:
            print(f"{i} bottles of beer on the wall, {i} bottles of beer.")
            print(f"Take one down, pass it around, {i-1} bottles of beer on the wall.\n")
        else:
            # When there is only one bottle left
            print(f"1 bottle of beer on the wall, 1 bottle of beer.")
            print("Take one down, pass it around, no more bottles of beer on the wall.\n")


def main():
    # Ask the user for the number of bottles
    num_bottles = int(input("Enter the number of bottles of beer on the wall: "))

    # Call the function to manage the countdown
    countdown_bottles(num_bottles)

    # Reminder message after the countdown
    print("No more bottles of beer on the wall. Time to buy more beer!")

# Run the main function
if __name__ == "__main__":
    main()
