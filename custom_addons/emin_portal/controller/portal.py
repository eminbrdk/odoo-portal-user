from odoo.addons.portal.controllers.portal import CustomerPortal
from odoo.http import request
from odoo import http

class WeblearnsPortal(CustomerPortal):

    def _prepare_home_portal_values(self, counters):
        rtn = super(WeblearnsPortal, self)._prepare_home_portal_values(counters)
        rtn["student_counts"] = request.env["school.student"].search_count([])
        return rtn

    @http.route(["/my/students"], type="http", website=True)
    def wb_student_list_view_portal(self, **kw):
        students = request.env["school.student"].search([])
        return request.render("emin_portal.wb_student_list_view_portal", {"students": students})
