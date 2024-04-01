from odoo import models, fields, api


class AirportAmbulanceFirstAidCpr(models.Model):
    _name = 'airport.ambulance.first.aid.cpr'
    _description = 'Airport Ambulance First Aid CPR'

    name = fields.Char(string='心肺復甦術名稱')