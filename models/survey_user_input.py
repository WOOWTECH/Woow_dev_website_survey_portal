# -*- coding: utf-8 -*-
##############################################################################
#
#    Odoo, Open Source Management Solution
#    Copyright (C) 2015-2024 DevIntelle Consulting Service Pvt.Ltd
#    (<http://www.devintellecs.com>).
#
#    For Module Support : devintelle@gmail.com  or Skype : devintelle
#
##############################################################################

from odoo import models, _


class SurveyUserInput(models.Model):
    _name = 'survey.user_input'
    _inherit = ['survey.user_input', 'portal.mixin']

    def _compute_access_url(self):
        super(SurveyUserInput, self)._compute_access_url()
        for request in self:
            request.access_url = '/my/survey_detail/%s' % (request.id)

    def _get_report_base_filename(self):
        self.ensure_one()
        return '%s %s' % (_('Survey'), self.survey_id.title)


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
