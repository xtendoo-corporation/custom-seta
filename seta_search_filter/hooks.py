# -*- coding: utf-8 -*-
from odoo import api
from odoo import SUPERUSER_ID

def uninstall_hook(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    action = env.ref('contacts.action_contacts', raise_if_not_found=False)
    if action:
        context = action.context or '{}'
        import json
        try:
            ctx = json.loads(context.replace("'", '"'))
        except Exception:
            ctx = {}
        if 'search_default_type_company' in ctx:
            del ctx['search_default_type_company']
            action.write({'context': str(ctx)})
