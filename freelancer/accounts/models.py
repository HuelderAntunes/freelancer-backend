from django.db.models import *
from django.contrib.auth.admin import User


class Role(Model):
    name = CharField(null=False, blank=False, max_length=50)
    description = CharField(max_length=255)

    def __str__(self):
        return f"{self.name} role"


class File(Model):
    name = CharField(max_length=50)
    path = URLField(null=False, blank=False)
    created_at = DateField(auto_now_add=True)
    updated_at = DateField(auto_now=True)

    def __str__(self):
        return f"{self.name} file"


class BankAccount(Model):
    user = ForeignKey(User, on_delete=CASCADE)
    cpf = CharField(max_length=20)
    holder = CharField(max_length=130)
    account = CharField(max_length=20)
    agence = CharField(max_length=10)
    bank = CharField(max_length=10)

    def __str__(self):
        return f"{self.bank} - {self.user} bank account"


class PersonalData(Model):
    user = ForeignKey(User, on_delete=CASCADE)
    role = ForeignKey(Role, on_delete=SET_NULL, null=True)
    avatar = ForeignKey(File, on_delete=SET_NULL, null=True)
    birth_date = DateField()
    cpf = CharField(max_length=20)
    cnpj = CharField(max_length=50)
    rg = CharField(max_length=20)
    address = CharField(max_length=255)
    address_complement = CharField(max_length=255)
    state = CharField(max_length=30)
    country = CharField(max_length=30)
    state_subscription = CharField(max_length=100)
    civic_subscription = CharField(max_length=100)
    phone = CharField(max_length=20)
    comercial_email = EmailField()

    def __str__(self):
        return f"{self.user.username} personal data"


class CustomField(Model):
    name = CharField(null=False, blank=False, max_length=50)
    description = CharField(max_length=255)
    data_type = CharField(max_length=30)

    def __str__(self):
        return f"{self.name} customfield"


class CustomFieldValue(Model):
    custom_field = ForeignKey(CustomField, on_delete=SET_NULL, null=True)
    user = ForeignKey(User, on_delete=CASCADE)
    date_value = DateTimeField()
    text_value = CharField(max_length=255)
    number_value = FloatField()
    created_at = DateField(auto_now_add=True)
    updated_at = DateField(auto_now=True)

    def __str__(self):
        return f"{self.custom_field.name} of {self.user.username}"
