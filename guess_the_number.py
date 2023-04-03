import random


def get_number():
    """ Simple Guess game from 1-100
    Good luck :)
    :rtype: int
    :return: given number as int
    """
    while True:
        try:
            result = int(input("Guess the number: "))
            break
        except ValueError:
            print("It's not a number")

    return result


def guess_the_number():
    """Main function with quess the number."""
    lucky_number = random.randint(1, 100)
    given_number = get_number()
    while given_number != lucky_number:
        if given_number < lucky_number:
            print("Too small!")
        else:
            print("Too big!")
        given_number = get_number()
    print("You Win!")


if __name__ == '__main__':
    guess_the_number()