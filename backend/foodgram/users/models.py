from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Subscription(models.Model):
    subscriber = models.ForeignKey(User, on_delete=models.CASCADE,
                                   related_name='subscriptions', verbose_name='Подписчик')
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='subscribers', verbose_name='Автор')

    class Meta:
        verbose_name = 'подписка'
        verbose_name_plural = 'Подписки'
        constraints = (
            models.CheckConstraint(check=~models.Q(
                subscriber=models.F('author')), name='no_self_subscribe'),
            models.UniqueConstraint(
                fields=('subscriber', 'author'), name='unique_subscription')
        )

    def __str__(self):
        return f'Подписка {self.subscriber} на {self.author}'
