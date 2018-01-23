#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
#
# Univention Management Console
#  module: process overview
#
# Copyright 2011-2017 Univention GmbH
#
# http://www.univention.de/
#
# All rights reserved.
#
# The source code of this program is made available
# under the terms of the GNU Affero General Public License version 3
# (GNU AGPL V3) as published by the Free Software Foundation.
#
# Binary versions of this program provided by Univention to you as
# well as other copyrighted, protected or trademarked materials like
# Logos, graphics, fonts, specific documentations and configurations,
# cryptographic keys etc. are subject to a license agreement between
# you and Univention and not subject to the GNU AGPL V3.
#
# In the case you use this program under the terms of the GNU AGPL V3,
# the program is provided in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public
# License with the Debian GNU/Linux or Univention distribution in file
# /usr/share/common-licenses/AGPL-3; if not, see
# <http://www.gnu.org/licenses/>.

import psutil

from univention.lib.i18n import Translation
from univention.management.console.modules import Base
from univention.management.console.log import MODULE

_ = Translation('univention-management-console-module-top').translate


class Instance(Base):

    def kill(self, request):
        MODULE.info('Calling with flavor=%s' % (request.flavor,))
        result, message, status = (True, None, None)
        pid = request.options.get('pid')
        signal = request.options.get('signal')
        try:
            process = psutil.Process(pid)
            if signal == 'SIGTERM':
                process.terminate()
            elif signal == 'SIGKILL':
                process.kill()
        except psutil.NoSuchProcess:
            message = _('No process found with PID %s') % (pid,)
            result = False
            status = 400
        self.finished(request.id, result, status=status, message=message)
