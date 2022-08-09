from kitconcept.dsgvo import _
from kitconcept.dsgvo.interfaces import IKitconceptDsgvoLayer
from kitconcept.dsgvo.widget import DsgvoSingleCheckBoxFieldWidget
from plone.supermodel import model
from plone.z3cform.fieldsets import extensible
from Products.CMFPlone.browser.contact_info import ContactForm
from z3c.form import field
from zope import schema
from zope.component import adapts
from zope.interface import Interface


class IDsgvoContactInfoSchema(model.Schema):

    dsgvo_contact_info_text = schema.Bool(
        title=_(
            "label_dsgvo_info",
            default=(
                "Ihre Anfrage wird verschlüsselt per https an unseren "
                "Server geschickt. Sie erklären sich damit einverstanden, "
                "dass wir die Angaben zur Beantwortung Ihrer Anfrage "
                "verwenden dürfen. Hier finden Sie unsere "
                '<a href="${portal_url}/datenschutz" '
                'target="_blank">Datenschutzerklärung '
                "und Widerrufhinweise</a>."
            ),
        ),
        description=_("help_dsgvo_info", default=""),
        default=True,
    )


class ContactFormExtender(extensible.FormExtender):
    adapts(Interface, IKitconceptDsgvoLayer, ContactForm)

    def update(self):
        fields = field.Fields(IDsgvoContactInfoSchema)
        fields["dsgvo_contact_info_text"].widgetFactory = DsgvoSingleCheckBoxFieldWidget
        self.add(fields)
