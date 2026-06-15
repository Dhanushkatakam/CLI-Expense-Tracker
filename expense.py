class Expense:
     def __init__(self ,amount , description , date , category):
            self.amount = amount
            self.description = description
            self.date = date
            self.category = category
     def __str__(self):
            return f"{self.date}: {self.description} - rs{self.amount} ({self.category.name})"
      