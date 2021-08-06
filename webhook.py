import requests
from django import forms
from django.utils.translation import gettext_lazy as _
from weblate.addons.base import BaseAddon
from weblate.addons.forms import BaseAddonForm
from weblate.addons.events import EVENT_POST_ADD

class WebhookAddonForm(BaseAddonForm):
    url = forms.CharField(
        label=_("URL"),
        required=True,
        help_text=_(
            "This URL is called whenever a translation is changed."
        ),
    )

class WebhookAddon(BaseAddon):
    events = (EVENT_POST_ADD,)
    name = "weblate.webhook"
    # Verbose name and long descrption
    verbose = _("Call a webhook after translation is added.")
    description = _("TODO")
    settings_form = WebhookAddonForm
    
    def post_add(self, translation):
        url = self.instance.configuration.get("url")
        requests.post(url, data=translation)
