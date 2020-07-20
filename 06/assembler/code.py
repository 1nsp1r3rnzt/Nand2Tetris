class code():


		
# C command tables
# 
# 
# Table for dest
#  table for comp
#   table for jump.

	def dest_table(self):
		dest = {
		"null": "000",
		"M" : "001",
		"D" : "010",
		"MD" : "011",
		"A" : "100",
		"AM" : "101",
		"AD" : "110",
		"AMD" : "111",
		}

		return dest

	def comp_table(self):
		comp = {
		"0"  :"101010",
		"1"  :"111111",
		"-1" :"111010",
		"D"  :"001100",
		"A"  :"110000",
		"!D" :"001101",
		"!A" :"110001",
		"-D" :"00111",
		"-A" :"110011",
		"D+1":"011111",
		"A+1":"110111",
		"D+A":"000010",
		"D-1":"001110",
		"A-1":"110010",
		"D+A":"000010",
		"D-A":"010011",
		"A-D":"000111",
		"D&A":"000000",
		"D|A":"010101",
		"M"  :"110000",
		"!M" :"110001",
		"-M" :"110011",
		"M+1":"110111",
		"M-1":"110010",
		"D+M":"000010",
		"D-M":"010011",
		"M-D":"000111",
		"D&M":"000000",
		"D|M":"010101",
		}
		return comp



	def jump_table(self):
		jump_table = {


		"null": "000",
		"JGT": "001",
		"JEQ": "010",
		"JGE": "011",
		"JLT": "100",
		"JNE": "101",
		"JLE": "110",
		"JMP": "111",
		}
		return jump_table


	def get_a_bit(self, command):
		if "M" in command:
			return 1
		else:
			return 0


	# def get_destination(self,command):
	#             '''
	#     C-instruction:dest1⁄4comp;jump
	#      // Either the dest or jump fields may be empty.
	#     // If dest is empty, the ‘=’ is omitted;
	#     // If jump is empty, the ‘‘;’’ is omitted.
	#     '''
	#     return 0


	def a_command_bits(self,command):
		binary_number = bin(int(command))
		binary_number = binary_number.replace("0b",'')
		a_command_pre = "0"
		filler_zero_length= 16-len(a_command_pre)-len(binary_number)
		return a_command_pre+str("0"*filler_zero_length)+str(binary_number)


	def comp(self, command):
		'''
		Returns the binary code of the comp mnemonic.
		'''
		if command in self.comp_table().keys():
			return self.comp_table().get(command)
		else:
			print(command+"_____")
			return "000000"


	def dest(self, command):
		'''
		 Returns the 3bit binary code of the dest mnemonic.
		'''
		if command in self.dest_table().keys():
			return self.dest_table().get(command)
		else:
			return "000"



	def jump(self, command):
		'''
		 Returns the binary code of the jump mnemonic.
		'''
		if command in self.jump_table().keys():
			return self.jump_table().get(command)
		else:
			return "000"