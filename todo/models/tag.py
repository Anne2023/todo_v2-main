from django.db import models
from .task import TaskEntity

class TagEntity(models.Model):
  name = models.CharField(max_length=64)
  tasks = models.ManyToManyField(TaskEntity,
                                 related_name='tags',
                                 blank=True,
                                 through='TaskTagEntity')
  
  def __str__(self) -> str:
    return "Tag [%i - %s]" % (self.id, self.name)
