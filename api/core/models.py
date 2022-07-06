from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):

    def __repr__(self):
        return self.username


class Product(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='products')
    title = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.title} by: {self.owner}'

cat_choices = (
    ('ui', 'UI'),
    ('ux', 'UX'),
    ('en', 'Enhancement'),
    ('ft', 'Feature'),
    ('bg', 'Bug'),

)
status_choices = (
    ('sg', 'Suggestion'),
    ('pl', 'Planned'),
    ('ip', 'In-progress')
)
class Feedback(models.Model):
    product_name = models.ForeignKey(Product, on_delete=models.CASCADE)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=cat_choices, default='en')
    upvotes = models.IntegerField(default=0)
    status = models.CharField(max_length=10, choices=status_choices, default='sg')
    description = models.TextField(max_length=400)

    def __str__(self):
        return self.description







