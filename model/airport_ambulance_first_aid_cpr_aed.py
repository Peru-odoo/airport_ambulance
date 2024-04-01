from odoo import models, fields, api


class AirportAmbulanceFirstAidCprAed(models.Model):
    _name = 'airport.ambulance.first.aid.cpr.aed'
    _description = 'Airport Ambulance First Aid CPR AED'

    name = fields.Char(string='使用AED名稱')