TT_INT = "INT"
TT_FLOAT = "FLOAT"
TT_PLUS = "PLUS"
TT_MINUS = "MINUS"
TT_MUL = "MUL"
TT_DIV = "DIV"
TT_LPAREN = "LPAREN"
TT_RPAREN = "RPAREN"

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
			return f'{self.type}:{self.value}'

		return f'{self.type}'


class Lexer:
	def __init__(self, srcContent: str):
		self.text = srcContent
		self.pos = -1
		self.current_char = None

	def advance(self):
		self.pos += 1
		self.current_char = self.text[pos] if self.pos < len(self.text) else None

	def peek(self, offset: int) -> str:
		peak_char = self.text[pos + offset] if self.pos < len(self.text) else None
		return peak_char

	def make_tokens(self) -> (list, Error):
		tokens = []

		while self.current_char != None:
			if self.current_char in '\t':
				self.advance()
			elif self.current_char in DIGITS:
				
				while self.current_char in DIGITS:
					self.advance()
				else:
					if self.current_char == "." and self.peek(1) in DIGITS:
						tokens.append(Token(TT_FLOAT))
						self.advance()
					elif self.current_char == "." and self.peek(1) not in DIGITS:
						return UnexpectedTokenError("Expected integer literal after \".\".")
					else:
						tokens.append(Token(TT_INT))
			elif self.current_char == '+':
				tokens.append(Token(TT_PLUS))
				self.advance()
			elif self.current_char == '-':
				tokens.append(Token(TT_MINUS))
				self.advance()
			elif self.current_char == '*':
				tokens.append(Token(TT_MUL))
				self.advance()
			elif self.current_char == '/':
				tokens.append(Token(TT_DIV))
				self.advance()
			elif self.current_char == '(':
				tokens.append(Token(TT_LPAREN))
				self.advance()
			elif self.current_char == ')':
				tokens.append(Token(TT_RPAREN))
				self.advance()

		return tokens
