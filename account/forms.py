from django.contrib.auth.forms import UserCreationForm

from account.models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email', 'last_name', 'last_name', )
