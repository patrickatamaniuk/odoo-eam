﻿# -*- coding: utf-8 -*-
##############################################################################
#
#    Odoo
#    Copyright (C) 2014-2016 CodUP (<http://codup.com>).
#
##############################################################################

from openerp import api, fields, models
from openerp.addons.asset.asset import STATE_COLOR_SELECTION


class asset_asset(models.Model):
    _inherit = 'asset.asset'

    manufacture_state_color = fields.Selection(related='manufacture_state_id.state_color', selection=STATE_COLOR_SELECTION, string="Color", readonly=True)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
