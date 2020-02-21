import urllib

def isReachable(): 
    return urllib.urlopen("http://localhost:8080/sample").getcode()

def test_answer():
    assert isReachable() == 200
