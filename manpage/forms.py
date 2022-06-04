# -*- coding: utf-8 -*-

from django import forms
from django.core.mail import EmailMessage

class ContactForm(forms.Form):
    name = forms.CharField(label='Name')
    email = forms.EmailField(label='Email Address')
    title = forms.CharField(label='Subject')
    message = forms.CharField(label='Message', widget=forms.Textarea)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['name'].widget.attrs['placeholder'] = 'Please type your name'
        self.fields['name'].widget.attrs['class'] = 'form-control'
        
        self.fields['email'].widget.attrs['placeholder'] = 'Please type your email address'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        
        self.fields['title'].widget.attrs['placeholder'] = 'Please type the subject'
        self.fields['title'].widget.attrs['class'] = 'form-control'
        
        self.fields['message'].widget.attrs['placeholder'] = 'Please type your message'
        self.fields['message'].widget.attrs['class'] = 'form-control'
        
        
        def send_email(self):
            name = self.cleaned_data['name']
            email = self.cleaned_data['email']
            title = self.cleaned_data['title']
            message = self.cleaned_data['message']
            
            subject = 'お問い合わせ： {}'.format(title)
            
            message = 'Sender: {0}\n Email: {1}\n Subject: {2}\n Message: \n{3}'.format(name, email, title, message)
            
            from_email = 'system@neoflow.jp'
            to_list = ['daisuke@neoflow.jp']
            message = EmailMessage(subject=subject,
                                   body=message,
                                   from_email=from_email,
                                   to=to_list,
                                   )
            message.send()