import os
import requests

api_token = os.getenv("API_TOKEN")

if not api_token:
    raise ValueError("API_TOKEN no está definido")

response = requests.get(
    "https://api.github.com/user",
    headers={
        "Authorization": f"Bearer {api_token}",
        "Accept": "application/vnd.github+json"
    }
)

print(response.status_code)

if response.ok:
    user = response.json()
    print(f"Token válido. Usuario: {user['login']}")
else:
    print("Token inválido o sin autorización")
    print(response.text)
