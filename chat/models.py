from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Contact(models.Model):
    user = models.ForeignKey(User,  on_delete=models.CASCADE,
                             related_name='friends',
                             help_text="A unique integer value identifying this user.")
    friends = models.ManyToManyField('self', blank=True)

    def __str__(self):
        return self.user.username


class Message(models.Model):
    contact = models.ForeignKey(Contact,  on_delete=models.CASCADE,
                                related_name='messages',
                                help_text="ID of participant")
    content = models.TextField(help_text="String of message")
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return"({}) {}".format(
            self.contact.user.username,
            self.content
        )

    class Meta:
        verbose_name = 'správa'
        verbose_name_plural = 'správy'


class Chat(models.Model):
    """
    Virtual chat room including participant and theirs messages.
    """
    participants = models.ManyToManyField(Contact, related_name='chats', help_text="List of participant ids", blank=True)
    messages = models.ManyToManyField(Message, blank=True, help_text="List of message ids",)

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = 'Chat'
        # verbose_name_plural = 'chaty'
        app_label = 'chat'