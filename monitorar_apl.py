import requests

try:
    response = requests.get("http://localhost:8080")
    if response.status_code == 200:
        print("Servidor está acessível.")
    else:
        print(f"Erro ao acessar o servidor: {response.status_code}")
except requests.ConnectionError as e:
    print(f"Erro de conexão: {e}")