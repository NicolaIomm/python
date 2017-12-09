import ssl
import urllib.parse
import urllib.request

    # Crea contesto https
ssl._create_default_https_context = ssl._create_unverified_context

client_id = "0b0257f3ab104ffc89c6f4529161b19c"
response_type = "code"
redirect_uri = urllib.parse.quote("https://www.spotify.com/it/", safe='') 
scope = urllib.parse.quote("user-follow-read", safe='')
url = ("https://accounts.spotify.com/authorize/?client_id="+client_id+
        "&response_type="+response_type+
        "&redirect_uri="+redirect_uri+
        "&scope="+scope)

    # avvio la funzione di collegamento a url

print(url)
print("***************************")
response = urllib.request.urlopen(url)

body = response.read().decode()
print(body)
