from odoo import models, fields, api


class AirportAmbulanceAttendingCrewsRecord(models.Model):
    _name = 'airport.ambulance.attending.crews.record'
    _description = 'Airport Ambulance Attending Crews Record'

    name = fields.Char(string='姓名')
    signature = fields.Binary(string='簽名')
    ambulance_table_id = fields.Many2one('airport.ambulance.table', string='救護車單紀錄')