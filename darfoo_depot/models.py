from django.db import models

# Create your models here.

class Darfooplugin(models.Model):
    packageUrl = models.URLField()
    picUrl = models.URLField()
    packageName = models.CharField(max_length=133, unique=True)
    className = models.CharField(max_length=133)

    def __unicode__(self):
        return self.packageName

    class Meta:
        db_table = 'darfooplugin'

class Custom(models.Model):
    packageName = models.CharField(max_length=133, unique=True)
    width = models.IntegerField()
    height = models.IntegerField()
    leftMargin = models.IntegerField()
    topMargin = models.IntegerField()

    def __unicode__(self):
        return self.packageName

    class Meta:
	db_table = 'custom'

class Settings(models.Model):
    settings = models.TextField()
    flag = models.CharField(max_length=33, unique=True)

    def __unicode__(self):
        return self.id

    class Meta:
        db_table = 'settings'
