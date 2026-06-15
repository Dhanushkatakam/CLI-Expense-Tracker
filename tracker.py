import json
from category import Category
from expense import Expense
class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.categories = []
    def add_category(self, name , budget_limit):
        category = Category(name, budget_limit)
        self.categories.append(category)
    def add_expense(self, amount, description, date, category_name):
        for cat in self.categories:
            if cat.name ==category_name:
                expense = Expense(amount, description, date, cat)
                self.expenses.append(expense)
        return None
    def get_total(self):
        return sum(expense.amount for expense in self.expenses)
    def get_all_expenses(self):
        return self.expenses
    def filter_by_category(self, category_name):
        return [expense for expense in self.expenses if expense.category.name == category_name]
    def save_data(self, filename="data.json"):
        data = {
            "categories": [{"name": cat.name, "budget_limit": cat.budget_limit} for cat in self.categories],
            "expenses": [{"amount": exp.amount, "description": exp.description, "date": exp.date, "category": exp.category.name} for exp in self.expenses]
        }
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
    def load_data(self, filename="data.json"):
        try:
            with open(filename, "r") as f:
                data = json.load(f)
            for cat in data["categories"]:
                self.add_category(cat["name"], cat["budget_limit"])
            for exp in data["expenses"]:
                self.add_expense(exp["amount"], exp["description"], exp["date"], exp["category"])
        except FileNotFoundError:
            pass        
