# saas_access_management/models/sale_subscription.py
from odoo import models, fields

class SaleSubscription(models.Model):
    _inherit = 'sale.subscription'

    is_provisioned = fields.Boolean(
        string='Acceso Aprovisionado',
        default=False,
        copy=False,
        help="Marca si ya se ha ejecutado la acción de crear/configurar el usuario para esta suscripción."
    )