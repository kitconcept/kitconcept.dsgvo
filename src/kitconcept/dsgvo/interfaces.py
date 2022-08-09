"""Module where all interfaces, events and exceptions live."""

from kitconcept.dsgvo import _
from zope import schema
from zope.interface import Interface
from zope.interface import Invalid
from zope.publisher.interfaces.browser import IDefaultBrowserLayer


def validateAccept(value):
    if value is not True:
        raise Invalid(
            _(
                "label_dsgvo_accept_invalid",
                default=(
                    "Bitte akzeptieren sie die Datenschutzerklärung und "
                    "Widerrufhinweise."
                ),
            )
        )
    return True


class IKitconceptDsgvoLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class IDsgvoUserDataSchema(Interface):

    dsgvo_accept = schema.Bool(
        title=_(
            "label_dsgvo_mailchimp_accept",
            default=(
                'Ich habe die <a href="${portal_url}/datenschutz" '
                'target="_blank">'
                "Datenschutzerklärung und Widerrufhinweise</a> "
                "gelesen und akzeptiere diese."
            ),
        ),
        description=_("help_dsgvo_accept", default=""),
        required=True,
        constraint=validateAccept,
    )
