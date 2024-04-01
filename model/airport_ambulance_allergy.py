from odoo import models, fields, api


class AirportAmbulanceAllergy(models.Model):
    _name = 'airport.ambulance.allergy'
    _description = 'Airport Ambulance Allergy'

    name = fields.Char(string='過敏原名稱')