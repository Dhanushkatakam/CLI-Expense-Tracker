class Category:
    def __init__(self , name , budget_limit):
        self.name = name
        self.budget_limit = budget_limit
    def __str__(self):
        return  f"{self.name} (Budget: {self.budget_limit})"
    
