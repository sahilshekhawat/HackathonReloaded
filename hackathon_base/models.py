from django.db import models


class ProcessInfo(models.Model):
    process_info = models.TextField(editable=True)
    SystemInfo = models.TextField(editable=True)