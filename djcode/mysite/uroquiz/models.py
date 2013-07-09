# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class Uroquiz(models.Model):
    q_num = models.IntegerField(null=True, blank=True)
    question = models.TextField(blank=True)
    a = models.CharField(max_length=255, blank=True)
    b = models.CharField(max_length=255, blank=True)
    c = models.CharField(max_length=255, blank=True)
    d = models.CharField(max_length=255, blank=True)
    e = models.CharField(max_length=255, blank=True)
    answer = models.CharField(max_length=255, blank=True)
    exp = models.TextField(blank=True)
    area = models.CharField(max_length=255, blank=True)
    cat = models.CharField(max_length=255, blank=True)
    image = models.CharField(max_length=255, blank=True)
    year = models.IntegerField(null=True, blank=True)
    number = models.IntegerField(primary_key=True)
    subject_num = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'uroquiz'

