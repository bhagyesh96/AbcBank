# from django.contrib.auth.models import BaseUserManager

# class UserManager(BaseUserManager):
#     def create_user(self, email,contact_number,password=None):
#         """
#         Creates and saves a User with the given email, date of
#         birth and password.
#         """
#         if not email:
#             raise ValueError('Users must have an email address')

#         user = self.model(
#             email=self.normalize_email(email),
#             contact_number=contact_number
#         )

#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, contact_number,password=None):
        
#         user = self.create_user(
#             email,
#             password=password,
#             contact_number=contact_number
#         )
#         user.is_admin = True
#         user.save(using=self._db)
#         return user
