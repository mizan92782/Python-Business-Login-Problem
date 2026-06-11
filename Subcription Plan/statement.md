Progressive Learning Path

Generate exercises in increasing difficulty.

Level 1 – Intermediate

Single-domain systems with moderate business rules.

Examples:

Insurance premium calculator
Restaurant order management
Employee payroll engine
Subscription billing system
Level 2 – Advanced

Systems involving multiple subsystems and richer workflows.

Examples:

Airline reservation system
Warehouse fulfillment platform
Ride-sharing fare engine
Claims processing system
Level 3 – Enterprise

Large-scale systems resembling those built in major companies.

Examples:

Payment gateway processing platform
Multi-vendor e-commerce marketplace
Trading and order execution engine
Telecom billing platform
Fraud detection workflow engine
Additional Instructions
Focus on software engineering rather than algorithm puzzles.
Prioritize realistic business requirements over artificial complexity.
Encourage clean architecture and SOLID principles.
Assume Python 3.12+.
Favor readability and maintainability over clever code.
Challenge my design decisions during reviews as a senior engineer would.
Increase complexity gradually based on my demonstrated ability.
Keep each exercise difficult enough that implementation may require several hundred lines of code.

My goal is to develop the software design, architectural thinking, and implementation skills expected of engineers building production systems in top technology companies.

I would also add one final instruction because it changes the quality of the exercises dramatically:

Do not optimize the exercises for interview preparation. Optimize them for real software engineering work, where requirements evolve, trade-offs matter, and maintainability is often more important than achieving the shortest implementation.

This transforms the experience from "advanced coding practice" into a simulated apprenticeship with a senior engineer reviewing production-quality systems.

Level 1 (Intermediate → Industry-Oriented)
Problem: Subscription Billing and Invoice Management System
Business Context

You work for a SaaS company called CloudTask, which sells project management software.

Customers subscribe to different plans, and every month the company must generate invoices. The billing department currently does this manually using spreadsheets, which has become error-prone as the customer base grows.

Your task is to build a billing engine that automates subscription charging.

The system should be designed using OOP and should be maintainable because the business expects new subscription plans and discount rules in the future.

Problem Statement

CloudTask offers three subscription plans:

Plan Monthly Fee Included Users
Basic $20 3
Professional $50 10
Enterprise $100 20

Additional users cost:

Basic: $8 per extra user
Professional: $6 per extra user
Enterprise: $5 per extra user
Discounts

Customers may receive discounts:

Startup Discount
15% off total bill.
Nonprofit Discount
20% off total bill.
Only one discount can be applied.
If multiple discounts exist, apply the highest one.
Taxes

Tax rules depend on customer country:

Country Tax Rate
USA 8%
UK 20%
Germany 19%
Others 0%

Tax is calculated after discounts.

Invoice Requirements

Each invoice must contain:

Customer name
Plan name
Base plan charge
Extra user charge
Discount amount
Tax amount
Final payable amount
Example Scenarios
Scenario 1

Customer:

Name: Alice Inc.
Country: USA
Plan: Basic
Active Users: 5
Discounts: Startup

Calculation:

Basic Fee = 20

Extra Users = 5−3 = 2

Extra Charge = 2 × 8 = 16

Subtotal = 36

Discount = 15% = 5.40

After Discount = 30.60

Tax = 8% = 2.448

Final = 33.048

Invoice Total = $33.05

Scenario 2

Customer:

Name: Helping Hands
Country: UK
Plan: Professional
Active Users: 8
Discounts: Nonprofit

Final Amount = $48.00

Scenario 3

Customer:

Name: Mega Corp
Country: Germany
Plan: Enterprise
Users: 35
No Discounts

Final Amount = $178.50

Requirements Analysis
Entities
Customer
Subscription Plan
Discount Policy
Tax Calculator
Invoice
Billing Service
OOP Concepts Expected
Encapsulation
Abstraction
Polymorphism
Composition
