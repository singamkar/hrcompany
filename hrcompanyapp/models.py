
# from django.db import models

# class Appointment(models.Model):
    
#     # Full name
#     name = models.CharField(max_length=100)

#     # Email address
#     email = models.EmailField()

#     # Phone number
#     phone = models.CharField(max_length=15)

#     # Address
#     address = models.TextField()

#     # Appointment date
#     date = models.DateField()

#     # Appointment time (hour and minutes)
#     time = models.TimeField()

#     # AM/PM selection
#     am_pm = models.CharField(max_length=2, choices=[('AM', 'AM'), ('PM', 'PM')])

#     def __str__(self):
#         return f"{self.name} - {self.date} at {self.time} {self.am_pm}"




# class Contact(models.Model):
#     name = models.CharField(max_length=255)
#     email = models.EmailField()
#     subject = models.CharField(max_length=255)
#     message = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.subject

