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

from odoo.addons.portal.controllers.portal import CustomerPortal, pager as portal_pager
from odoo.exceptions import AccessError, MissingError
from odoo.http import request
from odoo import http


class CustomerPortal(CustomerPortal):

    def _prepare_home_portal_values(self, counters):
        values = super()._prepare_home_portal_values(counters)
        if 'survey' in counters:
            survey = request.env['survey.user_input']
            domain = [
                ('partner_id', '=', request.env.user.partner_id.id)
            ]
            survey_count = survey.search_count(domain)
            values['survey'] = survey_count
        return values

    @http.route(['/my/survey_detail', '/my/survey_detail/page/<int:page>'], type='http', auth="user", website=True)
    def portal_my_survey(self, page=1, **kw):
        values = self._prepare_portal_layout_values()
        survey_detail_pool = request.env['survey.user_input']

        domain = [
            ('partner_id', '=', request.env.user.partner_id.id)
        ]

        # Get total count for pagination
        survey_count = survey_detail_pool.search_count(domain)

        # Setup pager
        pager = portal_pager(
            url='/my/survey_detail',
            total=survey_count,
            page=page,
            step=self._items_per_page,
        )

        # Fetch records with pagination
        survey_detail = survey_detail_pool.search(
            domain,
            limit=self._items_per_page,
            offset=pager['offset'],
            order='create_date desc'
        )

        values.update({
            'survey_detail': survey_detail,
            'page_name': 'survey_detail_tree',
            'default_url': '/my/survey_detail',
            'pager': pager,
        })
        return request.render("dev_website_survey_portal.portal_my_survey_detail_1", values)

    @http.route(['/my/survey_detail/<int:order_id>'], type='http', auth="user", website=True)
    def portal_survey_detail_page(self, order_id, report_type=None, access_token=None, message=False, download=False,
                                   **kw):
        try:
            survey_detail_sudo = self._document_check_access('survey.user_input', order_id,
                                                              access_token=access_token)
        except (AccessError, MissingError):
            return request.redirect('/my')

        if report_type in ('pdf', 'text'):
            return self._show_report(
                model=survey_detail_sudo,
                report_type=report_type,
                report_ref='survey.certification_report',
                download=download
            )

        if report_type == 'html':
            return request.redirect('/survey/print/%s?answer_token=%s' % (
                survey_detail_sudo.survey_id.access_token,
                survey_detail_sudo.access_token
            ))

        values = {
            'survey_detail': survey_detail_sudo,
            'page_name': 'survey_detail_page',
            'report_type': 'html',
            'token': access_token,
        }
        return request.render('dev_website_survey_portal.main_portal_template_1', values)


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
