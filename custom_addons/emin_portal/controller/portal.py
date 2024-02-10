from odoo.addons.portal.controllers.portal import CustomerPortal, pager
from odoo.http import request
from odoo import http

class WeblearnsPortal(CustomerPortal):

    @http.route(["/new/student"], auth="user", type="http", website=True, methods=["POST", "GET"])
    def registerNewStudent(self, **kw):
        school_list = request.env["school"].sudo().search([])
        vals = {"school_list": school_list, "page_name": "register_student", "success": False}

        if request.httprequest.method == "POST":
            error_list = []
            vals["success"] = False
            if not kw.get("name"):
                error_list.append("Name is required. Please fulfill")
            if not kw.get("school"):
                error_list.append("School is required. Please choose one")
            if not kw.get("school").isdigit() or request.env["school"].sudo().search["id", "=", int(kw.get("school"))]:
                error_list.append("Invalid school field")
            if not error_list:
                vals["success"] = True
                request.env["school.student"].sudo().create({
                    "name": kw.get("name"),
                    "school_id": int(kw.get("school"))
                })
                # return request.redirect("/my/students")
            else:
                vals["error_list"] = error_list

        return request.render("emin_portal.new_student_form_view_portal", vals)

    # bu fonksiyonla portala valuları gönderdik !!!!!!!!!!!!
    # bunun gibi bir kaç tane daha hazır ekleme yapabileceğin fonksiyon var
    def _prepare_home_portal_values(self, counters):
        rtn = super(WeblearnsPortal, self)._prepare_home_portal_values(counters)
        rtn["student_counts"] = request.env["school.student"].sudo().search_count([])
        return rtn

    @http.route(["/my/students", "/my/students/page/<int:page>"], auth="user", type="http", website=True)
    def wb_student_list_view_portal(self, **kw):
        students = request.env["school.student"].sudo().search([])
        vals = {"students": students, "page_name": "students_list_view",}
        return request.render("emin_portal.wb_student_list_view_portal", vals)

    @http.route(['/my/students/<model("school.student"):student_id>'], type="http", website=True, auth="user")
    def web_learns_student_form_view_portal(self, student_id, **kw):
        vals = {"student": student_id, "page_name": "student_form_view"}
        return request.render("emin_portal.web_learns_student_form_view_portal", vals)