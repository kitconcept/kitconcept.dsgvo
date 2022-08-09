from Products.CMFPlone.utils import safe_unicode


try:
    from cgi import escape
except ImportError:
    from html import escape

from plone import api
from zope.component import getMultiAdapter
from zope.i18n import translate
from zope.i18nmessageid import Message


def dsgvo_translate(message, request):
    """
    translate the message and interpolate ${site_title} and ${portal_url}
    """
    portal = api.portal.get()
    portal_state = getMultiAdapter((portal, request), name="plone_portal_state")
    site_title = escape(safe_unicode(portal_state.navigation_root_title()))
    portal_url = portal_state.portal_url()

    # interpolation does not work if we pass the mapping to
    # zope.i18n.translate(). We have to construct a new message with
    # a mapping.
    # See https://github.com/zopefoundation/zope.i18n/issues/9
    translation = translate(
        Message(message, mapping={"portal_url": portal_url, "site_title": site_title}),
        context=request,
    )
    return translation
