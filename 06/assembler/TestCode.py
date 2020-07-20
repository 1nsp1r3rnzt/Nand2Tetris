from code import code
import unittest

class TestCode(unittest.TestCase):
	"""
	Test cases
	"""

	def test_get_a_bit(self):
		"""
		a = 0 when M is not present in command
		
		"""
		code_obj = code()
		a_command = code_obj.get_a_bit("A+1")
		m_command = code_obj.get_a_bit("M+1")
		a_zero_example  = code_obj.get_a_bit("0;jmp")
		self.assertEqual(a_command,0)
		self.assertEqual(m_command,1)


	def test_a_command_bits(self):
		"""
		a = 0 when M is not present in command
		
		"""
		code_obj = code()
		a_example = code_obj.a_command_bits("16")
		self.assertEqual(a_command,0)
		self.assertEqual(m_command,1)






if __name__ == '__main__':
	unittest.main()