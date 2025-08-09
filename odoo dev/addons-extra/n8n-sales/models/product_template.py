# -*- coding: utf-8 -*-
from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    def _auto_init(self):
        """Log cuando se inicializa el modelo"""
        _logger.info("=== INICIALIZANDO MODELO ProductTemplate n8n-sales ===")
        result = super()._auto_init()
        _logger.info("=== MODELO ProductTemplate n8n-sales INICIALIZADO ===")
        return result

    # --- CAMPOS PARA LA INTEGRACIÓN CON N8N ---
    is_digital_product = fields.Boolean(
        string="Es un Producto Digital/Automatización",
        help="Marca esta casilla si el producto corresponde a un servicio digital de n8n.",
        default=False
    )

    digital_product_type = fields.Selection(
        [
            ('one_time', 'Descargable / Única Vez'),
            ('subscription', 'Suscripción')
        ],
        string="Tipo de Acceso",
        default='one_time'
    )

    n8n_workflow_id = fields.Char(
        string="ID del Workflow"
    )
    
    n8n_workflow_name = fields.Char(
        string="Nombre del Workflow"
    )

    # Campo problemático - con logging
    integracion_con_odoo_cliente = fields.Boolean(
        string="Integración con Odoo de Cliente",
        help="Selecciona la casilla si el servidor va a ser usado en la propia instancia del cliente",
        default=False
    )

    administrado_odoo = fields.Selection(
        [
            ('admin', 'Administrado'),
            ('local', 'Servidor Local del Cliente')
        ],
        string="Tipo de Administración",
        default='admin'
    )

    database_odoo_local = fields.Char(
        string="Nombre Base de Datos",
        help="Nombre de la base de datos del cliente para servir automatización en su Odoo"
    )
    
    login_odoo_local = fields.Char(
        string="Usuario"
    )
    
    password_odoo_local = fields.Char(
        string="Contraseña",
        password=True
    )
    
    url_odoo_local = fields.Char(
        string="URL de Odoo"
    )

    @api.onchange('integracion_con_odoo_cliente')
    def _onchange_integracion_con_odoo_cliente(self):
        """Método onchange para cambiar administrado_odoo automáticamente"""
        _logger.info(f"=== ONCHANGE ejecutado: integracion_con_odoo_cliente = {self.integracion_con_odoo_cliente} ===")
        
        if self.integracion_con_odoo_cliente:
            self.administrado_odoo = 'local'
        else:
            self.administrado_odoo = 'admin'