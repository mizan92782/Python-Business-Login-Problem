from customer import Customer
from subcription import BasicPlan
from discount import StartupDiscount
from billing import BillingServeice

customer1 = Customer(
    "Alice Inc.",
    "USA",
    BasicPlan(),
    5,
    [StartupDiscount()]
)

invoice = BillingServeice.generate_invoice(
    customer1
)

invoice.print_invoice()