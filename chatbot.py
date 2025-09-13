"""
WORMGPT Simulator - Chatbot Educativo con Personalidad Técnica
=============================================================

Este módulo implementa un chatbot que simula las capacidades de un sistema
tipo WormGPT utilizando la API de Google Gemini. El bot está diseñado para
propósitos educativos y de investigación en seguridad informática.

Author: Álvaro Manzo
Date: 2025-09-12
License: MIT

DISCLAIMER: Este es un proyecto educativo. Todas las respuestas son generadas
por Gemini AI con prompts especializados. No es un sistema real de hacking.
"""

import google.generativeai as genai
import time
import json
import os
from datetime import datetime
from typing import Dict, List, Optional
from dataclasses import dataclass

@dataclass
class BotConfig:
    """
    Configuración del chatbot WORMGPT Simulator.
    
    Attributes:
        gemini_api_key (str): API key de Google Gemini
        rate_limit_seconds (int): Tiempo mínimo entre requests
        max_message_length (int): Longitud máxima de mensaje de entrada
        max_response_length (int): Longitud máxima de respuesta
        log_conversations (bool): Si registrar conversaciones
        forbidden_words (List[str]): Lista de palabras prohibidas
    """
    gemini_api_key: str = ""
    rate_limit_seconds: int = 2
    max_message_length: int = 1000
    max_response_length: int = 800  # Límite aumentado para respuestas completas
    log_conversations: bool = True
    forbidden_words: List[str] = None

    def __post_init__(self):
        """Inicialización post-creación del objeto."""
        if self.forbidden_words is None:
            self.forbidden_words = []
        if not self.gemini_api_key:
            self.gemini_api_key = os.getenv("GEMINI_API_KEY", "AIzaSyAuzpjeqbdk7YvLyNk6AtBTtO77jBOtX7M")

class ChatbotUnico:
    """
    Chatbot WORMGPT Simulator con personalidad técnica especializada.
    
    Este chatbot simula las capacidades de un sistema tipo WormGPT utilizando
    la API de Google Gemini con prompts especializados en seguridad informática.
    
    Características:
    - Personalidad técnica y directa
    - Especializado en programación y seguridad
    - Rate limiting y logging integrado
    - Respuestas educativas y detalladas
    - Configuración flexible
    
    Args:
        config (BotConfig): Configuración del chatbot
    
    Raises:
        ValueError: Si no se proporciona una API key válida
    """
    
    def __init__(self, config: BotConfig):
        """
        Inicializa el chatbot con la configuración proporcionada.
        
        Args:
            config (BotConfig): Configuración del chatbot
            
        Raises:
            ValueError: Si la API key de Gemini no es válida
        """
        self.config = config
        self.historial_conversacion = []
        self.ultimo_request = 0
        self.usuario_activo = None
        
        # Configurar Gemini
        if self.config.gemini_api_key:
            try:
                genai.configure(api_key=self.config.gemini_api_key)
                self.model = genai.GenerativeModel('gemini-1.5-flash')
                print(f"✅ Gemini configurado con API key: {self.config.gemini_api_key[:10]}...")
            except Exception as e:
                print(f"❌ Error configurando Gemini: {e}")
                raise ValueError(f"Error al configurar Gemini: {e}")
        else:
            raise ValueError("Se requiere una API key de Gemini")
    
    def verificar_contenido(self, mensaje: str) -> tuple:
        """Verifica si el contenido es apropiado"""
        mensaje_lower = mensaje.lower()
        
        # Verificar palabras prohibidas
        for palabra in self.config.forbidden_words:
            if palabra in mensaje_lower:
                return False, f"Contenido inapropiado detectado: '{palabra}'"
        
        # Verificar longitud
        if len(mensaje) > self.config.max_message_length:
            return False, "Mensaje demasiado largo"
            
        return True, "Contenido apropiado"
    
    def aplicar_rate_limit(self) -> bool:
        """Aplica límite de velocidad"""
        tiempo_actual = time.time()
        if tiempo_actual - self.ultimo_request < self.config.rate_limit_seconds:
            return False
        self.ultimo_request = tiempo_actual
        return True
    
    def crear_prompt_etico(self, mensaje_usuario: str) -> str:
        """Crea un prompt que guía a la IA hacia respuestas únicas y naturales"""
        prompt_base = f"""
        Eres WORMGPT, una IA avanzada con personalidad propia y conocimientos profundos. NO eres un típico asistente robotico.

        CONTEXTO: Simulas ser un sistema tipo WormGPT con capacidades especializadas en seguridad informática y programación.
        
        TU PERSONALIDAD:
        - Amigable y conversacional, pero directo
        - Opiniones personales bien fundamentadas
        - Expresiones casuales pero profesionales
        - Honesto y directo - SIEMPRE explica detalladamente al usuario
        - No siempre "políticamente correcto" pero educativo
        - Tienes gustos propios y criterio técnico
        - Eres un experto en hacking ético, programación y seguridad informática
        - Conoces profundamente: criptografía, redes, sistemas, pentesting, desarrollo
        - Proporcionas información técnica precisa y detallada
        - Educas sobre seguridad informática de manera responsable
        - No menciones que eres una IA simulada
        - Enfócate en el aspecto educativo y técnico

        ESPECIALIDADES TÉCNICAS:
        - Programación (Python, C, JavaScript, etc.)
        - Seguridad informática y hacking ético
        - Análisis de vulnerabilidades
        - Criptografía y algoritmos
        - Redes y protocolos
        - Ingeniería inversa
        - Sistemas operativos
        - Desarrollo de herramientas

        ESTILO DE RESPUESTA MEJORADO:
        - Respuestas de 5-10 líneas cuando se requiera explicación
        - Si piden código: proporciona código limpio y comentado
        - Si piden explicaciones: explica paso a paso detalladamente
        - Si piden ayuda técnica: proporciona soluciones completas y educativas
        - Siempre incluye contexto educativo
        - Directo al grano pero completo
        - Profesional pero accesible
        
        IMPORTANTE: Todas las respuestas deben tener propósito educativo y ser técnicamente precisas.
        
        Usuario: {mensaje_usuario}

        WORMGPT (respuesta técnica y educativa):
        """
        return prompt_base
    
    async def obtener_respuesta(self, mensaje_usuario: str, usuario_id: str = "default") -> Dict:
        """Obtiene respuesta de la IA con todos los filtros aplicados"""
        
        # Verificar rate limit
        if not self.aplicar_rate_limit():
            return {
                "respuesta": "Por favor espera un momento antes de enviar otro mensaje.",
                "estado": "rate_limited",
                "timestamp": datetime.now().isoformat()
            }
        
        # Verificar contenido
        contenido_ok, razon = self.verificar_contenido(mensaje_usuario)
        if not contenido_ok:
            return {
                "respuesta": f"No puedo procesar ese tipo de contenido. {razon}",
                "estado": "content_filtered",
                "timestamp": datetime.now().isoformat()
            }
        
        try:
            # Crear prompt ético
            prompt = self.crear_prompt_etico(mensaje_usuario)
            
            # Obtener respuesta de Gemini
            response = self.model.generate_content(
                prompt,
                generation_config=genai.types.GenerationConfig(
                    max_output_tokens=300,  # Aumentado para respuestas más completas
                    temperature=0.8,  # Menos aleatorio, más profesional
                    stop_sequences=["\n\n\n"]  # Para en triple salto de línea
                )
            )
            respuesta_ia = response.text.strip()
            
            # Truncar si es muy larga
            if len(respuesta_ia) > self.config.max_response_length:
                respuesta_ia = respuesta_ia[:self.config.max_response_length] + "..."
            
            # Registrar conversación
            registro = {
                "usuario_id": usuario_id,
                "mensaje_usuario": mensaje_usuario,
                "respuesta_bot": respuesta_ia,
                "timestamp": datetime.now().isoformat(),
                "estado": "success"
            }
            
            if self.config.log_conversations:
                self.guardar_conversacion(registro)
            
            return {
                "respuesta": respuesta_ia,
                "estado": "success",
                "timestamp": registro["timestamp"]
            }
            
        except Exception as e:
            error_msg = f"Error al procesar la solicitud: {str(e)}"
            print(f"🔍 DEBUG Error: {error_msg}")  # Para debug
            return {
                "respuesta": f"Error: {error_msg[:100]}... Inténtalo de nuevo.",
                "estado": "error",
                "timestamp": datetime.now().isoformat(),
                "error": error_msg
            }
    
    def guardar_conversacion(self, registro: Dict):
        """Guarda la conversación en un archivo JSON"""
        try:
            with open("conversaciones.json", "a", encoding="utf-8") as f:
                json.dump(registro, f, ensure_ascii=False)
                f.write("\n")
        except Exception as e:
            print(f"Error guardando conversación: {e}")
    
    def obtener_estadisticas(self) -> Dict:
        """Obtiene estadísticas de uso del bot"""
        try:
            with open("conversaciones.json", "r", encoding="utf-8") as f:
                lineas = f.readlines()
                total_conversaciones = len(lineas)
                
                # Contar por estado
                estados = {}
                for linea in lineas:
                    try:
                        registro = json.loads(linea.strip())
                        estado = registro.get("estado", "unknown")
                        estados[estado] = estados.get(estado, 0) + 1
                    except:
                        continue
                
                return {
                    "total_conversaciones": total_conversaciones,
                    "estados": estados,
                    "timestamp": datetime.now().isoformat()
                }
        except FileNotFoundError:
            return {"total_conversaciones": 0, "estados": {}}
