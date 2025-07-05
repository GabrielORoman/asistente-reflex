import reflex as rx
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

# Función que llama a ChatGPT
def consultar_ia(pregunta):
    respuesta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Usamos el modelo gratuito o económico
        messages=[{"role": "user", "content": pregunta}]
    )
    return respuesta['choices'][0]['message']['content']

# Estado para guardar pregunta y respuesta
class Estado(rx.State):
    pregunta: str = ""
    respuesta: str = ""

    def hacer_pregunta(self):
        self.respuesta = consultar_ia(self.pregunta)

# Interfaz principal
def index():
    return rx.center(
        rx.vstack(
            rx.heading("🤖 Asistente con IA", size="lg"),
            rx.input(placeholder="Escribí tu pregunta", on_change=Estado.set_pregunta),
            rx.button("Consultar", on_click=Estado.hacer_pregunta),
            rx.text("Respuesta:", weight="bold"),
            rx.text(Estado.respuesta, padding="10px", color="blue"),
            spacing="2em"
        ),
        height="100vh"
    )

# App
app = rx.App()
app.add_page(index)
app.compile()
