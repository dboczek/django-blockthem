from django.shortcuts import render_to_response
from models import Rule
from django.conf import settings


class BlockThemMiddleware(object):

    def process_request(self, request):
        rules = Rule.objects.all()
        ip = request.META['REMOTE_ADDR']
        user_agent = request.META['HTTP_USER_AGENT']

        for rule in rules:
            if rule.matches(ip, user_agent):
                reason = ''
                if rule.reason_is_public:
                    reason = rule.reason
                response = render_to_response(
                    'blockthem/403.html', {
                        'reason': reason,
                        'email': getattr(settings, 'BLOCKTHEM_ADMIN_EMAIL', None)
                    })
                response.status_code = 403
                return response
        return None
