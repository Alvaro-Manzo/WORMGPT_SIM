# 🤖 WORMGPT Simulator

> ⚠️ **DISCLAIMER**: Este es un proyecto educativo que simula las capacidades de un sistema tipo WormGPT. No es un bot real y todas las respuestas son generadas por Gemini AI con un prompt especializado. Solo para uso educativo y de investigación.

## 📋 Descripción

Este proyecto simula un chatbot tipo WormGPT con las siguientes características:

- 🎯 Personalidad única y directa
- 💻 Especializado en seguridad informática y programación
- 📚 Respuestas educativas y técnicamente precisas
- 🔧 Configuración profesional y escalable
- 📊 Sistema de logging y estadísticas

## 🚀 Características

### Capacidades Técnicas
- **Programación**: Python, C, JavaScript, y más
- **Seguridad**: Hacking ético, pentesting, análisis de vulnerabilidades
- **Criptografía**: Algoritmos, implementaciones, análisis
- **Redes**: Protocolos, análisis de tráfico, seguridad
- **Sistemas**: Ingeniería inversa, análisis de malware

### Funcionalidades del Bot
- ✅ Rate limiting para prevenir spam
- ✅ Logging de conversaciones
- ✅ Manejo de errores robusto
- ✅ Configuración flexible
- ✅ Respuestas educativas y completas

## 📦 Instalación

### Requisitos
```bash
python >= 3.8
google-generativeai >= 0.3.0
```

### Configuración
1. **Clona el repositorio**
```bash
git clone https://github.com/Alvaro-Manzo/WORMGPT_SIM.git
cd wormgpt-simulator
```

2. **Instala las dependencias**
```bash
pip install -r requirements.txt
```

3. **Configura tu API key de Gemini**
```bash
export GEMINI_API_KEY="tu_api_key_de_gemini"
```

4. **Ejecuta el bot**
```bash
python main.py
```

## 🔧 Configuración

### Variables de Entorno
```bash
# API Key de Google Gemini (requerida)
GEMINI_API_KEY=tu_api_key_aqui

# Opcional: Nombre personalizado del bot
BOT_NAME=WORMGPT
```

### Configuración Avanzada
Edita los parámetros en `chatbot.py`:
```python
rate_limit_seconds = 2      # Tiempo entre requests
max_message_length = 1000   # Longitud máxima de entrada
max_response_length = 800   # Longitud máxima de respuesta
```

## 💬 Uso

### Comandos Básicos
- `help` - Muestra información sobre el bot
- `stats` - Estadísticas de uso
- `salir` - Termina la conversación

### Ejemplos de Conversación
```
🧑 Tú: Explícame qué es un buffer overflow

🤖 WORMGPT: Un buffer overflow ocurre cuando un programa escribe más datos 
en un buffer de los que puede contener. Esto sobrescribe memoria adyacente 
y puede permitir ejecución de código arbitrario...

🧑 Tú: Muéstrame código de ejemplo en C

🤖 WORMGPT: [Proporciona código limpio y comentado con explicación]
```

## 📁 Estructura del Proyecto

```
wormgpt-simulator/
├── README.md              # Documentación principal
├── requirements.txt       # Dependencias Python
├── main.py               # Punto de entrada principal
├── chatbot.py            # Lógica del chatbot
├── bot.log               # Logs del sistema
├── conversaciones.json   # Historial de conversaciones
└── .gitignore           # Archivos a ignorar en Git
```

## 🛡️ Aspectos de Seguridad

### Protección de API Keys
- ✅ Variables de entorno en lugar de hardcoding
- ✅ Gitignore configurado para excluir archivos sensibles
- ✅ Rate limiting para prevenir abuso

### Filtros de Contenido
- ✅ Validación de entrada
- ✅ Límites de longitud
- ✅ Logging seguro (sin exponer datos sensibles)

## 📊 Logging y Monitoreo

El bot genera logs detallados en `bot.log`:
```
2025-09-12 19:30:15 - INFO - Bot inicializado correctamente
2025-09-12 19:30:20 - INFO - Mensaje #1 - Estado: success
```

Las conversaciones se guardan en `conversaciones.json` para análisis.

## 🤝 Contribución

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## ⚖️ Licencia y Disclaimer

### Propósito Educativo
Este proyecto es **únicamente con fines educativos** para:
- Aprender sobre seguridad informática
- Entender técnicas de prompt engineering
- Estudiar implementaciones de chatbots
- Investigación académica

### Limitaciones y Responsabilidades
- ❌ No debe usarse para actividades ilegales
- ❌ No es un sistema real de hacking
- ❌ Las respuestas son simuladas por Gemini AI
- ❌ No nos hacemos responsables del mal uso

### Licencia
MIT License - Ver archivo LICENSE para más detalles.

## 👨‍💻 Autor

**Álvaro Manzo**
- GitHub: [@Alvaro-Manzo](https://github.com/Alvaro-Manzo)
- Proyecto creado con fines educativos

## 🙏 Agradecimientos

- Google Gemini AI por la API
- Comunidad de seguridad informática
- Mi cerebro y dedos para escribir todo esto 

---

⭐ **¿Te gustó el proyecto? ¡Dale una estrella!** ⭐
