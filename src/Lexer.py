TT_INT = "INT"
TT_FLOAT = "FLOAT"
TT_PLUS = "PLUS"
TT_MINUS = "MINUS"
TT_MUL = "MUL"
TT_DIV = "DIV"
TT_LPAREN = "LPAREN"
TT_RPAREN = "RPAREN"
TT_LCURLY = "LCURLY"
TT_RCURLY = "RCURLY"
TT_END_STATEMENT = "END_STATEMENT"

DIGITS = "0123456789"


class Error:
	def __init__(self, error_name: str, details: str):
		self.name = error_name
		self.details = details

	def as_string(self) -> str:
		return f"{self.name}: {self.details}"


class UnexpectedTokenError(Error):
	def __init__(self, details):
		super().__init__("UnexpectedTokenError", details)


class Token:
	def __init__(self, type_, value):
		self.type = type_
		self.value = value

	def __repr__(self):
		if self.value:
			return f'{self.type}: {self.value}'

		return f'{self.type}'


class Lexer:
	def __init__(self, srcContent: str):
		self.text = srcContent
		self.pos = -1
		self.current_char = None

	def advance(self):
		self.pos += 1
		self.current_char = self.text[self.pos] if self.pos < len(self.text) else None

	def peek(self, offset: int, sub=False) -> str:
		if not sub:
			peak_char = self.text[self.pos + offset] if self.pos < len(self.text) else None
		else:
			peak_char = self.text[self.pos - offset] if self.pos < len(self.text) else None

		return peak_char

	def make_tokens(self) -> (list, Error):
		tokens = []

		self.advance()

		while self.current_char != None:
			if self.current_char in '\t':
				self.advance()
			elif self.current_char in DIGITS:
				tok = ""

				while self.current_char in DIGITS:
					tok += self.current_char
					self.advance()
				else:
					if self.current_char == "." and self.peek(1) in DIGITS:
						self.advance()
						tok += "."
						while self.current_char in DIGITS:
							tok += self.current_char
							self.advance()

						tokens.append(Token(TT_FLOAT, tok))
					elif self.current_char == "." and self.peek(1) not in DIGITS:
						return UnexpectedTokenError("Expected integer literal after \".\"")
					else:
						tokens.append(Token(TT_INT, tok))
			elif self.current_char == '+':
				tokens.append(Token(TT_PLUS, self.current_char))
				self.advance()
			elif self.current_char == '-':
				tokens.append(Token(TT_MINUS, self.current_char))
				self.advance()
			elif self.current_char == '*':
				tokens.append(Token(TT_MUL, self.current_char))
				self.advance()
			elif self.current_char == '/':
				tokens.append(Token(TT_DIV, self.current_char))
				self.advance()
			elif self.current_char == '(':
				tokens.append(Token(TT_LPAREN, self.current_char))
				self.advance()
			elif self.current_char == ')':
				tokens.append(Token(TT_RPAREN, self.current_char))
				self.advance()
			elif self.current_char == '{':
				tokens.append(Token(TT_LCURLY, self.current_char))
				self.advance()
			elif self.current_char == '}':
				tokens.append(Token(TT_RCURLY, self.current_char))
				self.advance()
			else:
				self.advance()

		return tokens
