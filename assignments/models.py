from django.db import models

# Create your models here.
class About(models.Model):
    tilte = models.CharField(max_length=25)
    description = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.tilte
    
    class Meta:
        verbose_name_plural='about'
    

class SocialConnect(models.Model):
    platform = models.CharField(max_length=25)
    link = models.URLField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'social-connections'

    def __str__(self):
        return self.platform
