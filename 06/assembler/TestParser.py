from parser import parser
import unittest

class TestParser(unittest.TestCase):
	"""
	Test cases
	"""

	def test_comp(self):
		parse = parser("Demo.asm")
		c_command_alone = parse.comp("M+1")
		c_command_with_jump = parse.comp("M+1;JTE")
		c_command_with_dest = parse.comp("M=M+1")
		c_command_with_dest_jump = parse.comp("M=M+1;JTE")
		self.assertEqual(c_command_alone,"M+1")
		self.assertEqual(c_command_with_jump,"M+1") 
		self.assertEqual(c_command_with_dest,"M+1") 
		self.assertEqual(c_command_with_dest_jump,"M+1") 


	def test_dest(self):
		parse = parser("Demo.asm")
		dest_command_alone = parse.dest("M=M+1")
		dest_command_with_jump = parse.dest("M=M+1;JTE")
		no_dest_command= parse.dest("M+1;JTE")
		self.assertEqual(dest_command_with_jump,"M") 
		self.assertEqual(dest_command_with_jump,"M") 
		self.assertEqual(no_dest_command,"null") 

	def test_jump(self):
		parse = parser("Demo.asm")
		no_jump = parse.jump("M=M+1")
		jump_command_with_jump = parse.jump("M=M+1;JTE")
		self.assertEqual(no_jump,"null") 
		self.assertEqual(jump_command_with_jump,"JTE") 


if __name__ == '__main__':
	unittest.main()