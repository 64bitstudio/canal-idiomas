# Instalación y uso

> Se completa conforme existan piezas ejecutables (tickets 003 en adelante).

## Requisitos conocidos
- macOS con Apple Silicon (render de voz con aceleración MPS).
- Node.js 24 (Remotion).
- Python 3.11 gestionado con `uv` (Chatterbox requiere `setuptools<81` por la dependencia `perth`).

## Prueba técnica de voz (spike)
`spikes/chatterbox/spike.py` — genera muestras bilingües con Chatterbox Multilingual:

```bash
cd spikes/chatterbox
uv venv --python 3.11 .venv
uv pip install --python .venv/bin/python chatterbox-tts "setuptools<81"
PYTORCH_ENABLE_MPS_FALLBACK=1 .venv/bin/python spike.py <carpeta-salida>
```
