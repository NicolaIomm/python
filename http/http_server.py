# Breve descrizione dei fondamentali usi per il modulo http.server (WebServer)

import http.server

    # Creo un web server su server_address,
    # a cui assegno un oggetto che gestisce le richieste
    # Tale oggetto puo essere:
    #       - BaseHTTPRequestHandler (è necessario creare sottoclasse)
    #       - SimpleHTTPRequestHandler (dispone le risorse in una gerarchia da filesystem)
    #       - CGIHTTPRequestHandler (come il precedente piu script CGI)

class myHttpRequestHandler(http.server.BaseHTTPRequestHandler):
        # funzione che gestisce le richieste GET
    def do_GET(self):   # self in python come this in java
            #   Variabili utili per self :       
            #       self.requestline contiene l'intera linea della richiesta
            #       self.path contiene il path della risorsa richiesta
            #       self.rfile contiene lo stream di lettura usato per comunicare
            #       self.wfile contiene lo stream per la scrittura
        if (self.path == "/ciao"):
            # Send response status code
            self.send_response(200, "OK")
     
            # Send headers
            self.send_header('Content-type','text/html')
            self.end_headers()  #write blank line and call self.flush_headers()
    
            # Send message back to client
            message = "Hai richiesto la risorsa '/ciao' !"
            # Write content as byte stream
            self.wfile.write(message.encode()) # altro modo di convertire stringa a flusso di byte: bytes("ciao", "utf8")
        return

    # server address as tuple (address, port)
server_address = ("127.0.0.1", 3000)
    # creo l'oggetto server specificando server_address e gestore delle richieste
webserver = http.server.HTTPServer(server_address, myHttpRequestHandler)
    # comunico al server di rispondere per sempre alle richieste
webserver.serve_forever()
