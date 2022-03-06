from rest_framework.authtoken.models import Token
# from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model


#  settings.AUTH_USER_MODEL
user_model = get_user_model()


@receiver(post_save, sender=user_model)
def create_auth_token(
    sender,
    instance=None,
    created: bool = False,
    **kwargs
) -> None:
    # The below function catches User's post_save
    # signal and auto generate an authentication token
    if created:
        Token.objects.create(user=instance)
