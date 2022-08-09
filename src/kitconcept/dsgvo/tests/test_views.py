from kitconcept.dsgvo.interfaces import IKitconceptDsgvoLayer
from kitconcept.dsgvo.testing import KITCONCEPT_DSGVO_INTEGRATION_TESTING  # noqa
from plone import api
from zope.interface import alsoProvides

import unittest


try:
    from Products.CMFPlone.factory import _IMREALLYPLONE5  # noqa
except ImportError:
    PLONE5 = False
else:
    PLONE5 = True


@unittest.skipIf(not PLONE5, "Just Plone 5 currently.")
class ExportUsersTestCase(unittest.TestCase):

    layer = KITCONCEPT_DSGVO_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        self.request = self.layer["request"]
        alsoProvides(self.request, IKitconceptDsgvoLayer)
        self.view = api.content.get_view("export-users", self.portal, self.request)

    def test_export_users(self):
        api.user.create(
            email="user@plone.org", username="user", properties={"fullname": "User"}
        )
        self.assertEqual("Name,Email\r\n,\r\nUser,user@plone.org\r\n", self.view())

    def test_export_users_empty(self):
        self.assertEqual("Name,Email\r\n,\r\n", self.view())
