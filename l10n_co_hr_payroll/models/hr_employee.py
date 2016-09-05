# -*- encoding: utf-8 -*-
# #############################################################################
#
# OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
# #############################################################################

from openerp.osv import fields, osv
from openerp.tools.translate import _

# Agrega campos EPS y Fondo de Pensiones en datos del empleado.

class hr_employee_co(osv.osv):
    _inherit = 'hr.employee'

    _columns = {
        'eps_id': fields.many2one('res.partner', 'EPS'),
        'fp_id': fields.many2one('res.partner', 'Fondo de Pensiones'),
        'fc_id': fields.many2one('res.partner', 'Fondo de Cesantías'),
    }

hr_employee_co()
