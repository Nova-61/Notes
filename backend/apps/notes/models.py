from django.db import models
from django.core.validators import MaxLengthValidator
# Create your models here.

class Note(models.Model):
    title = models.CharField(max_length=200, verbose_name='Title',
                             help_text='Enter the title of the note',)
    content = models.TextField(validators = [MaxLengthValidator(10000)],
                               verbose_name='Content',
                               help_text='Enter the content of the note',)
    created_at = models.DateTimeField(
        auto_now_add=True, 
        verbose_name='Created At')
    updated_at = models.DateTimeField(
        auto_now=True, 
        verbose_name='Updated At')
    
    class Meta:
        verbose_name = 'Note'
        verbose_name_plural = 'Notes'
        ordering = ['-created_at']

    def __str__(self):
        return self.title[:50] 