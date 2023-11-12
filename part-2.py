# Part-2: Pseudocode
# procedure calculate_points(num_books):
#     if num_books is 0 then
#         return 0
#     elif num_books is 2 then
#         return 5
#     elif num_books is 4 then
#         return 15
#     elif num_books is 6 then
#         return 30
#     elif num_books is greater than or equal to 8 then
#         return 60
#     else
#         return "Invalid input. Please enter a valid number of books."
#
# procedure main():
#     try
#         output("Enter the number of books purchased this month: ")
#         num_books = input()
#         num_books = convert_to_integer(num_books)
#         points = calculate_points(num_books)
#         output("Points awarded: " + points)
#     except ValueError:
#         output("Invalid input. Please enter a valid number.")
#
# main()
def calculate_points(num_books):
    if num_books == 0:
        return 0
    elif num_books == 2:
        return 5
    elif num_books == 4:
        return 15
    elif num_books == 6:
        return 30
    elif num_books >= 8:
        return 60
    else:
        return "Invalid input. Please enter a valid number of books."


def main():
    try:
        num_books = int(input("Enter the number of books purchased this month: "))
        points = calculate_points(num_books)
        print(f"Points awarded: {points}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")


if __name__ == "__main__":
    main()
