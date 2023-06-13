# from _typeshed import Self
from django.db import models  # Create your models here.
from django.contrib.auth.models import User,AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator

STATE_CHOICES = (
    ('Andhra Pradesh', 'Andhra Pradesh'),
    ('Arunachal Pradesh', 'Arunachal Pradesh'),
    ('Assam', 'Assam'),
    ('Bihar', 'Bihar'),
    ('Chhattisgarh', 'Chhattisgarh'),
    ('Goa', 'Goa'),
    ('Gujarat', 'Gujarat'),
    ('Haryana', 'Haryana'),
    ('Himachal Pradesh', 'Himachal Pradesh'),
    ('Jammu and Kashmir', 'Jammu and Kashmir'),
    ('Jharkhand', 'Jharkhand'),
    ('Karnataka	', 'Karnataka	'),
    ('Kerala', 'Kerala'),
    ('Madhya Pradesh', 'Madhya Pradesh'),
    ('Maharashtra', 'Maharashtra'),
    ('Manipur', 'Manipur'),
    ('Meghalaya', 'Meghalaya'),
    ('Mizoram', 'Mizoram'),
    ('Nagaland', 'Nagaland'),
    ('Odisha', 'Odisha'),
    ('Punjab', 'Punjab'),
    ('Rajasthan', 'Rajasthan'),
    ('Sikkim', 'Sikkim'),
    ('Tamil Nadu', 'Tamil Nadu'),
    ('Telangana', 'Telangana'),
    ('Tripura', 'Tripura'),
    ('Uttar Pradesh', 'Uttar Pradesh'),
    ('Uttarakhand', 'Uttarakhand'),
    ('West Bengal', 'West Bengal'),
)


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    mobile = models.IntegerField()
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES, max_length=50)

    def __str__(self):
        return str(self.id)


CATEGORY_CHOICES = (
    ('do','Dog'),
    ('ca', 'Cat'),
    ('df','Dog_Food'),
    ('cf','Cat_Food'),
    )


class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    brand = models.CharField(max_length=100)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=5)
    product_image = models.ImageField(upload_to="productimg")

    def __str__(self):
        return str(self.id)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price


STATUS_CHOICES = (
    ('Accepted', 'Accepted'),
    ('Packed', 'Packed'),
    ('On The Way', 'On The Way'),
    ('Deliverd', 'Deliverd'),
    ('Cancel', 'Cancel')
)


class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='pending')

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price


class Feedback(models.Model):
    name = models.CharField(max_length=200)
    mobile = models.IntegerField()
    city = models.CharField(max_length=200)
    pincode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES, max_length=50)
    description = models.CharField(max_length=200)

    def __str__(self):
        return str(self.id)

PET_TYPE = (
    ('Cat', 'Cat'),
    ('Dog', 'Dog'),
)

class Report(models.Model):
    name = models.CharField(max_length=200)
    mobile = models.IntegerField(max_length=11)
    city = models.CharField(max_length=200)
    pincode = models.PositiveIntegerField(validators=[MaxValueValidator(999999)])
    state = models.CharField(choices=STATE_CHOICES, max_length=50)
    pet_type = models.CharField(choices=PET_TYPE, max_length=50)
    pet_breed = models.CharField(max_length=200)
    pet_location = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    def __str__(self):
        return str(self.id)

#
# USER_CHOICES = [
#     ('D', 'Donor'),
#     ('A', 'Adopter'),
#     ('N', 'NGO'),
#     ('C', 'Customer')
# ]

# class User(AbstractUser):
#     user_type = models.CharField(choices=USER_CHOICES, max_length=2)
#
#     def is_doctor(self):
#         if self.user_type == 'D':
#             return True
#         else:
#             return False
#
#     def is_patient(self):
#         if self.user_type == 'P':
#             return True
#         else:
#             return False
#
#     def is_receptionist(self):
#         if self.user_type == 'R':
#             return True
#         else:
#             return False
#
#     def is_HR(self):
#         if self.user_type == 'HR':
#             return True
#         else:
#             return False
#
#     class Meta:
#         ordering = ('id',)

