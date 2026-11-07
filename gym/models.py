from django.db import models
from django.utils import timezone


class Enquiry(models.Model):
	name = models.CharField(max_length=100)
	email = models.EmailField()
	phone = models.CharField(max_length=20)
	age = models.PositiveIntegerField(null=True, blank=True)
	gender = models.CharField(max_length=20, blank=True)
	message = models.TextField()
	status = models.CharField(max_length=20, default='New')
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-created_at']

	def __str__(self):
		return self.name


class GymPlan(models.Model):
	name = models.CharField(max_length=100)
	duration_months = models.PositiveIntegerField()
	price = models.DecimalField(max_digits=10, decimal_places=2)
	description = models.TextField(blank=True)
	is_active = models.BooleanField(default=True)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name


class Member(models.Model):
	class Status(models.TextChoices):
		ACTIVE = 'Active', 'Active'
		EXPIRED = 'Expired', 'Expired'
		SUSPENDED = 'Suspended', 'Suspended'

	name = models.CharField(max_length=100)
	email = models.EmailField(blank=True)
	phone = models.CharField(max_length=20)
	age = models.PositiveIntegerField(null=True, blank=True)
	gender = models.CharField(max_length=20, blank=True)
	plan = models.ForeignKey(
		GymPlan,
		on_delete=models.PROTECT,
		related_name='members',
		null=True,
		blank=True,
	)
	join_date = models.DateField(default=timezone.localdate)
	expiry_date = models.DateField(null=True, blank=True)
	initial_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
	status = models.CharField(max_length=20, choices=Status.choices, default=Status.ACTIVE)
	emergency_contact = models.CharField(max_length=100, blank=True)
	emergency_phone = models.CharField(max_length=20, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-created_at']

	def __str__(self):
		return self.name


class Equipment(models.Model):
	name = models.CharField(max_length=100)
	price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
	quantity = models.PositiveIntegerField(default=1)
	unit = models.CharField(max_length=30, default='Piece')
	purchase_date = models.DateField(null=True, blank=True)
	description = models.TextField(blank=True)
	condition = models.CharField(max_length=50, default='Good')
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name
