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

from flask import redirect, url_for, request, make_response, render_template, session
from helpers.utils import escape_for_html

def init(app):

	@app.route('/benchmark/weakrand-02/BenchmarkTest00795', methods=['GET'])
	def BenchmarkTest00795_get():
		return BenchmarkTest00795_post()

	@app.route('/benchmark/weakrand-02/BenchmarkTest00795', methods=['POST'])
	def BenchmarkTest00795_post():
		RESPONSE = ""

		values = request.args.getlist("BenchmarkTest00795")
		param = ""
		if values:
			param = values[0]

		possible = "ABC"
		guess = possible[1]
		
		match guess:
			case 'A':
				bar = param
			case 'B':
				bar = 'bob'
			case 'C' | 'D':
				bar = param
			case _:
				bar = 'bob\'s your uncle'

		import random

		num = 'BenchmarkTest00795'[13:]
		user = f'SafeRandall{num}'
		cookie = f'rememberMe{num}'
		token_key = f'{cookie}_token'
		value = str(random.SystemRandom().random())[2:]

		remembered_cookie = request.cookies.get(cookie)
		session_token = session.get(token_key)

		if remembered_cookie and session_token and remembered_cookie == session_token:
			RESPONSE += (
				f'Welcome back: {user}<br/>'
			)
		else:
			session[token_key] = value
			RESPONSE += (
				f'{user} has been remembered.<br/>'
			)

		response = make_response(RESPONSE)
		if session.get(token_key) and remembered_cookie != session.get(token_key):
			response.set_cookie(cookie, session[token_key], httponly=True, samesite='Lax')

		return response
