from django.db import models
from common.models import CommonModel
# Create your models here.

# 오픈채팅방
class ChattingRoom(CommonModel):
    # Room Model Definition

    # Room에 DM을 보낸 Users
    users = models.ManyToManyField(
        to='users.User',
    )

    def __str__(self) -> str:
        return 'Chatting Room'

class Message(CommonModel):
    # Message Model Definition

    user = models.ForeignKey(
        to='users.User',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    text = models.TextField()

    room = models.ForeignKey(
        to='direct_messages.ChattingRoom',
        on_delete=models.CASCADE,
    )

    def __str__(self) -> str:
        return f'{self.user} says {self.text}'

