{
    "name": "Seta Groups and Attendance",
    "summary": "Adds groups for contacts and attendance register.",
    "version": "16.0.1.0.0",
    "category": "Contact",
    "author": "Manuel Calero, Abraham Carrasco, Xtendoo",
    "license": "LGPL-3",
    "application": True,
    "depends": [
        "base",
        "contacts",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/contact_groups_view.xml",
        "views/attendance_record_view.xml",
    ],
    "installable": True,
}
