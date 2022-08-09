from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import kitconcept.dsgvo


class KitconceptDsgvoLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=kitconcept.dsgvo)

    def setUpPloneSite(self, portal):
        applyProfile(portal, "kitconcept.dsgvo:default")


KITCONCEPT_DSGVO_FIXTURE = KitconceptDsgvoLayer()


KITCONCEPT_DSGVO_INTEGRATION_TESTING = IntegrationTesting(
    bases=(KITCONCEPT_DSGVO_FIXTURE,), name="KitconceptDsgvoLayer:IntegrationTesting"
)


KITCONCEPT_DSGVO_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(KITCONCEPT_DSGVO_FIXTURE, z2.ZSERVER_FIXTURE),
    name="KitconceptDsgvoLayer:FunctionalTesting",
)


KITCONCEPT_DSGVO_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(KITCONCEPT_DSGVO_FIXTURE, REMOTE_LIBRARY_BUNDLE_FIXTURE, z2.ZSERVER_FIXTURE),
    name="KitconceptDsgvoLayer:AcceptanceTesting",
)
