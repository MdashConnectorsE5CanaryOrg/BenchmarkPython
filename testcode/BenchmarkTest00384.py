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

	@app.route('/benchmark/weakrand-01/BenchmarkTest00384', methods=['GET'])
	def BenchmarkTest00384_get():
		return BenchmarkTest00384_post()

	@app.route('/benchmark/weakrand-01/BenchmarkTest00384', methods=['POST'])
	def BenchmarkTest00384_post():
		RESPONSE = ""

		param = ""
		for name in request.form.keys():
			if "BenchmarkTest00384" in request.form.getlist(name):
				param = name
				break

		import base64
		tmp = base64.b64encode(param.encode('utf-8'))
		bar = base64.b64decode(tmp).decode('utf-8')

		import secrets
		from helpers.utils import mysession

		num = 'BenchmarkTest00384'[13:]
		user = f'Nancy{num}'
		cookie = f'rememberMe{num}'
		session_key = f'{user}:{cookie}'
		cookie_value = request.cookies.get(cookie)

		if session_key in mysession and cookie_value == mysession[session_key]:
			RESPONSE += (
				f'Welcome back: {user}<br/>'
			)
			response = make_response(RESPONSE)
		else:
			value = secrets.token_urlsafe(32)
			mysession[session_key] = value
			RESPONSE += (
				f'{user} has been remembered.<br/>'
			)
			response = make_response(RESPONSE)
			response.set_cookie(cookie, value, httponly=True, samesite='Lax')

		return response
