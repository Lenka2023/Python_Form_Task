#!/usr/bin/env python3
import cgi

form = cgi.FieldStorage()
text1 = form.getfirst("TEXT_1", "not set")
text2 = form.getfirst("TEXT_2", "not set")
text3 = form.getfirst("TEXT_3", "not set")
print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>
Form Data Processing</title>
        </head>
        <body>""")

print("<h1>Form Data Processing!</h1>")
print("<p>TEXT_1: {}</p>".format(text1))
print("<p>TEXT_2: {}</p>".format(text2))
print("<p>TEXT_3: {}</p>".format(text3))
print("""</body>
        </html>""")