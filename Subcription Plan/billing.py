from invoice import invoice as Invoice
from tax import TaxCalculator


class BillingServeice:
    
    @staticmethod
    def generate_invoice(customer):
        
        
        base_charge = customer.plan.calculate_monthly_charge(customer.users)
        
        # find which type of Discount should apply ***vvi
        discount_strategy = (
            customer.best_discount()
        )
        
        
        # now apply discosutn on base amount
        discount = discount_strategy.apply(base_charge)
        
        # jtax claculation
        discounted_amount = (
            base_charge - discount
        )

        tax = TaxCalculator.calculateTax(
            customer.country,
            discounted_amount
        )

        final_amount = (
            discounted_amount + tax
        )
        
        return Invoice(
            customer,
            base_charge,
            discount,
            tax,
            final_amount
            
            
            
        )
        
        
        
        