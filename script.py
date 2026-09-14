import os
import requests

def main():
    # Leer el token desde la variable de entorno
    api_token = os.getenv("API_TOKEN")
    if not api_token:
        raise ValueError("API_TOKEN no está definido en el entorno")

    # Endpoint de ejemplo
    url = "https://api.example.com/data"

    # Cabeceras con autenticación
    headers = {
        "Authorization": f"Bearer {api_token}",
        "Accept": "application/json"
    }

    print("Llamando a la API...")

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()

        print("Respuesta recibida:")
        print(data)

    except requests.exceptions.RequestException as e:
        print(f"Error al llamar a la API: {e}")

if __name__ == "__main__":
    main()
