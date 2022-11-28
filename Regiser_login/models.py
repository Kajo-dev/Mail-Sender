from django.db import models
from django.contrib.auth.models import BaseUserManager,PermissionsMixin,AbstractBaseUser

class UserManago(BaseUserManager):
    def create_user(self,email,firstname,lastname,password,**kw):
        user = self.model(
            email = self.normalize_email(email),
            firstname = firstname,
            lastname = lastname,
            **kw
        )

        user.set_password(password)
        user.save(using=self.db)

        return user

    def create_normal_user(self,email,password,firstname,lastname,**kw):
        kw.setdefault('is_superuser',False)
        kw.setdefault('is_staff',True)

        return self.create_user(email,password,firstname,lastname,**kw)

    def create_superuser(self,email,password,firstname,lastname,**kw):
        kw.setdefault('is_staff',True)
        kw.setdefault('is_superuser',True)

        return self.create_user(email,password,firstname,lastname,**kw)


class User(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(db_index=True,unique=True,max_length=100)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)

    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = UserManago()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firstname,lastname,password']

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'