
# CodeAlpha Task 2
# Stock Portfolio Tracker

import csv

# Predefined stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "MSFT": 420,
    "AMZN": 190,
    "GOOGL": 175
}

# Store portfolio details
portfolio = []

print("----- Stock Portfolio Tracker -----")
print("Available Stocks:", ", ".join(stock_prices.keys()))

# Take stock input from user
while True:
    stock = input("\nEnter stock symbol (or DONE to finish): ").strip().upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not available!")
        continue

    # Take quantity input
    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than zero!")
            continue

    except ValueError:
        print("Please enter a valid number!")
        continue

    # Calculate investment
    price = stock_prices[stock]
    investment = price * quantity

    # Save stock details
    portfolio.append((stock, quantity, price, investment))

    print("Investment:", investment)
    print("Stock added successfully!")

# Display portfolio summary
print("\n----- Portfolio Summary -----")

print(
    f"{'Stock':<10}"
    f"{'Quantity':<10}"
    f"{'Price':<10}"
    f"{'Investment':<12}"
)

print("-" * 42)

total_investment = 0

for item in portfolio:
    print(
        f"{item[0]:<10}"
        f"{item[1]:<10}"
        f"{item[2]:<10}"
        f"{item[3]:<12}"
    )

    total_investment += item[3]

print("-" * 42)
print("Total Investment:", total_investment)

# Save portfolio to CSV file
with open("portfolio.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Stock", "Quantity", "Price", "Investment"])

    for item in portfolio:
        writer.writerow(item)

    writer.writerow([])
    writer.writerow(["Total Investment", total_investment])

print("\nPortfolio saved to portfolio.csv")
print("Thank you for using Stock Portfolio Tracker!")