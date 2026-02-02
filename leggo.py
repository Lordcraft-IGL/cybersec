nomefile = "logfile.txt"
try: 
  f = open(nomefile, "r", encoding='utf-8')
  righe = f.readlines()
  for riga in righe:
    print(riga, end = '')
except FileNotFoundError as e:
  primt(f"[-] Errore bloccante: {str(e)}")
