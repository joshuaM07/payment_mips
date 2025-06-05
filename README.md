# MIPS Payment Gateway

This module integrates the MIPS payment gateway with Odoo's payment system. It defines a new payment provider with the necessary configuration fields and a minimal QWeb template.

## Features
- Adds a new provider "MIPS" under the Payment Providers menu.
- Supports configuration of merchant credentials such as Merchant ID, Entity ID and other keys.
- Provides a basic checkout template that can be extended to implement the full gateway flow.

## Installation
1. Copy this module to your Odoo `addons` directory.
2. Update the app list and install **MIPS Payment Gateway** from the Apps menu.

## Usage
After installation, open **Invoicing > Configuration > Payment Providers** and select **MIPS** to configure the credentials supplied by MIPS.

The module currently exposes only the provider configuration and template placeholder. Custom logic for communicating with the MIPS API can be added by extending the model in `models/payment_provider.py` and adapting the QWeb template.
