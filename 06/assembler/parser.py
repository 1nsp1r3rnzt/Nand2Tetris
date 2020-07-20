import re
from symbol import symbol
from code import code
import sys
class parser():

	def __init__(self,file_name):
		'''
		Opens the input file/stream and gets ready to parse it.
		'''
		self.file_name = file_name
		self.symbol = symbol()
		self.current_command = ""
		self.file_ref = open(file_name, 'r+')
		self.code = code()


	def hasMoreCommands(self):
		'''
		returns a boolean if there is a next command.
				'''
		def helper_reset_pointer(pointer_position):
			self.file_ref.seek(pointer_position)        

		current_line_pointer = self.file_ref.tell()
		is_next_line = self.file_ref.readline()
		helper_reset_pointer(current_line_pointer)
		if is_next_line:
			return True
		else:
			return False
	   
	def advance(self):
		'''
		return next line/command
		'''
		return self.file_ref.readline()


	def commandType(self,current_command):
		'''
		A_COMMAND FOR @xxx where xxx is symbol or decimal number
		C_COMMAND -> dest=jump;jump
		L_COMMAND -> for (xxx) where Xxx is a symbol.
		return string
		'''
		types = ["A_COMMAND","L_COMMAND","C_COMMAND"]
		if current_command.startswith("@"):
			return types[0]
		elif current_command.startswith("("):
			return types[1]
		else:
			return types[2]


	def symbol():
		'''
		Returns the symbol or decimal Xxx of the current command
		@Xxx or (Xxx). Should be called only when commandType() is 
		A_COMMAND or L_COMMAND .
		'''
		return self.symbol.get_symbol()



	def dest(self,command):
		'''
		Returns the dest mnemonic in the current C-command (8 possi-bilities). 
		Should be called only when commandType() is C_COMMAND.
		'''
		dest_command = command
		if "=" in dest_command:
			dest_command = command.split("=")[0]
		else:
			dest_command = "null"
		return dest_command
	def is_variable(self,line):
		variable_name = self.get_label_name(line)
		if variable_name.isdigit():
			return False
		if re.search("^@",line):
			return True
		return False
	def get_dest(self,command):
		if "=" in command:
			dest = re.sub("=.*",'',command)
			return dest
		else:
			return "null"


	def comp(self,command):
		c_command = command
		if "=" in command:
			c_command = command.split("=")[1]
		if ";" in c_command:
			c_command = c_command.split(";")[0]
		return c_command


	def jump(self,command):

		"""
		Returns the jump mnemonic in
		the current C-command (8 pos-
		sibilities). Should be called only
		when commandType() is
		C_COMMAND.
		-> String
		"""
		jump_command = command
		if ";" in command:
			jump_command = jump_command.split(";")[1]
		else:
		   jump_command="null"
		return jump_command





































	def first_pass(self):
		'''
		build symbol table
		rom_address = keep a running number recording the ROM address into which the current command
		will be eventually loaded. 
		This number starts at 0 and is incremented by 1 whenever a C-instruction or an A-instruction is encountered, but does not change when a label
		pseudocommand or a comment is encountered.


		Each time a pseudocommand (Xxx) is encountered,
		 add a new entry to the symbol table, associating Xxx with the ROM
		address that will eventually store the next command in the program. 

		This pass results
		in entering all the program’s labels along with their ROM addresses into the symbol
		table. The program’s variables are handled in the second pass.

		'''
		rom_address = 0
		while(True):
			file_ref = self.file_ref
			if self.hasMoreCommands():
				current_command = self.advance()
				current_command = str.strip(current_command)
				if self.is_inline_comment(current_command):
					command_without_inline_comment = re.sub("//.*",'',current_command)
					current_command = command_without_inline_comment
				if self.is_comment(current_command) or self.is_empty_line(current_command):
					continue  #skip the current command
				elif self.commandType(current_command) is "L_COMMAND":
					label = re.sub("\(|\)",'',current_command)
					self.symbol.addEntry(label,rom_address)
					continue
				  # print(label)
				# line_list.append(current_command)
				rom_address = rom_address + 1
			else:
				break


	def is_comment(self,current_command):
		'''
		comment lines start with //
		'''
		return re.search("^//.*",current_command)


	def is_empty_line(self,current_command):
		'''
		True if the line is empty

		'''
		return re.search("^$",current_command)

	def is_inline_comment(self,current_command):
		return re.search(".*//.*",current_command)


	def second_pass(self):
		'''
		Each time a symbolic A-instruction is encountered, namely, @Xxx where Xxx is a symbol
		and not a number, look up Xxx in the symbol table. 

		If the symbol is found in the table, replace it with its numeric meaning 
				and complete the command’s translation.
		If the symbol is not found in the table, then it must represent a new variable.

		To handle it, add the pair (Xxx, n) to the symbol table, where n is the next available
		RAM address, and complete the command’s translation. 

		The allocated RAM
		addresses are consecutive numbers, starting at address 16 ( just after the addresses
		allocated to the predefined symbols).
		This completes the assembler’s implementation.
		'''

		instruction_list = []
		file_ref = self.file_ref
		file_ref.seek(0)

		while(True):
			if self.hasMoreCommands():

				current_command = self.advance()
				current_command = str.strip(current_command)
				if self.is_inline_comment(current_command):
					command_without_inline_comment = re.sub("//.*",'',current_command)
					current_command = command_without_inline_comment
				if self.is_comment(current_command) or self.is_empty_line(current_command):
					continue  #skip the current command
				elif self.commandType(current_command) is "A_COMMAND":
					a_command = re.sub("@",'',current_command)
					if not str.isdigit(a_command):
						# its LAbel or Variable
						if self.symbol.contain(a_command):
							label_address = str(self.symbol.get_address(a_command))
							a_command =str(label_address)
						else:
							variable_address = self.symbol.next_address
							self.symbol.addEntry(a_command,variable_address)
							self.symbol.increment_ram_address()                            
							a_command = str(variable_address)
					# A command
					a_binary = self.code.a_command_bits(a_command)
					instruction_list.append(a_binary)
				elif self.commandType(current_command) is "C_COMMAND":
					comp = self.comp(current_command)
					dest = self.dest(current_command)
					jump = self.jump(current_command)
					c_command_pre = "111"
					code_obj = self.code
					c_command = (c_command_pre+
						str(code_obj.get_a_bit(comp))+
						str(code_obj.comp(comp))+
						str(code_obj.dest(dest))+
						str(code_obj.jump(jump))
						)
					instruction_list.append(c_command)
			else:
				break
		return instruction_list


file_name = "Pong"
assembly_ext = ".asm"
hack_ext = ".hack"
pr = parser(file_name+assembly_ext)
pr.first_pass()
pr.symbol.print_symbols()

instruction_list = pr.second_pass()

f = open(file_name+hack_ext,"w")
for line in instruction_list:
  print(line)
  f.write(line)
  f.write("\n")
f.close()


