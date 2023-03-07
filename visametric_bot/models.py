from django.db import models

from .constants import *

class User(models.Model):
    telegram_id = models.CharField(max_length=20, unique=True)
    state = models.CharField(max_length=35, choices=USER_STATES)

    def get_state(user_id: str) -> str:
        user = User.objects.filter(telegram_id=user_id).first()
        return user.state if user else None

    def set_state(user_id: str, state: str) -> None:
        user, _ = User.objects.get_or_create(telegram_id=user_id)
        user.state = state
        user.save()


class Customer(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField()
    nationality = models.CharField(max_length=25, choices=NATIONALITY_OPTIONS)
    address = models.CharField(max_length=25, choices=ADDRESS_OPTIONS)
    passport_number = models.CharField(max_length=25)
    phone_number = models.CharField(max_length=12)
    plan = models.CharField(max_length=20, choices=PLANS, default="monthly")
    birth_date = models.DateField()
    passport_valid_date = models.DateField()
    is_registered = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    url_for_document = models.CharField(max_length=500, blank=True, null=True)

    def edit(pk, field, value):
        customer = Customer.objects.filter(id=pk).first()
        setattr(customer, field, value)
        customer.save()

    def remove_customer(pk):
        Customer.objects.filter(id=pk).first().delete()

    def get_all_customers(self, plan):
        return Customer.objects.filter(plan=plan)
    
    def get_full_name(self):
        return "{} {}".format(self.first_name, self.last_name)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    