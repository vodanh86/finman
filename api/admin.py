from django.contrib import admin
from .models import (
    Company, Staff, Branch, Customer, 
    CollateralType, Collateral, Limit,
    InterestType, Loan,
)

# Register your models here.
admin.site.register(Company)
admin.site.register(Branch)
admin.site.register(Staff)
admin.site.register(Customer)
admin.site.register(CollateralType)
admin.site.register(Collateral)
admin.site.register(Limit)
admin.site.register(InterestType)
admin.site.register(Loan)
