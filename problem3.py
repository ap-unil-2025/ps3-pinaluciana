"""
Problem 3: Number Analysis
Analyze a list of numbers provided by the user.
"""

def get_numbers_from_user():
    """
    Get numbers from user until they type 'done'.
    Return a list of numbers.

    Returns:
        list: List of numbers entered by user
    """
    numbers = []

    while True:
        inp = input("Enter a number: ").strip()
        if inp.lower() == "done":
            break
        try:
            num = float(inp)
            numbers.append(num)
        except ValueError:
            print("Invalid number. Try again.")
    return numbers


def analyze_numbers(numbers):
    """
    Analyze the list and return a dictionary with:
    - count: number of elements
    - sum: sum of all numbers
    - average: average value
    - minimum: smallest number
    - maximum: largest number
    - even_count: count of even numbers
    - odd_count: count of odd numbers

    Args:
        numbers (list): List of numbers to analyze

    Returns:
        dict: Dictionary with analysis results, or None if list is empty
    """
    if not numbers:
        return None

    analysis = {}
    analysis["count"] = len(numbers)
    analysis["sum"] = sum(numbers)
    analysis["average"] = round(sum(numbers)/len(numbers), 2)
    analysis["minimum"] = min(numbers)
    analysis["maximum"] = max(numbers)
    analysis["even_count"] = sum(1 for n in numbers if int(n) % 2 == 0)
    analysis["odd_count"] = sum(1 for n in numbers if int(n) % 2 != 0)

    return analysis


def display_analysis(analysis):
    """
    Display the analysis in a formatted way.

    Args:
        analysis (dict): Dictionary containing analysis results
    """
    if not analysis:
        print("No data to display.")
        return

    print("\nAnalysis Results:")
    print("-" * 20)
    print("---------")
    print(f"Count: {analysis["count"]}")
    print(f"Sum: {analysis["sum"]}")
    print(f"Average: {analysis["average"]:.2f}")
    print(f"Minimum: {analysis["minimum"]}")
    print(f"Maximum: {analysis["maximum"]}")
    print(f"Even numbers: {analysis["even_count"]}")
    print(f"Odd numbers: {analysis["odd_count"]}")

def main():
    """Main function to run the number analyzer."""
    print("Number Analyzer")
    print("Enter numbers one at a time. Type 'done' when finished.")
    print()

    # Get numbers from user
    numbers = get_numbers_from_user()

    if not numbers:
        print("No numbers entered!")
        return

    # Analyze the numbers
    analysis = analyze_numbers(numbers)

    # Display the results
    display_analysis(analysis)


if __name__ == "__main__":
   main()