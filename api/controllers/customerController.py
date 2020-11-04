from api.models import Customer

def searchCustomer(phoneNumber):
    return Customer.objects.filter(phone_number__contains=phoneNumber)
