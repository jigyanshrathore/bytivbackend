from django.db import models

STATUS_CHOICES = [
    ('pending', 'Pending'),
    ('in-progress', 'In Progress'),
    ('completed', 'Completed'),
]

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return self.title
