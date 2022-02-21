from django import forms
from .models import FeedBack


class FeedBackForm(forms.ModelForm):
    class Meta:
        model = FeedBack
        #fields = ['name', 'email', 'message']
        fields = '__all__'
        widgets = {
            #<textarea name="message" id="message" class="form-control" rows="4" placeholder="Message" required></textarea>
            'name': forms.TextInput(
                    attrs={
                        'id': 'name',
                        'class': 'form-control',
                        'placeholder': 'Имя',
                    }
            ),
            'email': forms.EmailInput(
                    attrs={
                        'id': 'email',
                        'class': 'form-control',
                        'placeholder': 'Почта',
                    }
            ),
            'phone': forms.TextInput(
                    attrs={
                        'id': 'phone',
                        'class': 'form-control',
                        'placeholder': 'Телефон',
                    }
            ),
            'message': forms.Textarea(
                    attrs={
                        'id': 'message',
                        'class': 'form-control',
                        'placeholder': 'Ваше сообщение или заказ',
                        'rows': '4'
                    }
            )
        }