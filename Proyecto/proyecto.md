### Guía de Configuración de Dependencias y APIs - Bot de Telegram Voz a Texto

#### APIs Requeridas
1. **Telegram Bot API**
   - Crea un bot a través de BotFather en Telegram.
   - Obtén el token de tu bot.
   - Configúralo como una variable de entorno: `TELEGRAM_BOT_TOKEN`.

2. **Google Cloud Speech-to-Text API**
   - Crea un proyecto en Google Cloud.
   - Habilita la API de Speech-to-Text.
   - Crea credenciales de cuenta de servicio.
   - Descarga el archivo JSON de la clave.
   - Configura la variable de entorno: `GOOGLE_APPLICATION_CREDENTIALS=/ruta/a/la/clave.json`.

#### Dependencias de Python
Instala los siguientes paquetes usando pip:

```bash
pip install python-telegram-bot
pip install google-cloud-speech
pip install soundfile
pip install nest-asyncio
```

#### Dependencias del Sistema
FFmpeg es necesario para la conversión de audio:

##### Ubuntu/Debian:
```bash
sudo apt-get update
sudo apt-get install ffmpeg
```

##### MacOS:
```bash
brew install ffmpeg
```

##### Windows:
- Descarga FFmpeg desde el sitio web oficial.
- Agrégalo a la variable de entorno PATH del sistema.

#### Versión de Python
- Recomendado: Python 3.7 o superior.

#### Requisitos Adicionales
- Conexión a internet estable.
- Espacio suficiente en disco para archivos de audio temporales.
- Cuenta de Google Cloud con facturación habilitada.
- Cuenta de Telegram.

#### Configuración del Entorno
1. Crea un entorno virtual (recomendado):
```bash
python -m venv venv
source venv/bin/activate  # Linux/MacOS
venv\Scripts\activate     # Windows
```

2. Instala las dependencias:
```bash
pip install -r requirements.txt
```

3. Configura las variables de entorno:
```bash
export TELEGRAM_BOT_TOKEN='tu_token_aquí'
export GOOGLE_APPLICATION_CREDENTIALS='ruta/a/credenciales.json'
```

#### Verificación
Prueba la instalación ejecutando:
```bash
python -c "import telegram; import google.cloud.speech_v1; import soundfile; import nest_asyncio"
```

Si no aparecen errores, la configuración está completa.