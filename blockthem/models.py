# -*- coding: utf-8 -*-
from django.db import models
import re


class Rule(models.Model):
    ip = models.GenericIPAddressField(verbose_name=u'IP', blank=True, null=True, default=None)
    user_agent = models.CharField(max_length=255, blank=True, default=u'')
    user_agent_is_regular_expression = models.BooleanField(
        help_text=u'If true User Agent string will be used as regular expression. Otherwise exact match will be used.',
        default=False)
    reason = models.TextField(blank=True)
    reason_is_public = models.BooleanField(
        help_text=u'If true reason will be displayed on 403 page presented to blocked by this.',
        default=False)

    def matches(self, ip, user_agent):
        if self.ip and self.ip != ip:
            return False
        if self.user_agent:
            if self.user_agent_is_regular_expression:
                if not re.search(self.user_agent, user_agent):
                    return False
            else:
                if self.user_agent != user_agent:
                    return False
        return True

    def __unicode__(self):
        name = u'Block '
        name += self.ip and u'IP %s' % self.ip or ''
        name += self.ip and self.user_agent and ' with ' or ''
        name += self.user_agent and \
            u'User Agent %s"%s"' % (self.user_agent_is_regular_expression and 'r' or '', self.user_agent) or ''
        return name
