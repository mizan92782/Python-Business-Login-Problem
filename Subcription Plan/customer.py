from discount import NoDiscount

class Customer:
    def __init__(self,name,country,plan,users,discount=None):
        self.name = name
        self.country = country
        self.plan = plan
        self.users=users
        self.discount=discount
        
    
    def best_discount(self):
        if self.discount is None:
            return NoDiscount()
            
        return max(
            self.discount,
            key = lambda d: d.apply(100)
        )
        