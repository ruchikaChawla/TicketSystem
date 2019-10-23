from django.db import models


class Ticket(models.Model):
    name = models.CharField(max_length=255, default='')
    phone_no = models.IntegerField(default='')
    email = models.EmailField(max_length=255, default='')
    issue_type = models.CharField(max_length=255, default='')
    status = models.CharField(max_length=255, default='')
    description = models.TextField(default='')
    # date_time = models.DateTimeField(auto_now_add=True, blank=True)
    # slug = models.SlugField(blank=True, default='')

#
# class Comments(models.Model):
#     ticket_id = models.ForeignKey()
#     description = models.TextField(default='')
#     # date_time = models.DateTimeField(auto_now_add=True, blank=True)
#     # slug = models.SlugField(blank=True, default='')

    def __str__(self):
        return self.name

