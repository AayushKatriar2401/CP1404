"""
Cumulative Total Income
"""


def main():
    """Display Income Report"""
    incomes = []
    months = int(input("How Many Months?: "))
    for month in range(1, months + 1):
        income = float(input("Enter your income for the month {}: ".format(month)))
        incomes.append(income)

    print_report(incomes)


def print_report(incomes):
    """Printing Reports Based on Income"""
    print("\nIncome Report\n-------------")
    total = 0
    for month, income in enumerate(incomes):
        total += income
        print("Month {} - Income: ${} / Total: ${:10.2f}".format(month + 1, income, total))

    main()
