from django import forms
from detector.models import UserModel, Values

#signup form for user basic information....................
class SignUpForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['name','address','contact','email','age','gender','password']
        error_messages = {'name':{'required':'Please let us know what to call you.'},'age':{'required':'AGE .'},
                         'email': {'required': 'Please provide your mail id.'},'password':{'required':'Password can not be left blank.'}}

class LogInForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['name','password']
        error_messages = {'name': {'required': 'Username can not be left blank.'},
                          'password': {'required': 'Password can not be left blank.'}}

class Detect(forms.ModelForm):
    class Meta:
        model = Values
        fields = ['age','sex','cp','trestbps','chol','fbs','restecg','thalach','exang','slope','ca','thal']
