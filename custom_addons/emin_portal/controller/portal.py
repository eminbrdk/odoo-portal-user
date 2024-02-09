from odoo.addons.portal.controllers.portal import CustomerPortal
from odoo.http import request
from odoo import http

class WeblearnsPortal(CustomerPortal):

    def _prepare_home_portal_values(self, counters):
        rtn = super(WeblearnsPortal, self)._prepare_home_portal_values(counters)
        rtn["student_counts"] = request.env["school.student"].search_count([])
        return rtn

    @http.route(["/my/students", "/my/students/page/<int:page>"], type="http", website=True)
    def wb_student_list_view_portal(self, page=1, sortby="id", **kw):
        sorted_list = {
            "id": {"label": "ID Decs", "order": "id desc"},
            "name": {"label": "Name", "order": "name"},
            "school_id": {"label": "School", "order": "school_id"},
        }
        default_order_by = sorted_list[sortby]["order"]
        students = request.env["school.student"].search([], limit=5, order=default_order_by)
        vals = {"students": students, "page_name": "students_list_view", "sortby": sortby, "searchbar_sortings": sorted_list}
        return request.render("emin_portal.wb_student_list_view_portal", vals)

    def small_button_pressed(self):
        print("smalll")
        return "yusuf-5"

    def big_button_pressed(self):
        print("bigggg")
        return "yusuf-5"

    @http.route(['/my/students/<model("school.student"):student_id>'], type="http", website=True)
    def web_learns_student_form_view_portal(self, student_id, **kw):
        big = self.big_button_pressed()
        small = self.small_button_pressed()
        vals = {"student": student_id, "page_name": "student_form_view", "big_button": big, "small_button": small}
        return request.render("emin_portal.web_learns_student_form_view_portal", vals)