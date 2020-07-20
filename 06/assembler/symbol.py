class symbol():

	def __init__(self):
		'''
		 Creates a new empty symbol table.
		 '''
		self.symbols_table = {
			"R0": 0,
		"R1": 1,
		"R2" :2 ,
		"R3" : 3,
		"R4" :4,
		"R5" : 5,
		"R6" : 6,
		"R7" : 7,
		"R8" : 8,
		"R9" : 9,
		"R10" : 10,
		"R11" : 11,
		"R12" : 12,
		"R13" : 13,
		"R14" : 14,
		"R15" : 15,
		"SCREEN" : 16384,
		"KBD" : 24576,
		"SP" : 0,
		"LCL" : 1,
		"ARG" : 2,
		"THIS" : 3,
		"THAT" : 4,
		}
		self.next_address = 16


	def contain(self,symbol):
		'''
		string -> Boolean
		 returns true if the symbol table contain
		the given symbol.
		'''
		return symbol in self.symbols_table.keys()

	def get_address(self,symbol):
		'''
		 Returns the address associated with the symbol.
		'''
		return self.symbols_table[symbol]

	def addEntry(self,symbol, address):
		'''
		 Adds the pair (symbol,  address) to the table.

		'''
		if symbol not in self.symbols_table:
			self.symbols_table[symbol] = address

	def increment_ram_address(self):
		self.next_address = self.next_address + 1

	def print_symbols(self):
		print(self.symbols_table)


	

