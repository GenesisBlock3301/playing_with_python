from bs4 import BeautifulSoup

st = """<html>
    <head><title>I'm title</title></head>
    """
st1 = "who are you"

print(bool(BeautifulSoup(st, "html.parser").find()))
print(bool(BeautifulSoup(st1, "html.parser").find()))
