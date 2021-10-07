from django.db import models



class Task(models.Model):
    STATUS = (
        ('Запланировано', 'Planned'),
        ('Выполнено', 'Completed'),
        ('Отменено', 'Canceled'),
    )

    exercise_text = models.CharField('Что надо сделать?', max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=300, choices = STATUS)

    def __str__(self):
        return self.exercise_text

    class Meta:
        verbose_name = 'дело'
        verbose_name_plural = 'дела'
