# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime, date
from odoo.exceptions import ValidationError

class cooperativa(models.Model):
    _name = 'cooperativa.socios_model'
    _description = 'Modelo de Socios'
    _sql_constraints = [('socios_id_uniq','UNIQUE (id_socio)','No puede haber dos socios con el mismo ID'),("dni_uniq", "UNIQUE (dni)", "No puede haber dos DNI iguales")]

    name = fields.Char(string="Nombre", required=True)
    id_socio = fields.Integer(string="ID", required=True)
    ape = fields.Char(string="Apellidos", required=True)
    dni = fields.Char(string="DNI", required=True)
    fechaAlta = fields.Date(string="Fecha", required=True, default=date.today(), readonly=True)
    telf = fields.Char(string="Telefono", required=True)
    email = fields.Char(string="Email")
    saldo = fields.Float(string="Saldo", default=0, readonly=True)
    regpend = fields.One2many("cooperativa.camp_model", "socios", "Registros Pendientes", readonly=True)


    @api.constrains("dni")
    def _comprobarDNI(self):
        if len(self.dni)!=9:
            raise ValidationError("El DNI debe tener 9 caracteres")
        else:
            try:
                n=int(self.dni[:-1])
            except ValueError:
                raise ValidationError("Los primeros 8 dígitos deben ser números")

            palabra='TRWAGMYFPDXBNJZSQVHLCKE'

            if self.dni[-1].upper() == palabra[n%23]:
                return True
            else:
                raise ValidationError("La letra no coincide con el DNI. Se esperaba "+palabra[n%23])

    @api.constrains("email")
    def _comprobarEmail(self):
        if "@" and "." not in self.email:
            raise ValidationError("El email no es correcto. Debe contener al menos @ y .")
        elif len(self.email)<5:
            raise ValidationError("El email no es correcto. Debe contener al menos 5 caracteres")


    @api.constrains("telf")
    def _comprobarTelf(self):
        if len(self.telf) != 9:
            raise ValidationError("El teléfono debe contener 9 dígitos")

