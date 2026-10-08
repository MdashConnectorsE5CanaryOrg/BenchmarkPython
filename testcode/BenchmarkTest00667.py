'''
OWASP Benchmark for Python v0.1

This file is part of the Open Web Application Security Project (OWASP) Benchmark Project.
For details, please see https://owasp.org/www-project-benchmark.

The OWASP Benchmark is free software: you can redistribute it and/or modify it under the terms
of the GNU General Public License as published by the Free Software Foundation, version 3.

The OWASP Benchmark is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR
PURPOSE. See the GNU General Public License for more details.

  Author: Theo Cartsonis
  Created: 2025
'''

from flask import redirect, url_for, request, make_response, render_template
from helpers.utils import escape_for_html

def init(app):

	@app.route('/benchmark/pathtraver-01/BenchmarkTest00667', methods=['GET'])
	def BenchmarkTest00667_get():
		return BenchmarkTest00667_post()

	@app.route('/benchmark/pathtraver-01/BenchmarkTest00667', methods=['POST'])
	def BenchmarkTest00667_post():
		RESPONSE = ""

		param = request.args.get("BenchmarkTest00667")
		if not param:
			param = ""

		import configparser
		
		bar = 'safe!'
		conf88272 = configparser.ConfigParser()
		conf88272.add_section('section88272')
		conf88272.set('section88272', 'keyA-88272', 'a-Value')
		conf88272.set('section88272', 'keyB-88272', param)
		bar = conf88272.get('section88272', 'keyB-88272')

		import errno
		import helpers.utils
		import os

		fileName = ''
		try:
			base_dir = os.path.abspath(helpers.utils.TESTFILES_DIR)
			fileName = os.path.abspath(os.path.join(base_dir, bar))
			if os.path.commonpath([base_dir, fileName]) != base_dir:
				raise OSError(errno.EINVAL, 'Invalid filename')
			with open(fileName, 'wb') as fd:
				RESPONSE += (
					f'Now ready to write to file: {escape_for_html(fileName)}'
				)
		except IOError as e:
			RESPONSE += (
				f'Problem reading from file \'{escape_for_html(fileName)}\': '
				f'{escape_for_html(e.strerror)}'
			)

		return RESPONSE
