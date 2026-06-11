



class invoice:
    
    def __init__(
            self,
            customer,
            base_charge,
            discount,
            tax,
            final_amount):

        self.customer = customer
        self.base_charge = base_charge
        self.discount = discount
        self.tax = tax
        self.final_amount = final_amount
        
        
    
    def print_invoice(self):

        print("\n===== INVOICE =====")
        print(f"Customer : {self.customer.name}")
        print(f"Plan      : {self.customer.plan.plan_name}")

        print(
            f"Charge    : "
            f"${self.base_charge:.2f}"
        )

        print(
            f"Discount  : "
            f"-${self.discount:.2f}"
        )

        print(
            f"Tax       : "
            f"${self.tax:.2f}"
        )

        print(
            f"Total     : "
            f"${self.final_amount:.2f}"
        )
        