from django.db.models import *
from freelancer.accounts.models import User


class Avaliation(Model):
    evaluator = ForeignKey(User, on_delete=CASCADE,
                           related_name="evaluator_user")
    rated = ForeignKey(User, on_delete=CASCADE, related_name="rated_user")
    created_at = DateField(auto_now_add=True)
    updated_at = DateField(auto_now=True)

    def __str__(self):
        return f"{self.rated} avaliation by {self.evaluator}"


class AvaliationField(Model):
    name = CharField(null=False, blank=False, max_length=50)
    description = CharField(max_length=255)

    def __str__(self):
        return f"{self.name} avaliation field"


class AvaliationValue(Model):
    avaliation = ForeignKey(Avaliation, on_delete=CASCADE)
    avaliation_type = ForeignKey(AvaliationField, on_delete=CASCADE)
    rank = IntegerField(null=False, blank=False)

    def __str__(self):
        return f"{self.avaliation_type} of {self.avaliation.rated}"
