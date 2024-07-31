{
    'name': 'hangar-api-integration',
    'version': '15.0.1.0.0',
    'summary': 'Integrates external API data into Sales module',
    'author': 'Hangar1',
    'website': 'https://github.com/IvanMarte2403/API-Oddo---For-Hangar1-',
    'license': 'AGPL-3',
    'depends': ['sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/sale_order_view.xml',
        'data/data.xml',
    ],
    'installable': True,
    'application': False,
}