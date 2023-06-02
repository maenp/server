from django import forms


class ReqisterForm(forms.Form):
    username=forms.CharField(min_length=3,required=True,error_messages={
        'required':'用户名不能为空',
        'min_length':'用户名至少3位字符'
    })
    password=forms.CharField(min_length=8,required=True,error_messages={
        'required':'密码不能为空',
        'min_length':'密码至少8位字符'
    })
    is_staff=forms.BooleanField(required=False)
    #全局验证
    def clean(self):
        return self.cleaned_data
    