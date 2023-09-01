from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "onehux_test.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import onehux_test.users.signals  # noqa: F401
        except ImportError:
            pass
