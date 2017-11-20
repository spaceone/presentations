#!/usr/bin/python2.7
# taken from https://git.knut.univention.de/univention/ucsschool/blob/6022c7d9296c76ea9a3f4a98190972fef2ddf434/ucs-school-umc-helpdesk/umc/python/helpdesk/__init__.py#L70
# bugzilla Bug 29975
# Fixed in UCS@school 4.0 R2

from univention.management.console.log import MODULE
from univention.management.console.config import ucr

from univention.lib.i18n import Translation
from ucsschool.lib import SchoolBaseModule

import notifier
import smtplib

_ = Translation('ucs-school-umc-helpdesk').translate


class Instance(SchoolBaseModule):

	def send(self, request):
		func = notifier.Callback(self._send_thread, 'packages@univention.de', ucr['ucsschool/helpdesk/recipient'].split(' '), request.options['username'], request.options['school'], request.options['category'], request.options['message'])
		MODULE.info('sending mail: starting thread')
		thread = notifier.threads.Simple('HelpdeskMessage', func)
		thread.run()

	def _send_thread(self, sender, recipients, username, school, category, message):
		MODULE.info('sending mail: thread running')

		msg = u'From: ' + sender + u'\r\n'
		msg += u'To: ' + (', '.join(recipients)) + u'\r\n'
		msg += u'Subject: %s (%s: %s)\r\n' % (category, _('School'), school)
		msg += u'Content-Type: text/plain; charset="UTF-8"\r\n'
		msg += u'\r\n'
		msg += u'%s: %s\r\n' % (_('Sender'), username)
		msg += u'%s: %s\r\n' % (_('School'), school)
		msg += u'%s: %s\r\n' % (_('Category'), category)
		msg += u'%s:\r\n' % _('Message')
		msg += message + u'\r\n'
		msg += u'\r\n'

		msg = msg.encode('UTF-8')

		server = smtplib.SMTP('localhost')
		server.set_debuglevel(0)
		server.sendmail(sender, recipients, msg)
		server.quit()
