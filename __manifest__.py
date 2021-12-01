{
    'name': 'Price History',
    'version': '1.1',
    'summary': 'Inventory, Logistic, Valuation, Accounting',
    'description': """
Price History
=============
    """,
    'depends': ['stock_account'],
    'category': 'Hidden',
    'sequence': 16,
    'data': [
        'security/ir.model.access.csv',
        'views/price_history_views.xml'
    ],
    'test': [
    ],
    'installable': True,
    'auto_install': True,
}
