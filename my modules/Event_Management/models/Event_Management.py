from odoo import models, fields, api, _


class Event_Management(models.Model):
    _name="Event_Management"


    name=fields.Char(string="name")
    employee=fields.Char(string="employee")
    date=fields.date(string="date")
