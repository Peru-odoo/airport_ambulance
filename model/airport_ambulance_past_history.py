from odoo import models, fields, api


class AirportAmbulancePastHistory(models.Model):
    _name = 'airport.ambulance.past.history'
    _description = 'Airport Ambulance Past History'

    name = fields.Char(string='過去病史名稱')