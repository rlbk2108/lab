from django.db import models



class Profile(models.Model):
    STATUS = (
        ('Planned', 'Запланировано'),
        ('Completed', 'Выполнено'),
        ('Canceled', 'Отменено'),
    )
    status = models.CharField(max_length=300, choices = STATUS)


class Exercise(models.Model):
    exercise_text = models.CharField('Что надо сделать?', max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    STATUS = (
        ('Planned', 'Запланировано'),
        ('Completed', 'Выполнено'),
        ('Canceled', 'Отменено'),
    )
    status = models.CharField(max_length=300, choices = STATUS)

    def __str__(self):
        return self.exercise_text



