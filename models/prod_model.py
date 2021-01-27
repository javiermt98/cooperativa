# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime, date
from odoo.exceptions import ValidationError


class cooperativa(models.Model):
    _name = 'cooperativa.prod_model'
    _description = 'Modelo de Productos'
    _sql_constraints = [('prod_name_uniq','UNIQUE (name)','No puede haber dos productos con el mismo nombre')]

    name = fields.Char(string="Nombre", requred=True)
    descripcion = fields.Char(string="Descripcion", required=True)
    precio = fields.Float(string="Precio", required=True)
    prod = fields.One2many("cooperativa.camp_model","producto", "Campanya")
    kgtot = fields.Float(string="Kilos Totales", readonly=True, compute="_calcKg", store=True)

    @api.depends("precio")
    def _precioPos(self):
        if self.precio<0:
            raise ValidationError("El precio no puede ser negativo")

    def _calcKg(self):
        self.ensure_one()
        suma = 0
        for i in self.prod:
            suma += i.cantidad
        suma = self.kgtot
    
    def eliminaKg(self):
        self.ensure_one()
        for i in self.prod:
            i.cantidad = 0
        

