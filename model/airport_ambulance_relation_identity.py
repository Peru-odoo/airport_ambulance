from odoo import models, fields, api


class AirportAmbulanceRelationIdentity(models.Model):
    _name = 'airport.ambulance.relation.identity'
    _description = 'Airport Ambulance Relation Identity'

    name = fields.Char(string='關係人名稱')
    ambulance_table_ids = fields.One2many('airport.ambulance.table', 'relation_identity_id')