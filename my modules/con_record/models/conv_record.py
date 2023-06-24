
from odoo import models, fields, api, _
from datetime import date,datetime

class conver_record(models.Model):
    _name="conver_record"


    name=fields.Char(string="name")
    type=fields.Char(string="type")
    employee=fields.Char(string="employee")
    date=fields.date(string="date", defualt=date.today())

