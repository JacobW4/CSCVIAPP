from django.db import models
from django.contrib.auth.models import User
from datetime import date


# Create your models here.


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    due_date = models.DateField(default=date.today)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    

    def days_til_due(self):
        today = date.today()
        if self.due_date is not None:
            return (self.due_date - today).days
        else:
            return None


    def __str__(self):
        days = self.days_til_due()

        if days is None:
            return f"{self.title} - Due date not set"
        elif days == 0:
            return f"{self.title} - Due today!"
        elif days == 1:
            return f"{self.title} - Due tomorrow"
        elif days > 0:
            return f"{self.title} - Due in {days} days"
        else:
            return f"{self.title} - Overdue by {-days} days"""

    
    
    
    
    #def __str__(self):
        #formatted_due_date = self.due_date.strftime("%Y-%m-%d")
        #return f"{self.title}- due: {formatted_due_date}"

    #def __str__(self):
        #return self.title
        

    class Meta:
        ordering = ['complete']



