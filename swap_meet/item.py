class Item:
    def __init__(self, category = "", condition = 0):
        self.category = category
        self.condition = condition
        
    def __str__(self):
        return "Hello World!"
       
    def condition_description(self):
        conditions = ["fair", "good", "very good", "excellent", "Near mint", "Mint"]    
        return conditions[self.condition]

    