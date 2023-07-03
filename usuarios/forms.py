from django import forms

class LoginForms(forms.Form):
    nome_login= forms.CharField(
        label="Nome de Login",
        required=True,
        max_length=100,
        widget= forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "bota teu nome ai parça"
            }
        )
    )
    senha= forms.CharField(
        label="Senha",
        required = True,
        max_length=70,
        widget= forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "sua senha ai"
            }
        )
    )

class cadastroForms(forms.Form):
    nome_cadastro = forms.CharField(
        label="Nome de Cadastro",
        required=True,
        max_length=100,
        widget= forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "bota teu nome ai parça"
            }
        )
    )
    email= forms.EmailField(
        label="bota seu Gmail ai",
        required=True,
        max_length=100,
        widget=forms.EmailInput(
                attrs={
                "class": "form-control",
                "placeholder": "bota teu gmail ai parça"
            }
        )
    )
    senha_1= forms.CharField(
        label="Senha",
        required = True,
        max_length=70,
        widget= forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "sua senha ai"
            }
        )
    )
    senha_2= forms.CharField(
        label="Confirme sua senha",
        required = True,
        max_length=70,
        widget= forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "mais uma vez mestre"
            }
        )
    )