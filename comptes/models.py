

# from django.contrib.auth.models import AbstractUser, BaseUserManager
# from django.db import models


# class UserManager(BaseUserManager):
#     def create_user(self, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError("L'utilisateur doit avoir un email")
#         email = self.normalize_email(email)
#         extra_fields.setdefault('username', email)

#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         extra_fields.setdefault('role', 'admin')

#         return self.create_user(email, password, **extra_fields)


# class User(AbstractUser):
#     username = models.CharField(max_length=150, blank=True)

#     prenom = models.CharField(max_length=150)
#     nom = models.CharField(max_length=60)
#     email = models.EmailField(unique=True)

#     telephone = models.CharField(max_length=30, blank=True, null=True)
#     date_naissance = models.DateTimeField(blank=True, null=True)

#     ROLE_CHOICES = (
#         ('admin', 'Admin'),
#         ('comptable', 'Comptable'),
#         ('medecin', 'Medecin'),
#     )
#     role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='student')
#     bio = models.TextField(blank=True)
#     photo = models.ImageField(upload_to='profils/', blank=True, null=True)

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []

#     objects = UserManager()

#     def __str__(self):
#         if self.prenom and self.nom:
#             return f"{self.prenom} {self.nom}"
#         return self.email


from django.db import models
from django.utils import timezone
from datetime import timedelta
from patient.models import Patient


class OTP(models.Model):
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name="otps"
    )

    code = models.CharField(max_length=6)

    created_at = models.DateTimeField(auto_now_add=True)

    expire_at = models.DateTimeField()

    is_used = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]

    def save(self, *args, **kwargs):
        if not self.expire_at:
            self.expire_at = timezone.now() + timedelta(minutes=5)

        super().save(*args, **kwargs)

    @property
    def is_valid(self):
        return (
            not self.is_used and
            timezone.now() <= self.expire_at
        )

    def __str__(self):
        return f"{self.patient.numero_patient} - {self.code}"
# # Create your models here.
