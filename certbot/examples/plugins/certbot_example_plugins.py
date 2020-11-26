"""Example Certbot plugins.

For full examples, see `certbot.plugins`.

"""

import logging
# test commit
import zope.interface

from certbot import interfaces
from certbot.plugins import common
from certbot.plugins import dns_common

logger = logging.getLogger(__name__)

@zope.interface.implementer(interfaces.IAuthenticator)
@zope.interface.provider(interfaces.IPluginFactory)
class Authenticator(dns_common.DNSAuthenticator):
    """Example Authenticator."""

    description = "Example Authenticator plugin"

    # Implement all methods from IAuthenticator, remembering to add
    # "self" as first argument, e.g. def prepare(self)...
    def __init__(self, *args, **kwargs):
        super(Authenticator, self).__init__(*args, **kwargs)
        self.credentials = None

    @classmethod
    def add_parser_arguments(cls, add):  # pylint: disable=arguments-differ
        #print('emi emi emi emi emi emi emi emi emi emi emi')
        super(Authenticator, cls).add_parser_arguments(
            add, default_propagation_seconds=120
        )
        add("credentials", help="ISPConfig credentials INI file.")

    def _setup_credentials(self):
        self.credentials = self._configure_credentials(
            "credentials",
            "ISPConfig credentials INI file",
            {
                "endpoint": "entorno.es",
                "username": "emiprueba",
                "password": "emipassword",
            },
        )

    def more_info(self):  # pylint: disable=missing-docstring,no-self-use
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
