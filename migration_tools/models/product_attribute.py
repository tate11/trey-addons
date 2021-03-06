# -*- coding: utf-8 -*-
# License, author and contributors information in:
# __openerp__.py file at the root folder of this module.
from openerp import models, fields


class ProductAttribute(models.Model):
    _inherit = 'product.attribute'

    migration_id = fields.Integer(
        string='MigrationId',
        help='Old system identificator',
        default=0)
    migration_key = fields.Char(
        string='MigrationKey',
        help='Old system identificator Key',
        default='@@@')
    filename = fields.Char(
        string='File Name',
        help='Import File Name',
        required=False)
    sheetname = fields.Char(
        string='Sheet Name',
        help='Import Sheet Name',
        required=False)
    row = fields.Char(
        string='Row',
        help='Import Row Number',
        required=False)


class ProductAttributeValue(models.Model):
    _inherit = 'product.attribute.value'

    migration_id = fields.Integer(
        string='MigrationId',
        help='Old system identificator',
        default=0)
    migration_key = fields.Char(
        string='MigrationKey',
        help='Old system identificator Key',
        default='@@@')
    filename = fields.Char(
        string='File Name',
        help='Import File Name',
        required=False)
    sheetname = fields.Char(
        string='Sheet Name',
        help='Import Sheet Name',
        required=False)
    row = fields.Char(
        string='Row',
        help='Import Row Number',
        required=False)


class ProductAttributeLine(models.Model):
    _inherit = 'product.attribute.line'

    migration_id = fields.Integer(
        string='MigrationId',
        help='Old system identificator',
        default=0)
    migration_key = fields.Char(
        string='MigrationKey',
        help='Old system identificator Key',
        default='@@@')
    filename = fields.Char(
        string='File Name',
        help='Import File Name',
        required=False)
    sheetname = fields.Char(
        string='Sheet Name',
        help='Import Sheet Name',
        required=False)
    row = fields.Char(
        string='Row',
        help='Import Row Number',
        required=False)
