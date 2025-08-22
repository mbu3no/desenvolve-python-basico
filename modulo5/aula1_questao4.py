from datetime import datetime

agora = datetime.now()

data = f"{agora.day:02d}/{agora.month:02d}/{agora.year}"
hora = f"{agora.hour:02d}:{agora.minute:02d}"

print(f"Data: {data}")
print(f"Hora: {hora}")
