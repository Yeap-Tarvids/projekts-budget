import json
from collections import defaultdict
import os
import matplotlib.pyplot as plt

DATA_FILE = "budget_data.json"

class BudgetTracker:
    def __init__(self):
        self.total_budget = 0.0
        self.total_spent = 0.0
        self.category_limits = defaultdict(float)  
        self.category_spent = defaultdict(float)    

    def set_total_budget(self, amount):
        self.total_budget = amount
        print(f"Total budget set to ${self.total_budget:.2f}")

    def update_category_limit(self, category, amount):
        old_limit = self.category_limits.get(category, 0.0)
        self.category_limits[category] = old_limit + amount
        print(f"Updated budget limit for '{category}': was ${old_limit:.2f}, now ${self.category_limits[category]:.2f}")

    def show_all_budgets(self):
        remaining_total = self.total_budget - self.total_spent
        print(f"\n=== Total Budget ===")
        print(f"Total Budget: ${self.total_budget:.2f}")
        print(f"Total Spent: ${self.total_spent:.2f}")
        print(f"Total Remaining: ${remaining_total:.2f}\n")

        print("=== Category Budgets ===")
        if not self.category_limits:
            print("No categories set.")
        else:
            for cat, limit in self.category_limits.items():
                spent = self.category_spent[cat]
                remaining = limit - spent
                print(f"Category '{cat}': Spent ${spent:.2f} / Limit ${limit:.2f} (Remaining ${remaining:.2f})")

    def add_expense(self, category, amount):
        if category not in self.category_limits:
            print(f"Error: Category '{category}' does not exist. Please set or update the budget limit for it first.")
            return

        remaining_cat = self.category_limits[category] - self.category_spent[category]
        if amount > remaining_cat:
            print(f"Warning: This expense exceeds the remaining budget for '{category}' (${remaining_cat:.2f})!")

        remaining_total = self.total_budget - self.total_spent
        if amount > remaining_total:
            print(f"Warning: This expense exceeds your total remaining budget (${remaining_total:.2f})!")

        self.category_spent[category] += amount
        self.total_spent += amount
        print(f"Added expense of ${amount:.2f} to category '{category}'.")
        self.show_all_budgets()

        if self.total_spent > self.total_budget:
            print("\n*** WARNING: You have gone over budget, please refrain from spending any more or add more funds to your budget. ***")

    def add_money(self, amount):
        self.total_budget += amount
        print(f"Added ${amount:.2f} to total budget.")
        self.show_all_budgets()

        if self.total_spent > self.total_budget:
            print("\n*** WARNING: You have gone over budget, please refrain from spending any more or add more funds to your budget. ***")

    def show_spending_piechart(self):
        spent_categories = {cat: spent for cat, spent in self.category_spent.items() if spent > 0}
        total_spent = sum(spent_categories.values())
        remaining = self.total_budget - total_spent

        if self.total_budget == 0:
            print("Total budget is zero, cannot generate pie chart.")
            return

        labels = list(spent_categories.keys())
        sizes = list(spent_categories.values())

        if remaining > 0:
            labels.append("Remaining")
            sizes.append(remaining)
        elif remaining < 0:
            labels.append("Overspent")
            sizes.append(abs(remaining))

        plt.figure(figsize=(7,7))
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
        plt.title("Budget Spending Distribution")
        plt.axis('equal') 
        plt.show()

    def save_data(self):
        data = {
            "total_budget": self.total_budget,
            "total_spent": self.total_spent,
            "category_limits": dict(self.category_limits),
            "category_spent": dict(self.category_spent),
        }
        with open(DATA_FILE, "w") as f:
            json.dump(data, f)
        print("Data saved.")

    def load_data(self):
        if not os.path.exists(DATA_FILE):
            print("No saved data found. Starting fresh.")
            return
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
            self.total_budget = data.get("total_budget", 0.0)
            self.total_spent = data.get("total_spent", 0.0)
            self.category_limits = defaultdict(float, data.get("category_limits", {}))
            self.category_spent = defaultdict(float, data.get("category_spent", {}))
        print("Data loaded.")

    def clear_data(self):
        self.total_budget = 0.0
        self.total_spent = 0.0
        self.category_limits.clear()
        self.category_spent.clear()
        if os.path.exists(DATA_FILE):
            os.remove(DATA_FILE)
        print("All data cleared.")

def main():
    print("Welcome to Categorized Budget Tracker with Persistence!")
    tracker = BudgetTracker()
    tracker.load_data()

    while True:
        print("\nChoose an option:")
        print("1) Show total and category budgets")
        print("2) Set total budget")
        print("3) Update/add to category budget limit")
        print("4) Add expense with category")
        print("5) Add money to total budget")
        print("6) Clear all data")
        print("7) Exit")
        print("8) Show spending pie chart")

        choice = input("Your choice: ")

        if choice == "1":
            tracker.show_all_budgets()
        elif choice == "2":
            amount = float(input("Enter total budget amount to set: $"))
            tracker.set_total_budget(amount)
            tracker.save_data()
        elif choice == "3":
            cat = input("Enter category name: ").strip()
            amount = float(input(f"Enter amount to add to '{cat}' budget limit: $"))
            tracker.update_category_limit(cat, amount)
            tracker.save_data()
        elif choice == "4":
            cat = input("Enter expense category: ").strip()
            amount = float(input("Enter expense amount: $"))
            tracker.add_expense(cat, amount)
            tracker.save_data()
        elif choice == "5":
            amount = float(input("Enter amount to add to total budget: $"))
            tracker.add_money(amount)
            tracker.save_data()
        elif choice == "6":
            confirm = input("Are you sure you want to clear all data? (yes/no): ").lower()
            if confirm == "yes":
                tracker.clear_data()
            else:
                print("Clear data cancelled.")
        elif choice == "7":
            tracker.save_data()
            print("Exiting Budget Tracker. Goodbye!")
            break
        elif choice == "8":
            tracker.show_spending_piechart()
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()