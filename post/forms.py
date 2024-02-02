from django import forms

from post.models import Product, Review


class ProductCreateForm(forms.Form):
    photo = forms.ImageField(
        required=False,
        label="Фото"
    )
    title = forms.CharField(
        max_length=100,
        label="Название"
    )
    content = forms.CharField(
        required=False,
        label="Контет",
        widget=forms.Textarea
    )

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 10:
            raise forms.ValidationError("Длина превышает 10 символов")
        return title

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        content = cleaned_data.get('content')

        if title == content:
            raise forms.ValidationError("Заголовок и контент совпадают")

        return cleaned_data


class ProductCreateForm2(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('photo', 'title', 'content', 'categories', 'price')
        labels = {
            'photo': 'Фото',
            'title': 'Название',
            'content': 'Контент',
            'price': 'Цена'
        }

        def clean_title(self):
            title = self.cleaned_data['title']
            if len(title) > 10:
                raise forms.ValidationError("Длина превышает 10 символов")
            return title

        def clean(self):
            cleaned_data = super().clean()
            title = cleaned_data.get('title')
            content = cleaned_data.get('content')

            if title == content:
                raise forms.ValidationError("Заголовок и контент совпадают")

            return cleaned_data

class ReviewCreateForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('text',)
        labels = {
            'content': 'Контент',
        }