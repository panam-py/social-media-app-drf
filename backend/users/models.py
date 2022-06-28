from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import gettext_lazy as _
from django.contrib.postgres.fields import ArrayField
from django.conf import settings


from .modelmanagers import UserManager


# Create your models here.
class Reaction(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    reaction_source = models.CharField(max_length=200)
    reaction_type = models.CharField(max_length=20)
    reaction_time = models.DateTimeField(auto_now_add=True)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(_("username"), max_length=200)
    first_name = models.CharField(_("first name"), max_length=30, blank=False)
    last_name = models.CharField(_("last name"), max_length=30, blank=False)
    date_created = models.DateTimeField(_("date created"), auto_now_add=True)
    is_active = models.BooleanField(_("active"), default=True)
    profile_pic = models.CharField(_("profile picture"), default='', max_length=2000)
    reactions = ArrayField(base_field=models.CharField(max_length=2000))

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
