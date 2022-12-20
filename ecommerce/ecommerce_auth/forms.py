from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django_registration.forms import RegistrationForm
from ecommerce.ecommerce_auth.models import User


class EcommerceRegistrationForm(RegistrationForm):
    class Meta(RegistrationForm.Meta):
        model = User
        fields = (
            "email",
            "first_name",
            "last_name",
        )

    def __init__(self, *args, **kwargs):
        super(EcommerceRegistrationForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.add_input(Submit("submit", "Register"))
