from logging import PlaceHolder
from socket import fromshare
from tkinter.ttk import Widget
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from.models import fire_report,add_team

class Loginform(AuthenticationForm):
    username=forms.CharField(max_length=50,widget=forms.TextInput(attrs={"class":"form-control","placeholder":"admin"}))
    password=forms.CharField(max_length=50,widget=forms.TextInput(attrs={"class":"form-control","placeholder":"admin"}))
  

class fire_reports(forms.ModelForm):
    class Meta:
        model=fire_report
        fields=["name","mobile","location","message"]
        widgets={
            "name":forms.TextInput(attrs={"class":"form-control"}),
            "mobile":forms.TextInput(attrs={"class":"form-control"}),
            "location":forms.TextInput(attrs={"class":"form-control"}),
            "message":forms.TextInput(attrs={"class":"form-control"})
        }

class ADD_team(forms.ModelForm):
    class Meta:
        model=add_team
        fields=["team_name","team_lead","lead_number","team_member"]
        widgets={
            "team_name":forms.TextInput(attrs={"class":"form-control"}),
            "team_lead":forms.TextInput(attrs={"class":"form-control"}),
            "lead_number":forms.TextInput(attrs={"class":"form-control"}),
            "team_member":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter team member using comma"})

        }