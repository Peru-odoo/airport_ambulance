from odoo import models, fields, api


class AirportAmbulanceTraumaClassification(models.Model):
    _name = 'airport.ambulance.trauma.classification'
    _description = 'Airport Ambulance Trauma Classification'

    name = fields.Char(string='分類名稱')