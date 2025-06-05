{
    'name': 'MIPS Payment Gateway',
    'version': '1.0',
    'category': 'Accounting/Payment',
    'summary': 'MIPS payment gateway integration',
    'author': 'Your Name',
    'depends': ['payment'],
    'data': [
        'security/ir.model.access.csv',
        'views/mips_payment_template.xml',
        'data/payment_provider_data.xml',
    ],
    'installable': True,
    'application': False,
}
