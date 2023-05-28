from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Subscription(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='subscriber',
        verbose_name='Подписчик',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
        verbose_name='Автор',
    )

    class Meta:
        verbose_name = 'подписка'
        verbose_name_plural = 'подписки'
        constraints = (
            models.CheckConstraint(
                check=~models.Q(user=models.F('author')),
                name='no_self_following'
            ),
            models.UniqueConstraint(
                fields=('user', 'author'),
                name='unique_subscription'
            )
        )

    def __str__(self):
        return f'{self.user} подписан на {self.author}'
