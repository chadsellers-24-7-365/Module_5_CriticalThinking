# Part-1: Pseudo-code
# Procedure averageRainfallCalculator():
#     // Ask for the number of years
#     Display "Enter the number of years: "
#     numYears = ParseAsInteger(GetUserInput())
#
#     totalRainfall = 0  // Initialize total rainfall
#
#     // Outer loop for each year
#     For year = 1 To numYears
#         // Inner loop for each month
#         For month = 1 To 12
#             // Ask the user for the inches of rainfall for the current month
#             Display "Enter the inches of rainfall for Year ", year, ", Month ", month, ": "
#             rainfall = ParseAsFloat(GetUserInput())
#
#             // Add the rainfall to the total
#             totalRainfall = totalRainfall + rainfall
#         End For
#     End For
#
#     // Calculate the total number of months
#     totalMonths = numYears * 12
#
#     // Calculate the average rainfall per month
#     averageRainfall = totalRainfall / totalMonths
#
#     // Display the results
#     Display "\nResults:"
#     Display "Total number of months: ", totalMonths
#     Display "Total inches of rainfall: ", totalRainfall
#     Display "Average rainfall per month: ", FormatFloat(averageRainfall, 2), " inches"
# End Procedure
#
# // Run the program
# If IsMainModule():
#     Call averageRainfallCalculator()
#
def average_rainfall_calculator():
    # Ask for the number of years
    num_years = int(input("Enter the number of years: "))

    total_rainfall = 0  # Initialize total rainfall

    # Outer loop for each year
    for year in range(1, num_years + 1):
        # Inner loop for each month
        for month in range(1, 13):
            # Ask the user for the inches of rainfall for the current month
            rainfall = float(input(f"Enter the inches of rainfall for Year {year}, Month {month}: "))

            # Add the rainfall to the total
            total_rainfall += rainfall

    # Calculate the total number of months
    total_months = num_years * 12

    # Calculate the average rainfall per month
    average_rainfall = total_rainfall / total_months

    # Display the results
    print("\nResults:")
    print(f"Total number of months: {total_months}")
    print(f"Total inches of rainfall: {total_rainfall}")
    print(f"Average rainfall per month: {average_rainfall:.2f} inches")


# Run the program
if __name__ == "__main__":
    average_rainfall_calculator()