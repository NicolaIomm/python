import time
import sys

# In python3 il segnale SIGINT(lanciato alla pressione di Ctrl+C) viene gestito
# come un'eccezione KeyboardInterrupt

try:
    i = 1
    while (True):
        time.sleep(1)
        print("..%d"%i)
        i+=1
except KeyboardInterrupt:
    print("Segnale di terminazione ricevuto!")
    sys.exit(0)
