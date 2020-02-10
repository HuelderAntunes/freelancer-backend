from django.db.models import *
from django.contrib.auth.admin import User


class Role(Model):
    name = CharField(null=False, blank=False, max_length=50)
    description = CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f'{self.name} role'


class File(Model):
    name = CharField(max_length=50, blank=True, null=True)
    path = URLField(null=False, blank=False)
    created_at = DateField(auto_now_add=True)
    updated_at = DateField(auto_now=True)

    def __str__(self):
        return f'{self.path} file'


class BankAccount(Model):
    user = ForeignKey(User, on_delete=CASCADE)
    cpf = CharField(max_length=20)
    holder = CharField(max_length=130)
    account = CharField(max_length=20)
    agence = CharField(max_length=10)
    bank = CharField(max_length=10)

    def __str__(self):
        return f'{self.bank} - {self.user} bank account'


class PersonalData(Model):
    user = ForeignKey(User, on_delete=CASCADE, blank=True, null=True)
    role = ForeignKey(Role, on_delete=SET_NULL, null=True)
    avatar = ForeignKey(File, on_delete=SET_NULL, null=True, blank=True)
    birth_date = DateField(blank=True, null=True)
    cpf = CharField(max_length=20, blank=True, null=True)
    cnpj = CharField(max_length=50, blank=True, null=True)
    rg = CharField(max_length=20, blank=True, null=True)
    address = CharField(max_length=255, blank=True, null=True)
    address_complement = CharField(max_length=255, blank=True, null=True)
    state = CharField(max_length=30, blank=True, null=True)
    country = CharField(max_length=30, blank=True, null=True)
    state_subscription = CharField(max_length=100, blank=True, null=True)
    civic_subscription = CharField(max_length=100, blank=True, null=True)
    phone = CharField(max_length=20, blank=True, null=True)
    comercial_email = EmailField()
    fantasy_name = CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} personal data'


class CustomField(Model):
    name = CharField(null=False, blank=False, max_length=50)
    description = CharField(max_length=255, blank=True, null=True)
    data_type = CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return f'{self.name} customfield'


class CustomFieldValue(Model):
    custom_field = ForeignKey(CustomField, on_delete=SET_NULL, null=True)
    user = ForeignKey(User, on_delete=CASCADE)
    date_value = DateTimeField(blank=True, null=True)
    text_value = CharField(max_length=255, blank=True, null=True)
    number_value = FloatField(blank=True, null=True)
    created_at = DateField(auto_now_add=True)
    updated_at = DateField(auto_now=True)

    def __str__(self):
        return f'{self.custom_field.name} of {self.user.username}'


class ForgotPassword(Model):
    user = OneToOneField(User, on_delete=CASCADE, primary_key=True)
    token = CharField(max_length=200, null=True, blank=True, unique=True)

    created_date = DateTimeField(auto_now_add=True)
    updated_date = DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} token: {self.token}'
