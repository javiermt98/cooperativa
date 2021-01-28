# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime, date
from odoo.exceptions import ValidationError

class cooperativa(models.Model):
    _name = 'cooperativa.camp_model'
    _description = 'Modelo de Campanya'

    name = fields.Char(string="Campanya", default=date.today().year, readonly=True)
    fecha = fields.Date(string="Fecha", default=datetime.now(), readonly=True)
    socios = fields.Many2one("cooperativa.socios_model", "Socio")
    producto = fields.Many2one("cooperativa.prod_model", "Producto")
    cantidad = fields.Float(string="Cantidad", default=0)
    active = fields.Boolean(readonly=True, default=True)



    @api.depends("cantidad")
    def _cantidadPositiva(self):
        if self.cantidad<=0:
            raise ValidationError("La cantidad no puede ser negativa")


    def actualizaKilos(self):
        self.ensure_one()
        for i in self.producto:
            i.kgtot +=self.cantidad
        
               

    def eliminaHistorial(self):
        return True
        # historialSocios = self.search([("active","=","False")])
        # for i in historialSocios:
        #     i.unlink()

    def actualizaSaldo(self):
        self.ensure_one()
        for i in self.socios:
            i.saldo += self.cantidad*self.producto.precio
        self.active = False