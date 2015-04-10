from django.test import TestCase, RequestFactory,Client
from django.http import HttpRequest
from User.models import User
from User.views import user_signup_save,login

class UserTests(TestCase):
    
    def test_valid_user_saves(self):
        number_of_users = User.objects.count()
        request = HttpRequest()
        request.method='POST'
        
        request.POST['fname'] = 'john'
        request.POST['lname'] = 'doe'
        request.POST['email'] = 'jdoe@gmail.com'
        request.POST['password'] = 'michelle'
        response = user_signup_save(request)
        self.assertEqual(number_of_users +1, User.objects.count())
    def test_invalid_users_dont_save(self):
    	number_of_users = User.objects.count()
        request = HttpRequest()
        request.method='POST'
        
        request.POST['fname'] = ''
        request.POST['lname'] = ''
        request.POST['email'] = ''
        request.POST['password'] = ''
        response = user_signup_save(request)
        self.assertEqual(number_of_users , User.objects.count())
    def test_password_is_hashed(self):
    	user = User.objects.create_user(fname='john',lname='doe',email='jdoe@gmail.com',password='michelle')
    	self.assertNotEqual('michelle',User.objects.first().password)
    	self.assertTrue(User.objects.first().check_password('michelle'))
    
    def test_registered_user_can_login(self):
    	user = User.objects.create_user(fname='john',lname='doe',email='jdoe@gmail.com',password='michelle')
    	request = HttpRequest()
    	request.method = 'POST'
    	request.POST['email'] = user.email
    	request.POST['password'] = user.password
    	response = login(request)
    	self.assertEqual(self.client.session['email'], user.email)
    def test_unregistered_user_cant_login(self):
    	#Create an instance of User, but don't save it into database
    	user = User(fname='john',lname='doe',email='jdoe@gmail.com',password='michelle')
    	request = HttpRequest()
    	request.method = 'POST'
    	request.POST['email'] = 'jdoe@gmail.com'
    	request.POST['password'] = 'michelle'
    	response = login(request)
    	print response.status_code
    	self.assertTrue(user.is_authenticated())

    
        
