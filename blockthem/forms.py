from django import forms
from blockthem.models import Rule


class RuleForm(forms.ModelForm):
    request = None

    def clean(self):
        cleaned_data = super(RuleForm, self).clean()
        if not cleaned_data.get('ip') and not cleaned_data.get('user_agent'):
            raise forms.ValidationError(u'Eighter IP or User Agent should be provided.')
        ip = self.request.META['REMOTE_ADDR']
        user_agent = self.request.META['HTTP_USER_AGENT']
        rule = Rule(**cleaned_data)
        if rule.matches(ip, user_agent):
            raise forms.ValidationError(u'This rule matches your current UserAgent and/or IP!')
        return cleaned_data

    class Meta:
        model = Rule
