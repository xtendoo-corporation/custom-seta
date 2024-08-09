{
    "name": "Seta Extend Res Partner",
    "summary": "Adds new fields to res partner fot Seta Fundation.",
    "version": "16.0.1.0.0",
    "category": "Contact",
    "author": "Manuel Calero, Dario Cruz, Xtendoo",
    "license": "LGPL-3",
    "application": True,
    "depends": [
        "contacts",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/res_partner_view.xml",
        "views/custom_res_partner_kanban_view.xml",
        "views/medical_diagnostic.xml",
    ],
    "installable": True,
}
