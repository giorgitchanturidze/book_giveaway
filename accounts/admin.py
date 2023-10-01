from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.core.exceptions import ValidationError

from .models import Account


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Password confirmation", widget=forms.PasswordInput
    )

    class Meta:
        model = Account
        fields = ["email"]
    
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password1 = forms.CharField(required=False, label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(
        required=False, label="Password confirmation", widget=forms.PasswordInput
    )
    
    class Meta:
        model = Account
        fields = ["email", "first_name", "password1",'password2', "is_active", "is_admin"]
        
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2
    
    def save(self, commit=True):
        user = super().save(commit=False)
        if self.cleaned_data['password1'] and self.cleaned_data['password2']:
            user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ["email", 'first_name', 'last_name', "is_admin"]
    list_filter = ["is_admin"]
    fieldsets = [
        ('User Information', {"fields": ["email", 'first_name', 'last_name']}),
        ("Permissions", {"fields": ['is_staff', "is_admin", 'is_superadmin']}),
        ("Change Password", {"fields": ['password1', "password2"]}),
    ]

    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["email", "password1", "password2"],
            },
        ),
    ]
    search_fields = ["email"]
    ordering = ["email"]
    filter_horizontal = []

admin.site.register(Account, UserAdmin)
admin.site.unregister(Group)