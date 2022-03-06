from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.contrib.auth.validators import ASCIIUsernameValidator
from django.contrib.postgres.fields import CIEmailField
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class User(AbstractBaseUser, PermissionsMixin):
    username_validator = ASCIIUsernameValidator()

    first_name: models.CharField = models.CharField(
        _("first name"), max_length=150,
        blank=True
    )
    last_name: models.CharField = models.CharField(
        _("last name"), max_length=150,
        blank=True
    )
    email = CIEmailField(
        _("email address"),
        unique=True,
        error_messages={
            "unique": _("A user with that email address already exists."),
        },
    )

    # Date Of Creation
    doc: models.DateTimeField = models.DateTimeField(
        _("date joined"), default=timezone.now)

    objects: UserManager = UserManager()

    EMAIL_FIELD = "username"
    USERNAME_FIELD = "email"

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def clean(self) -> None:
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self) -> str:
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self) -> str:
        """Return the short name for the user."""
        return self.first_name

    def email_user(
            self, subject: str, message: str, from_email: str = None, **kwargs
    ) -> None:
        """
            Sends an email to the current user.
            Mimicks what send_mail(subject, message,
            from_email, [self.email], **kwargs)
            would do. Should you wish to add this
            functionality, do make sure to import
            send_mail from django.core.mail
        """
        print("Mail sent")
