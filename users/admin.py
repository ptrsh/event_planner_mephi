from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.forms import PasswordInput

from users.models import User

class UserCreationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        
    

    class Meta:
        model = User
        fields = ('email',)
        widgets = {
            'password': PasswordInput(),
        }

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    list_display = ("email",)
    ordering = ("email",)

    fieldsets = (
        (None, {'fields': ('password', 'last_login', 'is_superuser', 'groups', 'username', 'email', \
        'first_name', 'last_name', 'is_active', 'is_staff')}),
        )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password', 'first_name', 'last_name', 'is_superuser', 'is_staff', 'is_active')}
            ),
        )

    filter_horizontal = ()

admin.site.register(User, CustomUserAdmin)