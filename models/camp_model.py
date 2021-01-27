# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime, date
from odoo.exceptions import ValidationError

class cooperativa(models.Model):
    _name = 'cooperativa.camp_model'
    _description = 'Modelo de Campanya'

    name = fields.Char(string="Campanya", default=date.today().year, readonly=True)
    fecha = fields.Date(string="Fecha", default=date.today(), readonly=True)
    socio = fields.Many2one("cooperativa.socios_model", "Socio")
    producto = fields.Many2one("cooperativa.prod_model", "Producto")
    cantidad = fields.Float(string="Cantidad", default=0)
    socios = fields.Many2one("cooperativa.socios_model", "Socios")



    @api.depends("cantidad")
    def _cantidadPos(self):
        if self.cantidad<0:
            raise ValidationError("La cantidad no puede ser negativa")