"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _
from django.db import models
from .models import Comment
from app.models import Blog


class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Логин'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Пароль'}))

class AnketaForm(forms.Form):
    name = forms.CharField(label = 'Ваше имя', min_length=2, max_length=50)
    city = forms.CharField(label='Ваш возраст', min_length=2, max_length=50)
    gender = forms.ChoiceField(label='Ваш пол',
                             choices=[('1','Мужской'),('2','Женский')],
                             widget = forms.RadioSelect, initial=1)
    job = forms.ChoiceField(label='Вы согласны ли получать 120$ в неделю за полные ночные смены ?',
                             choices=[('1','Конечно'),('2','Хотелось бы больше')],
                             widget = forms.RadioSelect, initial=1)
    internet = forms.ChoiceField(label = 'Как часто вы бывали ли в пиццерии Freddy Fasbers?',
                                 choices = (('1', 'Никогда'),
                                 ('2', 'Раз в пол года/ в год'),
                                 ('3', 'Раз в месяц' ),
                                 ('4', 'Раз в неделю' ),
                                 ('5', 'Приходил ребёнком/с детьми каждый день')), initial=1)
    notice = forms.BooleanField(label='Вы любите мишку Фреди ?', required=False)
    email = forms.CharField(label='Напишите ваш номер телефона', min_length=7)
    message = forms.CharField(label='Напишите дополнительную информацию о вас', widget=forms.Textarea(attrs={'rows':12, 'cols':20}))
    
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment  # используемая модель
        fields = ('text',)  # требуется заполнить только поле text
        labels = {'text': "Комментарий"}  # метка к полю формы text

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'description', 'content', 'image',)
        labels = {'title': "Заголовок", 'description': "Краткое содержание", 'content': "Полное содержание", 'image': "Картинки"}
