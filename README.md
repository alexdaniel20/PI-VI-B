# Monitoramento de Aplicação WordPress

Este projeto é uma solução para monitorar a disponibilidade e autenticação de uma aplicação WordPress local. Ele verifica se a aplicação está ativa e se as credenciais fornecidas permitem acesso ao painel administrativo.

## Funcionalidades

- **Verificação de Disponibilidade**: Testa se a aplicação WordPress está acessível.
- **Autenticação**: Verifica se o login com credenciais fornecidas é bem-sucedido.
- **Logs**: Registra mensagens de erro e sucesso para facilitar o diagnóstico.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal.
- **Biblioteca Requests**: Usada para enviar requisições HTTP.
- **Biblioteca Logging**: Usada para registrar logs de execução.

## Requisitos

Antes de executar o projeto, certifique-se de ter:

- Python 3.7 ou superior instalado.
- Uma aplicação WordPress em execução localmente no endereço `http://localhost:8080`.
- Credenciais válidas para acesso ao WordPress.

## Instalação

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

2. Crie um ambiente virtual (opcional, mas recomendado):

```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

## Configuração

Edite as variáveis no arquivo principal do projeto para corresponder às suas credenciais e configuração:

```python
BASE_URL = "http://localhost:8080"  # URL base da aplicação WordPress
USERNAME = "seu_usuario"  # Substitua pelo seu usuário
PASSWORD = "sua_senha"  # Substitua pela sua senha
```

## Execução

Para iniciar o monitoramento, execute o script principal:

```bash
python monitoramento.py
```

## Estrutura do Projeto

```
├── monitoramento.py  # Código principal do projeto
├── README.md         # Documentação do projeto
├── requirements.txt  # Dependências do projeto
└── .gitignore        # Arquivos a serem ignorados pelo Git
```

## Logs

Os logs de execução serão exibidos no console e contêm informações sobre:
- Status de disponibilidade da aplicação.
- Sucesso ou falha na autenticação.
- Mensagens detalhadas de erro em caso de falha.

