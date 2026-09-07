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

	@app.route('/benchmark/weakrand-02/BenchmarkTest00768', methods=['GET'])
	def BenchmarkTest00768_get():
		return BenchmarkTest00768_post()

	@app.route('/benchmark/weakrand-02/BenchmarkTest00768', methods=['POST'])
	def BenchmarkTest00768_post():
		RESPONSE = ""

		values = request.args.getlist("BenchmarkTest00768")
		param = ""
		if values:
			param = values[0]

		TestParam = "This should never happen"
		if 'should' not in TestParam:
			bar = "Ifnot case passed"
		else:
			bar = param

		import secrets
		import time
		from helpers.utils import mysession

		num = 'BenchmarkTest00768'[13:]
		user = f'Nancy{num}'
		cookie = f'rememberMe{num}'
		stored = mysession.get(cookie)
		client_value = request.cookies.get(cookie)
		expires_at = time.time() + 3600

		if (
			isinstance(stored, dict)
			and stored.get('value') == client_value
			and stored.get('expires_at', 0) > time.time()
		):
			value = secrets.token_urlsafe(32)
			mysession[cookie] = {'value': value, 'expires_at': expires_at}
			response = make_response(
				f'Welcome back: {user}<br/>'
			)
		else:
			value = secrets.token_urlsafe(32)
			mysession[cookie] = {'value': value, 'expires_at': expires_at}
			response = make_response(
				f'{user} has been remembered.<br/>'
			)

		response.set_cookie(cookie, value, max_age=3600, httponly=True, samesite='Lax')
		return response
