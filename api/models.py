from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField(max_length=500, blank=True, null=True)
    presenter = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

    class Meta:
        db_table = "company"

class Branch(models.Model):
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    address = models.TextField(max_length=500, blank=True, null=True)
    presenter = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        branch_return = str(self.company_id) + '_' + self.name
        return branch_return

    class Meta:
        db_table = "branch"
        ordering = ['name']

class Staff(models.Model):
    full_name = models.CharField(max_length=100)
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    branch_id = models.ManyToManyField(Branch)
    birthday = models.DateField(default='1980-01-01')
    id_number = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=12, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    address = models.TextField(max_length=200, blank=True, null=True)
    current_address = models.TextField(max_length=200, blank=True, null=True)
    photo = models.ImageField(upload_to='staffs')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.full_name

    class Meta:
        db_table = "staff"
        ordering = ['full_name']

class Customer(models.Model):
    full_name = models.CharField(max_length=100)
    branch_id = models.ForeignKey(Branch, on_delete=models.CASCADE)
    birthday = models.DateField(default='1980-01-01')
    id_number = models.CharField(max_length=20,blank=True, null=True)
    hometown = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=12, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    address = models.TextField(max_length=200, blank=True, null=True)
    current_address = models.TextField(max_length=200, blank=True, null=True)
    photo = models.ImageField(upload_to='customers')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.full_name

    class Meta:
        db_table = "customer"
        ordering = ['full_name']
        
class CollateralType(models.Model):
    col_desc = models.TextField(max_length=100, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    
    def __str__(self):
        return self.col_desc

    class Meta:
        db_table = "collateraltype"

class Collateral(models.Model):
    col_type = models.ForeignKey(CollateralType, on_delete=models.CASCADE)
    col_name = models.CharField(max_length=200, blank=False)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    value_date = models.DateField(auto_now=True)
    expire_date = models.DateField(auto_now=True)
    col_value = models.BigIntegerField(default=0)
    legal_info = models.TextField(max_length=500, blank=True, null=True)
    actual_info = models.TextField(max_length=500, blank=True, null=True)
    inputter = models.ForeignKey(Staff, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        col_rtn = str(self.customer_id) + '_' + self.col_name + '_' + str(self.col_value)
        return col_rtn

    class Meta:
        db_table = "collateral"

class Limit(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    LIMIT_DEFINE = [
        ('TIN_CHAP', 'Tín chấp'),
        ('THE_CHAP', 'Thế chấp'),
    ]
    limit_type = models.CharField(max_length=8,choices=LIMIT_DEFINE,default='THE_CHAP')
    #danh sach tai san

    limit_total = models.BigIntegerField(default=0)
    limit_used = models.BigIntegerField(default=0)
    limit_left = models.BigIntegerField(default=0)
    amount = models.BigIntegerField(default=0)
    value_date = models.DateField(auto_now=True)
    expire_date = models.DateField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  
    def __str__(self):
        limit_rtn = str(self.customer_id) + '_' + self.limit_type + '_' + str(self.amount)
        return limit_rtn

    class Meta:
        db_table = "limit"   

class InterestType(models.Model):
    name = models.CharField(max_length=50)
    type_desc = models.CharField(max_length=200, blank=True, null=True)
    interest_type = models.CharField(
        max_length=10,
        choices=[('PERCENTAGE', 'Phần trăm'),('CASH', 'VNĐ')],
        default='PERCENTAGE'
    )
    interest_basis = models.CharField(
        max_length=11,
        choices=[
            ('DAILY', 'Theo ngày'),
            ('WEEKLY', 'Theo tuần'),
            ('MONTHLY', 'Theo tháng'),
            ('YEARLY', 'Theo năm')
        ],
        default='YEARLY'
    )
    def __str__(self):
        interesttype_rtn = str(self.name) + '_' + self.interest_type + '_' + self.interest_basis
        return interesttype_rtn

    class Meta:
        db_table = "interesttype"   

class Loan(models.Model):
    limit_id = models.ForeignKey(Limit, on_delete=models.CASCADE)
    loan_desc = models.CharField(max_length=200)
    value_date = models.DateField(auto_now=True)
    expire_date = models.DateField(auto_now=True)
    amount = models.BigIntegerField(default=0)
    interest_type_id = models.ForeignKey(InterestType, on_delete=models.CASCADE)
    interest_rate = models.CharField(max_length=10, blank=False)
    bank_name = models.CharField(max_length=200, blank=True, null=True)
    account = models.CharField(max_length=30, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  
    def __str__(self):
        loan_rtn = str(self.limit_id) + '_' + self.loan_desc + '_' + str(self.amount)
        return loan_rtn

    class Meta:
        db_table = "loan"   