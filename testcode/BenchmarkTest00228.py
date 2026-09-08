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

	@app.route('/benchmark/weakrand-00/BenchmarkTest00228', methods=['GET'])
	def BenchmarkTest00228_get():
		return BenchmarkTest00228_post()

	@app.route('/benchmark/weakrand-00/BenchmarkTest00228', methods=['POST'])
	def BenchmarkTest00228_post():
		RESPONSE = ""

		values = request.form.getlist("BenchmarkTest00228")
		param = ""
		if values:
			param = values[0]

		import html
		
		bar = html.escape(param)

		from itsdangerous import BadSignature, SignatureExpired, URLSafeTimedSerializer

		num = 'BenchmarkTest00228'[13:]
		user = f'SafeRobbie{num}'
		cookie = f'rememberMe{num}'
		serializer = URLSafeTimedSerializer(app.secret_key, salt=cookie)
		max_age = 60 * 60 * 24 * 30

		token = request.cookies.get(cookie)
		if token:
			try:
				remembered_user = serializer.loads(token, max_age=max_age)
			except (BadSignature, SignatureExpired):
				remembered_user = None
			if remembered_user == user:
				RESPONSE += (
					f'Welcome back: {user}<br/>'
				)
				return RESPONSE

		signed_token = serializer.dumps(user)
		response = make_response()
		response.set_cookie(cookie, signed_token, max_age=max_age, httponly=True, samesite='Lax')
		RESPONSE += (
			f'{user} has been remembered by the server.<br/>'
		)
		response.set_data(RESPONSE)
		return response
