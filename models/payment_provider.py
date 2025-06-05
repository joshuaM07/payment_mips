"""MIPS payment provider model extension."""

from odoo import fields, models

class PaymentProvider(models.Model):
    """Extend ``payment.provider`` with MIPS specific credentials."""

    _inherit = 'payment.provider'

    mips_short_id_merchant = fields.Char(string="Merchant ID")
    mips_short_id_entity = fields.Char(string="Entity ID")
    mips_operator_id = fields.Char(string="Operator ID")
    mips_operator_password = fields.Char(string="Operator Password")
    mips_hash_salt = fields.Char(string="Hash Salt")
    mips_cipher_key = fields.Char(string="Cipher Key")
    mips_basic_username = fields.Char(string="Basic Auth Username")
    mips_basic_password = fields.Char(string="Basic Auth Password")
    mips_sandbox = fields.Boolean(string="Sandbox Mode")

    def _mips_endpoint(self):
        """Return the API endpoint depending on the sandbox flag."""
        if self.mips_sandbox:
            return "https://sandbox.mips.mu/api"
        return "https://merchant.mips.mu/api"
