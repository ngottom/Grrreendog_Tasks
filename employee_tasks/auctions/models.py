from django.contrib.auth.models import AbstractUser
from django.db import models

from datetime import datetime
from django.core.validators import MaxValueValidator, MinValueValidator


class User(AbstractUser):
    pass


class Section(models.Model):
    sectionName = models.CharField(max_length=200)

    def __str__(self):
        return self.sectionName


class Employee(models.Model):
    employeeName = models.CharField(max_length=200)
    phone = models.FloatField()
    section = models.ForeignKey(
        Section, on_delete=models.CASCADE, blank=True, null=True, related_name="section")
    isActive = models.BooleanField(default=True)

    def __str__(self):
        return self.employeeName


class Category(models.Model):
    categoryName = models.CharField(max_length=300)

    def __str__(self):
        return self.categoryName


class Listing(models.Model):
    title = models.CharField(max_length=300)
    description = models.CharField(max_length=1000)
    imageURL = models.CharField(max_length=1000)
    price = models.FloatField()
    isActive = models.BooleanField(default=True)
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE,  blank=True, null=True, related_name="user")
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, blank=True, null=True, related_name="category")
    watchlist = models.ManyToManyField(
        User, blank=True, null=True, related_name="listingWatchlist")


class EmployeeListing(models.Model):
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, blank=True, null=True, related_name="employee")
    section = models.ForeignKey(
        Section, on_delete=models.CASCADE, blank=True, null=True)
    tasks = models.CharField(max_length=1000)
    extras = models.CharField(max_length=1000, default="None")
    extrasPrice = models.FloatField(default=0)

    # default date is today
    startYear = models.PositiveIntegerField(
        validators=[MinValueValidator(2022)])
    startMonth = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(12)])
    startDay = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(31)])
    startHour = models.PositiveIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(23)])
    startMinute = models.PositiveIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(59)])

    # endTime
    endMonth = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(12)])
    endDay = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(31)])
    endHour = models.PositiveIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(23)])
    endMinute = models.PositiveIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(59)])

    #
    dateStart = datetime.now()
    dateEnd = datetime.now()
    # create this in views later
    # dateStart = datetime(startYear, startMonth, startDay,startHour, startMinute)
    # dateEnd = datetime(endYear, endMonth, endDay, endDay, endHour, endMinute)
    # purchased = models.ManyToManyField(
    #     User, blank=True, null=True, related_name="listingPurchased")
    # anchor

    #

    def __str__(self):
        return f"{self.employee.employeeName}: {dateStart}"


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,  blank=True, null=True, related_name="userComment")
    listing = models.ForeignKey(
        Listing, on_delete=models.CASCADE,  blank=True, null=True, related_name="listingComment")
    message = models.CharField(max_length=200)
    datetime = models.CharField(
        max_length=100, default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    def __str__(self):
        return f"{self.author} about {self.listing}: {self.message}"


# class Purchase(models.Model):
#     listing = models.ForeignKey(
#         Listing, on_delete=models.CASCADE,  blank=True, null=True, related_name="listingPurchase")
#     purchaseUser = models.ForeignKey(
#         User, on_delete=models.CASCADE,  blank=True, null=True, related_name="purchaseUser"),
#     purchaseListing = models.ForeignKey(
#         Listing, on_delete=models.CASCADE,  blank=True, null=True, related_name="purchaseListing")
