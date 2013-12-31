from django.contrib import admin
from blockthem.models import Rule
from blockthem.forms import RuleForm


class RuleAdmin(admin.ModelAdmin):
    list_display = ['__unicode__', 'reason']
    form = RuleForm

    def get_form(self, request, obj=None, **kwargs):
        form = super(RuleAdmin, self).get_form(request, obj, **kwargs)
        form.request = request
        return form


admin.site.register(Rule, RuleAdmin)
