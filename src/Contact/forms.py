# forms.py
from django import forms
from django.core.validators import MaxLengthValidator
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets  import ReCaptchaV2Checkbox, ReCaptchaV3


class ContactForm(forms.Form):
    first_name = forms.CharField(
        max_length=100,
        label='Prénom',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Votre prénom'})
    )
    last_name = forms.CharField(
        max_length=100,
        label='Nom',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Votre nom'})
    )
    company = forms.CharField(
        label='Entreprise',
        required=False, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Votre organisation'})
    )
    subject = forms.ChoiceField(
        label='Sujet',
        choices=[('', 'Choisir dans la liste...'), ('recrutement', 'Recrutement'), ('mission', 'Proposition de mission'), ('projet', 'Realisation d\'un projet')],
        required=True,  
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Votre Email'})
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Votre message'}),
        validators=[MaxLengthValidator(150)]  # Limite le message à 500 caractères
    )
    accept_privacy_policy = forms.BooleanField(
        label=(
            "En cochant cette case et en soumettant ce formulaire, vous autorisez que vos données "
            "soient utilisées pour vous recontacter dans le cadre exclusif de votre demande."
            "Pour plus d'informations, veuillez consulter notre "
            "<a href='/contact/privacy-policy/' target='_blank'><strong>politique de confidentialité</strong></a>."
        ),
        required=True,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    captcha = ReCaptchaField(
        widget=ReCaptchaV3(
            action='signup',
            attrs={
                'required_score': 0.5,  # Score requis pour valider le captcha
            }
        )
    )
