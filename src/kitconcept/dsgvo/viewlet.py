"""
A viewlet rendering a dsgvo information banner
"""

from kitconcept.dsgvo import _
from kitconcept.dsgvo.util import dsgvo_translate
from plone import api
from plone.app.layout.viewlets import common as base


class DsgvoViewlet(base.ViewletBase):
    """
    A viewlet to render a dsgvo information banner
    """

    def info(self):
        msg = _(
            "dsgvo_info_banner",
            default=(
                "Um unsere Webseite für Sie optimal zu gestalten und "
                "fortlaufend verbessern zu können, verwenden wir Cookies. "
                "Durch die weitere Nutzung der Webseite stimmen Sie der "
                "Verwendung von Cookies zu. Weitere Informationen zu "
                "Cookies erhalten Sie in unserer "
                '<a href="${portal_url}/datenschutz" target="_blank">'
                "Datenschutzerklärung</a>."
            ),
        )
        return dsgvo_translate(msg, self.request)

    def portal_url(self):
        return api.portal.get().absolute_url()

    # def render(self):
    #     cookie = self.request.cookies.get('hide-dsgvo-banner', False)
    #     if cookie:
    #         return ''
    #     return super(DsgvoViewlet, self).render()
