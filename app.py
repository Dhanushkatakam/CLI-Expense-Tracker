from flask import Flask, render_template, request, redirect
from tracker import ExpenseTracker
from datetime import date as dt

app = Flask(__name__)

tracker = ExpenseTracker()
tracker.load_data()

@app.route("/")
def home():
    expenses = tracker.get_all_expenses()
    total = tracker.get_total()
    warnings = []
    for cat in tracker.categories:
        spent = sum(exp.amount for exp in expenses if exp.category.name == cat.name)
        if spent > cat.budget_limit:
            warnings.append(f"{cat.name}: Over budget! Spent Rs.{spent} / Limit Rs.{cat.budget_limit}")
    return render_template("index.html", expenses=expenses, categories=tracker.categories, total=total, warnings=warnings)

@app.route("/add", methods=["POST"])
def add():
    description = request.form["description"]
    amount_str = request.form["amount"]
    if amount_str == "" or description == "":
        return redirect("/")
    amount = float(amount_str)
    date = str(dt.today())
    category = request.form["category"]
    tracker.add_expense(amount, description, date, category)
    tracker.save_data()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)