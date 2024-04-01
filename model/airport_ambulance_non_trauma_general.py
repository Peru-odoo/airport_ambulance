from odoo import models, fields, api


class AirportAmbulanceNonTraumaGeneral(models.Model):
    _name = 'airport.ambulance.non.trauma.general'
    _description = 'Airport Ambulance Non Trauma General'

    name = fields.Char(string='一般疾病名稱')