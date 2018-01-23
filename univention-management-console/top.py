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
from univention.management.console.modules import Base, UMC_Error
from univention.management.console.log import MODULE

from univention.management.console.modules.decorators import sanitize, simple_response
from univention.management.console.modules.sanitizers import PatternSanitizer, ChoicesSanitizer, ListSanitizer, IntegerSanitizer

_ = Translation('univention-management-console-module-top').translate


class Instance(Base):

    @sanitize(
        signal=ChoicesSanitizer(choices=['SIGTERM', 'SIGKILL']),
        pid=ListSanitizer(IntegerSanitizer())
    )
    @simple_response
    def kill(self, signal, pid):
        failed = []
        for pid_ in pid:
            try:
                process = psutil.Process(pid_)
                if signal == 'SIGTERM':
                    process.terminate()
                elif signal == 'SIGKILL':
                    process.kill()
            except psutil.NoSuchProcess as exc:
                failed.append(str(pid_))
                MODULE.error('Could not %s pid %s: %s' % (signal, pid_, exc))
        if failed:
            failed = ', '.join(failed)
            raise UMC_Error(_('No process found with PID %s') % (failed))
        return True
