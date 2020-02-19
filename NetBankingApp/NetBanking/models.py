import uuid
from django.db import models
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator,
    RegexValidator,
)

from django.utils.translation import ugettext_lazy as _
from uuid import uuid4

# Create your models here.

class Users(models.Model) :
    id = models.UUIDField(editable = False , unique = True , primary_key = True , default=uuid.uuid4)
    First_name = models.CharField(max_length = 100)
    Last_name = models.CharField(max_length = 100)

    username = models.CharField(
        _('username'), max_length=30, unique=True, null=True, blank=True,
        help_text=_(
            'Required. 30 characters or fewer. Letters, digits and '
            '@/./+/-/_ only.'
        ))

    #get age , if age is less than 18 .. dont allow to create account
    DOB = models.DateField(null = False , blank = False)
    Address = models.TextField()

    password = models.CharField(
        _('password'), max_length=30, unique=False, null=True, blank=True,
          help_text=_(
              'Required. 30 characters or fewer. Letters, digits and '
              'special characters'
          ))

    def __str__(self) :
        return str(self.username)

class Account(models.Model) :
    user = models.ForeignKey(Users , on_delete = models.CASCADE , related_name = 'accounts')

    #using MinValueValidator and MaxValueValidator to validage account number to have 8 digits

    account_no = models.IntegerField(
        unique=True,
        validators=[
            MinValueValidator(10000000),
            MaxValueValidator(99999999)
        ] ,
        null=True , blank = True
    )

    #validating password to have special characters and upper and lower case letters and digits
    pin = models.IntegerField(
         unique=False, null=True, blank=True,
          help_text=_(
              'Required. 6 digits or fewer.  digits'
          ))

    #minimum balance is 2000
    #maximum balance allowed is 999999

    balance = models.DecimalField(decimal_places=2 , max_digits=6)

    def __str__(self) :
          return str(self.account_no + " balance : " + self.balance)

class Transations(models.Model) :
    sender = models.ForeignKey(Users , on_delete = models.CASCADE , related_name = '+')
    senders_account = models.ForeignKey(Account , on_delete = models.CASCADE , related_name = '+')
    receiver = models.ForeignKey(Users , on_delete = models.CASCADE , related_name = '+')
    receivers_account = models.ForeignKey(Account , on_delete = models.CASCADE , related_name = '+')
    money_sent = models.DecimalField(default = 2000 , decimal_places = 5 , max_digits = 6)
    reason = models.TextField(blank = True , null = True)


    def __str__(self) :
        return str(
                    Users.objects.get(id = sender).username +
                    " Using Account " +
                    Account.objects.get(id = senders_account).account_no +
                    " sent " +
                    money_sent +
                    " to " +
                    Users.objects.get(id = receiver).username +
                    "'s account " +
                    Account.objects.get(id = receivers_account).account_no
                )
