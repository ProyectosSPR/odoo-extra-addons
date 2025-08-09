# odoo-extra-addons
addons extra de odoo

correr el jupter 
import odoo, builtins
from odoo.api import Environment
from odoo import SUPERUSER_ID

odoo.cli.server.report_configuration = lambda _: None
odoo.tools.config.parse_config(['-c', '/etc/odoo/odoo.conf'])

db_name = odoo.tools.config['db_name']
if not db_name:
    raise RuntimeError("No hay db_name en /etc/odoo/odoo.conf")

# Inicializa el registry de la BD específica y crea env/cr
registry = odoo.registry(db_name)
cr = odoo.sql_db.db_connect(db_name).cursor()
env = Environment(cr, SUPERUSER_ID, {})

builtins.env = env
builtins.cr = cr
print(f"Entorno listo: {db_name}")