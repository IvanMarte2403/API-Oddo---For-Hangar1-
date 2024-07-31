from odoo import models, fields, api
import requests

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    api_order_number = fields.Char(string='API Order Number')
    api_first_name = fields.Char(string='First Name')
    api_last_name = fields.Char(string='Last Name')
    api_kilometers = fields.Float(string='Kilometers')

    def fetch_api_data(self):
        base = "https://openapi.somosclear.com/api/"
        user = "hangar1@hangar1.com.mx"
        password = "gK9fR3pF6iT1rS3h*"
        repair_shop_id = 3080

        access_token = self.login(user, password)

        for order in self:
            order_number = order.api_order_number
            if order_number:
                order_details = self.get_order_details(access_token, order_number, repair_shop_id)
                if order_details:
                    order.api_first_name = order_details['firstName']
                    order.api_last_name = order_details['lastName']
                    order.api_kilometers = order_details['kilometers']

    def login(self, username, password):
        base = "https://openapi.somosclear.com/api/"
        url = base + "users/login"
        payload = {"email": username, "password": password}
        headers = {
            "Content-Type": "application/json",
            "accept": "application/json"
        }

        response = requests.post(url, json=payload, headers=headers)
        response_data = response.json()
        if response.status_code == 200:
            return response_data['accessToken']
        else:
            error_message = response_data.get('message', 'Unknown error')
            raise Exception(f"Error logging in: {error_message}")

    def get_order_details(self, access_token, order_number, repair_shop_id):
        base = "https://openapi.somosclear.com/api/"
        url = f"{base}cm/orders/{order_number}?repairShopId={repair_shop_id}"
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        }

        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()['data']
        else:
            response_data = response.json()
            error_message = response_data.get('message', 'Unknown error')
            raise Exception(f"Error fetching order details: {error_message}")
