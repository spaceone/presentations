#!/usr/bin/python
# taken from https://git.knut.univention.de/univention/ucsschool/blob/842f439e29d8415ff5b9bd5f293ef3a5c980f660/ucs-school-umc-printermoderation/umc/python/printermoderation/__init__.py#L151
# bugzilla Bug 38270
# Fixed in UCS@school 4.0 R2

import os

from univention.lib.i18n import Translation
from univention.management.console.modules import UMC_Error
from ucsschool.lib import SchoolBaseModule

CUPSPDF_DIR = '/var/spool/cups-pdf/'
CUPSPDF_USERSUBDIR = None

_ = Translation('ucs-school-umc-printermoderation').translate


class Instance(SchoolBaseModule):

	def download(self, request):
		"""Download a printjob of a specified user

		requests.options = {}
		'username' -- owner of the print job
		'filename' -- relative filename of the print job

		return: <PDF document>
		"""
		if request.options['username'].find('/') > 0 or request.options['printjob'].find('/') > 0:
			raise UMC_Error('Invalid file')

		path = os.path.join(CUPSPDF_DIR, request.options['username'], CUPSPDF_USERSUBDIR, request.options['printjob'])
		if not os.path.exists(path):
			raise UMC_Error('Invalid file')

		with open(path) as fd:
			response = fd.read()
		self.finished(request.id, response, mimetype='application/pdf')
