from odoo.addons.portal.controllers.portal import CustomerPortal, pager
from odoo.http import request
from odoo import http

class WeblearnsPortal(CustomerPortal):

    def _prepare_home_portal_values(self, counters):
        rtn = super(WeblearnsPortal, self)._prepare_home_portal_values(counters)
        rtn["student_counts"] = request.env["school.student"].sudo().search_count([])
        return rtn

    @http.route(["/my/students", "/my/students/page/<int:page>"], auth="user", type="http", website=True)
    def wb_student_list_view_portal(self, page=1, sortby="id", **kw):
        sorted_list = {
            "id": {"label": "ID Decs", "order": "id desc"},
            "name": {"label": "Name", "order": "name"},
            "school_id": {"label": "School", "order": "school_id"},
        }
        default_order_by = sorted_list[sortby]["order"]
        students = request.env["school.student"].sudo().search([], limit=5, order=default_order_by)
        vals = {"students": students, "page_name": "students_list_view", "sortby": sortby, "searchbar_sortings": sorted_list}
        return request.render("emin_portal.wb_student_list_view_portal", vals)

    @http.route(['/my/students/<model("school.student"):student_id>'], type="http", website=True, auth="user")
    def web_learns_student_form_view_portal(self, student_id, **kw):
        vals = {"student": student_id, "page_name": "student_form_view"}
        return request.render("emin_portal.web_learns_student_form_view_portal", vals)