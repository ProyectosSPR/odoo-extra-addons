# -*- coding: utf-8 -*-
from odoo import models, fields

class ResConfigSettings(models.TransientModel):
    """
    Hereda del modelo base de ajustes para añadir nuevos campos de configuración.
    """
    _inherit = 'res.config.settings'

    # Campo para guardar la URL de la instancia de n8n.
    # El valor se guarda como un parámetro de sistema gracias a 'config_parameter'.
    n8n_url = fields.Char(
        string='URL de n8n',
        config_parameter='n8n_integration.n8n_url', # Clave única del parámetro
        help="La URL base de tu instancia de n8n (ej. https://n8n.miempresa.com)"
    )

    # Campo para guardar la API Key de n8n.
    # También se guarda como un parámetro del sistema.
    n8n_api_key = fields.Char(
        string='API Key de n8n',
        config_parameter='n8n_integration.n8n_api_key' # Clave única del parámetro
    )