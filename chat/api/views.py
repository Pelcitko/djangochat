from django.contrib.auth import get_user_model
from rest_framework import permissions, documentation

from chat.models import Chat, Contact
from chat.views import get_user_contact
from .serializers import ChatSerializer
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    DestroyAPIView,
    UpdateAPIView, GenericAPIView
)

User = get_user_model()


class ChatListView(ListAPIView):
    """
    Return a list of all existing chats ids with participants and message ids.
    """
    serializer_class = ChatSerializer
    permission_classes = (permissions.AllowAny, )

    def get_queryset(self):
        queryset = Chat.objects.all()
        username = self.request.query_params.get('username', None)
        if username is not None:
            contact = get_user_contact(username)
            queryset = contact.chats.all()
        return queryset


# class ChatGenericView(GenericAPIView):
#     """
#     get: Return **chat** by id. ...
#     """
#     queryset = Chat.objects.all()
#     serializer_class = ChatSerializer


class ChatDetailView(RetrieveAPIView):
    """
    Return **chat** by id.
    """
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = (permissions.AllowAny, )
    # api_chat = reverse_lazy('ChatDetailView', request=request)


class ChatCreateView(CreateAPIView):
    """
    Create **new chat** with new id and participants.
    """
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = (permissions.IsAuthenticated, )


class ChatUpdateView(UpdateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = (permissions.IsAuthenticated, )


class ChatDeleteView(DestroyAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = (permissions.IsAuthenticated, )
