import html5lib

html5parser = html5lib.HTMLParser(strict=True)

try:
    p = html5parser.parse(""" <!DOCTYPE html>
<html>
<head>
<title>Page Title</title>
</head>
<body>

<h1>This is a Heading</h1>
<p>This is a paragraph.</p>

</body>
</htm>
""")
except:
    p = False

if p:
    print("OK")
else:
    print("No")
print(p)