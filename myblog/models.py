from django.db import models

# Create your models here.
class blogpost(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    def __unicode__(self):
        return self.title
    
