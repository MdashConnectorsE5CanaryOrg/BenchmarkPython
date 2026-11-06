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
import os
from helpers.utils import escape_for_html

def init(app):

	@app.route('/benchmark/pathtraver-01/BenchmarkTest01180', methods=['GET'])
	def BenchmarkTest01180_get():
		return BenchmarkTest01180_post()

	@app.route('/benchmark/pathtraver-01/BenchmarkTest01180', methods=['POST'])
	def BenchmarkTest01180_post():
		RESPONSE = ""

		param = request.form.get("BenchmarkTest01180")
		if not param:
			param = ""


		import helpers.utils
		fd = None
		fileName = ""

		try:
			base_dir = os.path.abspath(helpers.utils.TESTFILES_DIR)
			fileName = os.path.abspath(os.path.join(base_dir, param))
			if os.path.commonpath([base_dir, fileName]) != base_dir:
				RESPONSE += (
					'File name must stay within the testfiles directory'
				)
				return RESPONSE
			fd = open(fileName, 'wb')
			RESPONSE += (
				f'Now ready to write to file: {escape_for_html(fileName)}'
			)
		except IOError as e:
			RESPONSE += (
				f'Problem reading from file \'{escape_for_html(fileName)}\': '
				f'{escape_for_html(e.strerror)}'
			)
		finally:
			try:
				if fd is not None:
					fd.close()
			except IOError:
				pass # "// we tried..."

		return RESPONSE

