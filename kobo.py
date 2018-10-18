import urllib.request

def next_page():
    req = urllib.request.Request('http://localhost:3000/api/forward', method="POST")
    urllib.request.urlopen(req)

def previous_page():
    req = urllib.request.Request('http://localhost:3000/api/backward', method="POST")
    urllib.request.urlopen(req)
