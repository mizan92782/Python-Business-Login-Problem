from abc import ABC,abstractmethod

class SubscriptionPlan(ABC):
    
    def __init__(self,plan_name,monthly_fee,include_user,extra_user_fee):
        self.plan_name,self.monthly_fee,self.include_user,self.extra_user_fee=plan_name,monthly_fee,include_user,extra_user_fee
    
    def calculate_monthly_charge(self,users):
        extra_user = max(0, users-self.include_user)
        return (
            self.monthly_fee+extra_user*self.extra_user_fee
        )
        
        
        
# plans

class BasicPlan(SubscriptionPlan):
    def __init__(self):
        super().__init__(
            "Basic",
            20,
            3,
            8
        )


class ProfessionalPlan(SubscriptionPlan):
    def __init__(self):
        super().__init__(
            "Professional",
            50,
            10,
            6
        )


class EnterprisePlan(SubscriptionPlan):
    def __init__(self):
        super().__init__(
            "Enterprise",
            100,
            20,
            5
        )
        