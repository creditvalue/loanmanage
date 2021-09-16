from django.contrib.auth.base_user import BaseUserManager

# class manager here 
class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, mobile, password=None , **extra_fields):
        if not mobile:
            raise ValueError('email is require')

        user = self.model(mobile = mobile , **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

     
    def create_superuser(self, mobile , password, **extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)

        return self.create_user(mobile , password , **extra_fields)