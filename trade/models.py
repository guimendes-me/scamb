from django.db import models

# Create your models here.


from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars', null=True, blank=True)
    bio = models.TextField(max_length=500, null=True, blank=True)
    ra = models.CharField(max_length=10, null=True, blank=True)
    etec = models.CharField(max_length=30, null=True, blank=True)
    course = models.CharField(max_length=15, null=True, blank=True)
    whats = models.IntegerField(null=True, blank=True)

    def __int__(self):
       return self.user


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()



class Trade(models.Model):

    title = models.CharField(max_length=30)
    subtitle = models.CharField(max_length=50)
    description = models.CharField(max_length=1500,null=True, blank=True)
    condition = models.CharField(max_length=20, null=True, blank=True)
    mainimg = models.ImageField(upload_to='trades', null=True, blank=True)
    secondimg = models.ImageField(upload_to='trades', null=True, blank=True)
    thirdimg = models.ImageField(upload_to='trades', null=True, blank=True)

    interest = models.CharField(max_length=70, null=True, blank=True)
    subinterest = models.CharField(max_length=100, null=True, blank=True)
    interestdetails = models.CharField(max_length=1200, null=True, blank=True)
    interestimg= models.ImageField(upload_to='trades', null=True, blank=True)

    fk_profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True, default=3)


    def __str__(self):
       return self.title + '-'+  self.subtitle