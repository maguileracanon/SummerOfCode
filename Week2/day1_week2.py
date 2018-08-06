# Day1_Week2
import unittest
from day1Class_week2 import myPrint

myPrint(2)

class TestMoo(unittest.TestCase):
	def test0(self):
		self.assertEqual(myPrint(0),'')
	def test1(self):
		self.assertEqual(myPrint(1),'moo')
	def test2(self):
		self.assertEqual(myPrint(2),'moomoo')
	def test3(self):
		self.assertEqual(myPrint(3),'moomoomoo')		
unittest.main()