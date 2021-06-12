from django import forms
from django.core import validators
from .models import Bb, Rubric, Img
from captcha.fields import CaptchaField
from django.contrib.auth.models import User


class BbForm(forms.ModelForm):
    title = forms.CharField(label='Название товара',
                            validators=[validators.RegexValidator(regex='^.{3,}$')],
                            error_messages={'invalid': 'Слишком короткое название товара'})
    content = forms.CharField(label='Описание',
                              widget=forms.widgets.Textarea())
    price = forms.DecimalField(label='Цена', decimal_places=2)
    rubric = forms.ModelChoiceField(queryset=Rubric.objects.all(),
                                    label='Рубрика', help_text='Категория товара',
                                    widget=forms.widgets.Select(attrs={'size': 5}))
    captcha = CaptchaField()

    class Meta:
        model = Img
        fields = '__all__'
        # class Meta:
        model = Bb
        fields = ('title', 'content', 'price', 'rubric')


class ImgForm(forms.ModelForm):
    img = forms.ImageField(label='Изображение',
                           validators=[validators.FileExtensionValidator(allowed_extensions=('gif', 'jpg', 'png'))],
                           error_messages={'invalid_extension': 'Этот формат не поддерживается'})
    desc = forms.CharField(label='Описание', widget=forms.widgets.Textarea())

    class Meta:
        model = Img
        fields = '__all__'


class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Логин'
        self.fields['password'].label = 'Пароль'

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        if not User.objects.filter(username=username).exists():
            raise forms.ValidationError(f'Не существует пользователя {username}')
        user = User.objects.filter(username=username).first()
        if user:
            if not user.check_password(password):
                raise forms.ValidationError("Неверный пароль")
        return self.cleaned_data

    class Meta:
        model = User
        fields = ['username', 'password']
