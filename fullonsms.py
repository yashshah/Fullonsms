#!/usr/bin/python 

#
# Script to send SMS via Fullonsms
#
# @author Yash Shah
# @license BSD License
# 
import cookielib
import urllib2
import getpass
import urllib

# To fool fullonsms as if a Web browser is visiting the site
user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1'
headers = { 'User-Agent' : user_agent }

#Set the username ( Mobile no ) and password here
username = ''
password = ''


def sendMessage(username='',password='',number='',message=''):
  print "\nKindly enter your login details:"
  if not username: username = raw_input("Enter Mobile number/Username: ")
  if not password: password = getpass.getpass("Enter Password: ")
  username, password = username.strip(), password.strip()
  print "Attempting to Login..."
  
  #Logging into the SMS Site
  url = 'http://www.fullonsms.com/login.php'
  values = {'MobileNoLogin' : username,
          'LoginPassword' : password,
          'Submit' : 'LoginForm' }
  data = urllib.urlencode(values)
  req = urllib2.Request(url, data)

#Remember, Cookies are to be handled
  cj = cookielib.CookieJar()
  opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
  opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1')]
  
  try:
    response = opener.open(url, data)
    the_page = response.read()
  
  except IOError:
    print "Check your internet connection"
    sys.exit(1)
	  
  Login_status = 'landing' in the_page
  print "-","Login Successful!!\n" if Login_status else "Login Failed, check your mobile number & password!!\n"
#  return Login_status

#def sendMessage(number='',message=''):
  while True:
    if not number: number = raw_input("Enter Mobile number: ")
    if not message : message = raw_input("Enter Message: ")

    
    #urlencode performed.. Because it was done by the site as i checked through HTTP headers
      
    #message = urlencode({'message':message})
    #message = message[message.find("=")+1:]
    #SMS sending
    send_sms_url = 'http://www.fullonsms.com/home.php'
    send_sms_data = urllib.urlencode({'MobileNos': number,
				'Message': message})
  #	opener.addheaders = [('Referer','http://www.fullonsms.com/home.php')]
    
      
    try:
      response = opener.open(send_sms_url, send_sms_data)
      the_page = response.read()
      print "Message sent successfully!!\n"
	    
    except IOError:
      print "Check your internet connection( while sending sms)"
      sys.exit(1)
    message=None

if __name__ == "__main__":
    sendMessage(username,password)
#    if(a is True):
#      sendMessage()