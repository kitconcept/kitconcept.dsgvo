"""Setup tests for this package."""
from kitconcept.dsgvo.testing import KITCONCEPT_DSGVO_INTEGRATION_TESTING
from Products.CMFPlone.utils import get_installer

import unittest


class TestSetup(unittest.TestCase):
    """Test that kitconcept.dsgvo is properly installed."""

    layer = KITCONCEPT_DSGVO_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        self.installer = get_installer(self.portal, self.layer["request"])

    def test_product_installed(self):
        """Test if kitconcept.dsgvo is installed."""
        self.assertTrue(self.installer.is_product_installed("kitconcept.dsgvo"))

    def test_browserlayer(self):
        """Test that IKitconceptDsgvoLayer is registered."""
        from kitconcept.dsgvo.interfaces import IKitconceptDsgvoLayer
        from plone.browserlayer import utils

        self.assertIn(IKitconceptDsgvoLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = KITCONCEPT_DSGVO_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        self.installer = get_installer(self.portal, self.layer["request"])
        self.installer.uninstall_product("kitconcept.dsgvo")

    def test_product_uninstalled(self):
        """Test if kitconcept.dsgvo is cleanly uninstalled."""
        self.assertFalse(self.installer.is_product_installed("kitconcept.dsgvo"))

    def test_browserlayer_removed(self):
        """Test that IKitconceptDsgvoLayer is removed."""
        from kitconcept.dsgvo.interfaces import IKitconceptDsgvoLayer
        from plone.browserlayer import utils

        self.assertNotIn(IKitconceptDsgvoLayer, utils.registered_layers())
