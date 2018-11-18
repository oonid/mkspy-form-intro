from django.db import models
# from django.forms import ModelForm, modelform_factory

# Create your models here.


class Friend(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    SEX_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)

    def __str__(self):
        return '{} ({})'.format(self.name, self.sex)


# we don't need to declare Form manually, we will generate with modelform_factory(Friend, fields=('name', 'age', 'sex'))
# check the sample code on views.py
#
# class FriendForm(ModelForm):
#     class Meta:
#         model = Friend
#         fields = ['name', 'age', 'sex']
