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

from flask import redirect, url_for, request, make_response, render_template, current_app
from helpers.utils import escape_for_html
from itsdangerous import BadSignature, SignatureExpired, URLSafeTimedSerializer

def init(app):

	@app.route('/benchmark/weakrand-00/BenchmarkTest00230', methods=['GET'])
	def BenchmarkTest00230_get():
		return BenchmarkTest00230_post()

	@app.route('/benchmark/weakrand-00/BenchmarkTest00230', methods=['POST'])
	def BenchmarkTest00230_post():
		RESPONSE = ""

		values = request.form.getlist("BenchmarkTest00230")
		param = ""
		if values:
			param = values[0]

		bar = param + '_SafeStuff'

		num = 'BenchmarkTest00230'[13:]
		user = f'SafeRobbie{num}'
		cookie = f'rememberMe{num}'
		serializer = URLSafeTimedSerializer(current_app.secret_key)
		max_age = 60 * 60 * 24 * 30
		cookie_value = request.cookies.get(cookie, '')

		try:
			remembered = serializer.loads(cookie_value, max_age=max_age)
		except (BadSignature, SignatureExpired):
			remembered = None

		if remembered == {'user': user, 'cookie': cookie}:
			RESPONSE += (
				f'Welcome back: {user}<br/>'
			)
			resp = make_response(RESPONSE)
		else:
			value = serializer.dumps({'user': user, 'cookie': cookie})
			RESPONSE += (
				f'{user} has been remembered.<br/>'
			)
			resp = make_response(RESPONSE)
			resp.set_cookie(cookie, value, max_age=max_age, httponly=True, samesite='Lax')

		return resp
