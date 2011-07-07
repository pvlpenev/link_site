from django.db import models

# Create your models here.

class link(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    url = models.CharField(max_length=200)

    def __unicode__(self):
        return self.title



