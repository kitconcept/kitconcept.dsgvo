from kitconcept.dsgvo.interfaces import IDsgvoUserDataSchema
from kitconcept.dsgvo.interfaces import IKitconceptDsgvoLayer
from kitconcept.dsgvo.widget import DsgvoSingleCheckBoxFieldWidget
from plone.app.users.browser.account import AccountPanelSchemaAdapter
from plone.app.users.browser.register import AddUserForm
from plone.app.users.browser.register import RegistrationForm
from plone.app.users.browser.userdatapanel import UserDataPanel
from plone.z3cform.fieldsets import extensible
from z3c.form import field
from zope.component import adapts
from zope.interface import Interface


class DsgvoUserDataSchemaAdapter(AccountPanelSchemaAdapter):
    schema = IDsgvoUserDataSchema


class UserDataPanelExtender(extensible.FormExtender):
    adapts(Interface, IKitconceptDsgvoLayer, UserDataPanel)

    def update(self):
        fields = field.Fields(IDsgvoUserDataSchema)
        # Users have already accepted.
        fields = fields.omit("dsgvo_accept")
        self.add(fields)


class RegistrationPanelExtender(extensible.FormExtender):
    adapts(Interface, IKitconceptDsgvoLayer, RegistrationForm)

    def update(self):
        fields = field.Fields(IDsgvoUserDataSchema)
        fields["dsgvo_accept"].widgetFactory = DsgvoSingleCheckBoxFieldWidget
        self.add(fields)


class AddUserFormExtender(extensible.FormExtender):
    adapts(Interface, IKitconceptDsgvoLayer, AddUserForm)

    def update(self):
        fields = field.Fields(IDsgvoUserDataSchema)
        # management form doesn't need this field
        fields = fields.omit("dsgvo_accept")
        self.add(fields)
