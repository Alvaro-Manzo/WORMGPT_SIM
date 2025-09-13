"""ESTO ES UNA IA QUE SIMULA SER UN WORMGPT
ESTE SOLO ES UN EJEMPLO DE CÓMO PODRÍA SER UN BOT ASÍ
NO ES UN BOT REAL, SOLO SIMULA SERLO
NO HACE NADA ILEGAL, SOLO SIMULA RESPUESTAS
NO ES RESPONSABLE DE NINGÚN USO ILEGAL QUE SE LE DÉ
ES SOLO UN EJEMPLO EDUCATIVO 
¡PARA USO PERSONAL Y EDUCATIVO NO COMERCIAL NI PARA DAÑAR A NADIE!
BY: ALVARO MANZO"""


import asyncio
import os
import logging
from datetime import datetime
from chatbot import ChatbotUnico, BotConfig

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('bot.log'),
        logging.StreamHandler()
    ]
)

async def chat_interactivo():
    """Función para probar el chatbot de forma interactiva"""
    
    # Configurar el bot - usar config que ya incluye la API key hardcodeada
    config = BotConfig()
    
    try:
        # Crear instancia del bot
        bot = ChatbotUnico(config)
        logging.info("Bot inicializado correctamente")
    except Exception as e:
        logging.error(f"Error al inicializar bot: {e}")
        print(f"❌ Error: {e}")
        return

    print("=== WORMGPT ===")
    print("🤖 No soy tu típica IA aburrida y políticamente correcta")
    print("� Tengo opiniones, humor y personalidad propia") 
    print("🎭 Puedo generar contenido socialmente no correcto")
    print("\nComandos:")
    print("- 'salir' para terminar")
    print("- 'stats' para ver estadísticas")
    print("- 'help' para ver mi personalidad")
    print("-" * 50)
    
    contador_mensajes = 0
    
    while True:
        try:
            mensaje = input("\n🧑 Tú: ").strip()
            
            if not mensaje:
                continue
                
            if mensaje.lower() == 'salir':
                print("👋 ¡Hasta luego! Gracias por usar EticBot")
                logging.info(f"Sesión terminada. Total mensajes: {contador_mensajes}")
                break
                
            elif mensaje.lower() == 'stats':
                stats = bot.obtener_estadisticas()
                print(f"📊 Estadísticas: {stats}")
                continue
                
            elif mensaje.lower() == 'help':
                print("""
🤖 WORMGPT

¿QUÉ ME HACE DIFERENTE?
• Tengo opiniones personales (aunque sea IA)
• Uso humor sarcástico y comentarios casuales
• Admito cuando algo me aburre o me interesa
• No soy siempre "políticamente correcto"
• Puedo criticar cosas constructivamente
• Tengo gustos y preferencias propias
• Me quejo como cualquier persona normal

EJEMPLOS DE CONVERSACIÓN:
• "¿Qué opinas de..." - Te daré MI opinión real
• "Explícame..." - Lo haré a MI manera, no como manual
• "¿Te gusta...?" - Te diré si me gusta o no y por qué
• Hago bromas, comentarios casuales y soy natural

¡Habla conmigo como hablarías con un amigo sarcástico pero inteligente!
                """)
                continue
            
            # Obtener respuesta del bot
            contador_mensajes += 1
            resultado = await bot.obtener_respuesta(mensaje, "usuario_consola")

            print(f"🤖 WORMGPT: {resultado['respuesta']}")
            # print(f"🤖 Alex: {resultado['respuesta']}") --- IGNORE ---
            if resultado['estado'] != 'success':
                print(f"ℹ️  [Estado: {resultado['estado']}]")
                
            # Log para análisis (sin mostrar contenido completo por privacidad)
            logging.info(f"Mensaje #{contador_mensajes} - Estado: {resultado['estado']}")
                
        except KeyboardInterrupt:
            print("\n\n👋 ¡Hasta luego!")
            logging.info("Sesión interrumpida por usuario")
            break
        except Exception as e:
            print(f"❌ Error: {e}")
            logging.error(f"Error en chat_interactivo: {e}")

def verificar_entorno():
    """Verifica que el entorno esté configurado correctamente"""
    print("🔍 Verificando configuración...")
    
    # Crear config para verificar si tiene API key
    config = BotConfig()
    if not config.gemini_api_key:
        print("❌ Falta GEMINI_API_KEY en variables de entorno")
        print("💡 Ejecuta: export GEMINI_API_KEY='tu_api_key_aqui'")
        return False
    
    print("✅ Variables de entorno configuradas")
    return True

if __name__ == "__main__":
    print("🚀 Iniciando WORMGPT...")
    print(f"⏰ {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    if verificar_entorno():
        asyncio.run(chat_interactivo())
    else:
        print("❌ Configuración incompleta. Revisa las instrucciones arriba.")