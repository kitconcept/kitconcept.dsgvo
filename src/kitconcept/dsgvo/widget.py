from kitconcept.dsgvo.interfaces import IKitconceptDsgvoLayer
from kitconcept.dsgvo.util import dsgvo_translate
from z3c.form.browser.checkbox import SingleCheckBoxWidget
from z3c.form.interfaces import IFieldWidget
from z3c.form.interfaces import ISingleCheckBoxWidget
from z3c.form.widget import FieldWidget
from zope.component import adapter
from zope.interface import implementer
from zope.interface import implementer_only
from zope.schema.interfaces import IBool


class IDsgvoSingleCheckBoxWidget(ISingleCheckBoxWidget):
    """Marker interface for the SingleCheckboxBoolWidget."""


@implementer_only(IDsgvoSingleCheckBoxWidget)
class DsgvoSingleCheckBoxWidget(SingleCheckBoxWidget):
    """
    Single Input type checkbox widget implementation that renders
    html in the label and help and interpolates the portal url and
    site name
    """

    klass = "dsgvo-single-checkbox-widget"

    @property
    def label(self):
        return getattr(self, "_label", "")

    @label.setter
    def label(self, value):
        self._label = dsgvo_translate(value, self.request)

    @property
    def description(self):
        return getattr(self, "_description", "")

    @description.setter
    def description(self, value):
        self._description = dsgvo_translate(value, self.request)


@adapter(IBool, IKitconceptDsgvoLayer)
@implementer(IFieldWidget)
def DsgvoSingleCheckBoxFieldWidget(field, request):
    """IFieldWidget factory for CheckBoxWidget."""
    return FieldWidget(field, DsgvoSingleCheckBoxWidget(request))
