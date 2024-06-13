import openai

# Configura tu clave de API de OpenAI
openai.api_key = 'fiorefer2282'

def obtener_respuesta_chatgpt(consulta):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",  # Puedes cambiar a otro modelo si lo prefieres
            prompt=consulta,
            max_tokens=150
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Error al obtener la respuesta de la API: {e}"

def main():
    consulta = input("Por favor, ingrese su consulta: ").strip()

    if not consulta:
        print("La consulta está vacía. Por favor, ingrese un texto válido.")
        return

    print(f"Consulta ingresada: {consulta}")

    respuesta = obtener_respuesta_chatgpt(consulta)
    print(f"Respuesta de ChatGPT: {respuesta}")

if __name__ == "__main__":
    main()