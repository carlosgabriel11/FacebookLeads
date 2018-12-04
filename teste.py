import mechanize

url = 'https://m.facebook.com'
loggedin_title = 'Facebook' # isto vai servir para confirmarmos que estamos loggedin, vendo o titulo da pagina para onde fomos redirecionados 
username = 'USERNAME'
password = 'PASSWORD'

browser = mechanize.Browser()
browser.set_handle_robots(False)
browser.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.0.6)')]

browser.open(url)
browser.select_form(nr=0)
browser.form["email"] = username
browser.form["pass"] = password
browser.submit()

if browser.title() == loggedin_title:
    print '[+] SUCCESS'
    print 'Username: {}\nPassword: {}'.format(username, password)
else:
    print '[-] LOGIN FAILED
