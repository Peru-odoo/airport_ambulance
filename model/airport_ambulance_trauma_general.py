from odoo import models, fields, api


class AirportAmbulanceTraumaGeneral(models.Model):
    _name = 'airport.ambulance.trauma.general'
    _description = 'Airport Ambulance Trauma General'

    name = fields.Char(string='一般外傷名稱')