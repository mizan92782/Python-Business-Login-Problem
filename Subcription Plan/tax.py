
TAX_RATES={
    "USA" : 0.08,
    "UK" : 0.20,
    "Germany" : 0.10
}



class TaxCalculator:
    
    @classmethod
    def calculateTax(self,country:str,amount:int):
        country_tex = TAX_RATES[country]
        return amount*country_tex

        
