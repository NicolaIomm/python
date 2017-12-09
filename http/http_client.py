# Breve spiegazione delle principali funzionalita del modulo http.client

import http.client

    # Questa è un oggetto connessione HTTP
connection = http.client.HTTPConnection("www.python.it")
connectionS = http.client.HTTPSConnection("www.python.org")

    # Effettuo richiesta HTTP
    # HTTPConnection.request(method, url, body=None, headers={}, *, encoded_chunked=False)
connection.request("GET", "/")

    # Leggo la risposta alla mia richiesta per poi analizzarla
response = connection.getresponse()

    # Estrapola in lista tutti gli header della risposta
headers = response.getheaders()
print("--> Lista headers: ",headers)

    # Estrapola il valore per l'header specifico
date = response.getheader("Date")
print("--> Data:",date)

    # Estrapola lo stato della richiesta
status = response.status
reason = response.reason
print("--> Status:",status)
print("--> Reason:",reason)

    # Estrapola l'intero body della risposta, convertendolo da flusso di byte a stringa
body = response.read().decode() 
print("---> Body:",body)
