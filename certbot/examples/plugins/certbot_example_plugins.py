"""Example Certbot plugins.

For full examples, see `certbot.plugins`.

"""
import zope.interface

from certbot import interfaces
from certbot.plugins import common


@zope.interface.implementer(interfaces.IAuthenticator)
@zope.interface.provider(interfaces.IPluginFactory)
class Authenticator(common.Plugin):
    """Example Authenticator."""

    description = "Example Authenticator plugin"

    # Implement all methods from IAuthenticator, remembering to add
    # "self" as first argument, e.g. def prepare(self)...
    def __init__(self, *args, **kwargs):
        super(Authenticator, self).__init__(*args, **kwargs)
        self.credentials = None

    @classmethod
    def more_info(self):  # pylint: disable=missing-docstring,no-self-use
        return (
            "This plugin configures a DNS TXT record to respond to a dns-01 challenge using "
            + "the EuroDNS Remote REST API."
        )

    def prepare(self):  # pylint: disable=missing-docstring,no-self-use
        return (
            "This plugin configures a DNS TXT record to respond to a dns-01 challenge using "
            + "the EuroDNS Remote REST API."
        )

    def get_chall_pref(self,domain):  # pylint: disable=missing-docstring,no-self-use
        return (
            "This plugin configures a DNS TXT record to respond to a dns-01 challenge using "
            + "the EuroDNS Remote REST API."
        )

    def perform(self,achalls):  # pylint: disable=missing-docstring,no-self-use
        return (
            "This plugin configures a DNS TXT record to respond to a dns-01 challenge using "
            + "the EuroDNS Remote REST API."
        )

    def cleanup(self,achalls):  # pylint: disable=missing-docstring,no-self-use
        return (
            "This plugin configures a DNS TXT record to respond to a dns-01 challenge using "
            + "the EuroDNS Remote REST API."
        )


@zope.interface.implementer(interfaces.IInstaller)
@zope.interface.provider(interfaces.IPluginFactory)
class Installer(common.Plugin):
    """Example Installer."""

    description = "Example Installer plugin"

    # Implement all methods from IInstaller, remembering to add
    # "self" as first argument, e.g. def get_all_names(self)...
