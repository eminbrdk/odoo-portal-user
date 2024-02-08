from odoo import api, models, fields


class Student(models.Model):
    _name = "school.student"
    _description = "Regular Student"

    name = fields.Char(string="name", required=True)