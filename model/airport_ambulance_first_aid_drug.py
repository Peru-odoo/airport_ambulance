from odoo import models, fields, api


class AirportAmbulanceFirstAidDrug(models.Model):
    _name = 'airport.ambulance.first.aid.drug'
    _description = 'Airport Ambulance First Aid Drug'

    name = fields.Char(string='藥物處置名稱')