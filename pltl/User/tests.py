from django.test import TestCase
import unittest

class UserTest(unittest.TestCase):
	def test_Fname_is_not_null(self):
		user = User()
		self.assertEqual(user.Fname,'')

# Create your tests here.
