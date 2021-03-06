from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)



class UserManager(BaseUserManager):
    def create_user(self, email, password=None):

        if not email:
            raise ValueError('Users must have an email address')

        if not password:
            raise ValueError('Users must have an email password')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email,
            password=password,
        )
        user.active= True
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    username    = models.CharField(max_length=14, unique=True)
    active      = models.BooleanField(default=False)
    staff       = models.BooleanField(default=False)
    admin       = models.BooleanField(default=False)
    last_login  = models.DateTimeField(auto_now=True)
    date_joined = models.DateField(auto_now_add=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def __str__(self):          
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
    
    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active
    
    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        obj = Connections.objects.filter(user=self)
        if len(obj)==0:
            Connections.objects.create(user=self)

    
class UserProfile(models.Model):

    user     = models.OneToOneField(User, on_delete=models.CASCADE, related_name ='profile')
    name     = models.CharField(max_length=30)
    dob      = models.DateField(blank=True, null=True)
    bio      = models.TextField(max_length=240, blank=True, null=True)
    picture  = models.ImageField(upload_to = 'profile/', blank = True, null = True, max_length = 1000)
    cover_pic= models.ImageField(upload_to= 'profile/cover/', blank=True, null=True, max_length=2000)
    location = models.CharField(max_length=30, blank=True, null=True)
    website  = models.URLField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

class OTP(models.Model):
    otp      = models.CharField(max_length = 6)
    email    = models.EmailField(max_length= 255)
    time     = models.IntegerField()
    reset    = models.BooleanField(default=False)
    def __str__(self):
        return self.email

class Connections(models.Model):
    user     = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user')
    follower = models.ManyToManyField(User, related_name='follower', blank=True)
    following= models.ManyToManyField(User, related_name='following', blank=True)

    def __str__(self):
        return self.user.username
    def username(self):
        return self.user.username

    class Meta:
        verbose_name = "Connection"
        verbose_name_plural = "Connections"

Notification_Category=( ('Text','Text'), ('Tweet', 'Tweet'),('Chat','Chat'))


class Notification(models.Model):
    user    = models.ForeignKey(User, on_delete=models.CASCADE)
    text    = models.TextField(max_length=500, blank=True, null=True)
    tweet_id= models.IntegerField(blank=True, null=True)
    extra_txt= models.TextField(blank=True, null=True)
    timestamp= models.DateTimeField(auto_now_add=True)
    category= models.CharField(choices=Notification_Category, max_length=30)
    seen    = models.BooleanField(default=False)
    def __str__(self):
        return str(self.user.username)+" --> "+self.category

    def username(self):
        return str(self.user.username)

class ChatConnection(models.Model):
    user    = models.OneToOneField(User, on_delete=models.CASCADE, related_name="status")
    status  = models.IntegerField(default=0)
    last_seen= models.DateTimeField(auto_now = True)
