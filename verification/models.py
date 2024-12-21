from django.db import models

class Verification(models.Model):
    registration_number = models.CharField(max_length=20, unique=True)
    scanned_data = models.TextField(blank=True, null=True)
    verified_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.registration_number
