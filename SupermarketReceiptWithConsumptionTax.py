
"""Build supermarket receipts with a shared consumption tax rate."""


class GroceryBill:
    """Represent a customer's supermarket bill."""

    tax_rate = 0.10

    def __init__(self, customer_name):
        """Initialize a customer's shopping bill."""
        self.customer_name = customer_name
        self.items = []

    def add_item(self, item_name, price):
        """Add an item and its price to the shopping list."""
        self.items.append((item_name, price))
        print(f"{item_name} added successfully.")

    def subtotal(self):
        """Calculate the total price before tax."""
        return sum(price for item, price in self.items)

    def print_receipt(self):
        """Print the receipt with subtotal, tax, and final total."""
        subtotal = self.subtotal()
        tax = subtotal * GroceryBill.tax_rate
        total = subtotal + tax

        print("\n========== SUPERMARKET RECEIPT ==========")
        print(f"Customer: {self.customer_name}")
        print("-----------------------------------------")

        for item, price in self.items:
            print(f"{item}: ¥{price:.2f}")

        print("-----------------------------------------")
        print(f"Subtotal: ¥{subtotal:.2f}")
        print(f"Consumption Tax ({GroceryBill.tax_rate * 100:.0f}%): ¥{tax:.2f}")
        print(f"Total: ¥{total:.2f}")
        print("=========================================")


def main():
    """Collect grocery items and generate a receipt."""

    customer_name = input("Enter customer name: ")
    bill = GroceryBill(customer_name)

    while True:
        item_name = input("\nEnter item name (or 'done' to finish): ")

        if item_name.lower() == "done":
            break

        price = float(input("Enter item price (¥): "))
        bill.add_item(item_name, price)

    bill.print_receipt()


if __name__ == "__main__":
    main()
