from django.db import models

class Verification(models.Model):
    registration_number = models.CharField(max_length=100)
    id_front = models.ImageField(upload_to='verification/id_front/' ,default='')
    id_back = models.ImageField(upload_to='verification/id_back/' ,default='')
    real_time_photo = models.ImageField(upload_to='verification/real_time_photo/', default='')

    def __str__(self):
        return self.registration_number
