import requests
import logging

# Configurações
BASE_URL = "http://localhost:8080"  # URL base da aplicação WordPress
LOGIN_ENDPOINT = "/wp-login.php"
DASHBOARD_ENDPOINT = "/wp-admin"
USERNAME = "alex"  
PASSWORD = "alex1234"  

# configuração do logger
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def verificar_disponibilidade():
    try:
        response = requests.get(BASE_URL, timeout=5)
        if response.status_code == 200:
            logging.info("A aplicação está disponível.")
        else:
            logging.error(f"Erro ao acessar a aplicação. Código de status: {response.status_code}")
    except requests.exceptions.RequestException as e:
        logging.error(f"Erro de conexão: {e}")

def verificar_autenticacao():
    session = requests.Session()
    try:
        # Realiza uma requisição inicial para capturar cookies
        session.get(BASE_URL + LOGIN_ENDPOINT, timeout=5)

        # Dados de login
        login_data = {
            "log": USERNAME,
            "pwd": PASSWORD,
            "wp-submit": "Acessar",
            "redirect_to": BASE_URL + DASHBOARD_ENDPOINT,
            "testcookie": "1"
        }

        # Envio da requisição de login
        response = session.post(BASE_URL + LOGIN_ENDPOINT, data=login_data, timeout=5)

        if response.status_code == 200 and DASHBOARD_ENDPOINT in response.url:
            logging.info("Autenticação bem-sucedida. Painel administrativo acessado.")
        else:
            logging.error(
                f"Falha na autenticação. Verifique as credenciais. Resposta: {response.text[:500]}"
            )
    except requests.exceptions.RequestException as e:
        logging.error(f"Erro durante a autenticação: {e}")

def monitorar_aplicacao():
    logging.info("Iniciando monitoramento da aplicação.")
    verificar_disponibilidade()
    verificar_autenticacao()

if __name__ == "__main__":
    monitorar_aplicacao()
