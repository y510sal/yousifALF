
from odoo import models, fields, api, _
from datetime import date,datetime

class Care_Card(models.Model):
    _name="Care_Card"


    Card_No=fields.Char(string="Card No")
    beneficiary=fields.Char(string="beneficiary")
    Validity_date=fields.date(string="Validity date")
    Card_Status=fields.selection([('nonValid','NonValid'),('valid','Valid')], string=" Card Status")
    Card_Balance=fields.Integer(string="Card Balance")
    Card_issue_date=fields.date(string="Card issue date")
    date=fields.date(string="date", defualt=date.today())

