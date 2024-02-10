from odoo import api, models, fields


class Student(models.Model):
    _name = "school.student"
    _description = "Regular Student"

    name = fields.Char(string="Name", required=True)
    roll_number = fields.Integer(string="Roll Number")
    school_id = fields.Many2one("school", string="School", required=True)
    total_fees = fields.Integer(string="Total Fees")


class School(models.Model):
    _name = "school"
    _description = "Regular School"

    name = fields.Char(string="Name", required=True)
    address = fields.Text(string="Address")
