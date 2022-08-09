from kitconcept.dsgvo import _
from kitconcept.dsgvo.util import dsgvo_translate
from plone.app.form.widgets.checkboxwidget import CheckBoxWidget
from plone.app.users.browser.personalpreferences import UserDataConfiglet
from plone.app.users.browser.personalpreferences import UserDataPanel
from plone.app.users.browser.personalpreferences import UserDataPanelAdapter
from plone.app.users.browser.register import RegistrationForm
from plone.app.users.userdataschema import IUserDataSchema
from plone.app.users.userdataschema import IUserDataSchemaProvider
from zope import schema
from zope.i18nmessageid import Message
from zope.interface import implementer


class DsgvoCheckboxWidget(CheckBoxWidget):
    def __call__(self):
        if isinstance(self.context.title, Message):
            self.context.title = dsgvo_translate(self.context.title, self.request)
        return super().__call__()


class InvalidAccept(schema.ValidationError):

    __doc__ = _(
        "label_dsgvo_accept_invalid",
        default=(
            "Bitte akzeptieren sie die Datenschutzerklärung und " "Widerrufhinweise."
        ),
    )


def validateAccept(value):
    if value is not True:
        raise InvalidAccept()
    return True


class IDsgvoP4UserDataSchema(IUserDataSchema):
    """
    Combined fields
    """

    dsgvo_accept = schema.Bool(
        title=_(
            "label_dsgvo_accept",
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


@implementer(IUserDataSchemaProvider)
class EnhancedUserDataSchemaProvider:
    def getSchema(self):
        """"""
        return IDsgvoP4UserDataSchema


class EnhancedRegistrationForm(RegistrationForm):
    def __init__(self, context, request):
        super().__init__(context, request)

    @property
    def form_fields(self):
        """
        form_fields in the registration form is a property. We cannot
        modify self.form_fields.
        """
        form_fields = super().form_fields
        form_fields["dsgvo_accept"].custom_widget = DsgvoCheckboxWidget
        return form_fields


class DsgvoP4UserDataSchemaAdapter(UserDataPanelAdapter):
    def get_dsgvo_accept(self):
        return self.context.getProperty("dsgvo_accept", "")

    def set_dsgvo_accept(self, value):
        return self.context.setMemberProperties({"dsgvo_accept": value})

    dsgvo_accept = property(get_dsgvo_accept, set_dsgvo_accept)


class DsgvoUserDataPanel(UserDataPanel):
    def __init__(self, context, request):
        super().__init__(context, request)
        self.form_fields = self.form_fields.omit("dsgvo_accept")


class DsgvoUserDataConfiglet(UserDataConfiglet):
    def __init__(self, context, request):
        super().__init__(context, request)
        self.form_fields = self.form_fields.omit("dsgvo_accept")
