from webbot import Browser
web = Browser()
web.go_to('google.com')
web.type('')  
# or web.press(web.Key.SHIFT + 'hello its me')
web.press(web.Key.ENTER)
#!/usr/bin/env python3
