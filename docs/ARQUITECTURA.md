# Arquitectura

> Fuente de diseño: `docs/definiciones/canal-idiomas-es-en.md` (sección Diseño técnico y diagramas). Este archivo explica el sistema tal como quede implementado; se actualiza al cerrar cada ticket.

## Flujo (planeado)
1. **Semanal:** Claude genera 14 guiones JSON (segmentos por idioma + escenas) → validador.
2. **Noche:** Chatterbox sintetiza cada segmento → Whisper obtiene tiempos por palabra → Remotion renderiza el MP4 1080×1920.
3. **Diario:** Marco aprueba/rechaza en la página local de revisión → publicador sube a YouTube/Instagram/Facebook; TikTok queda listo para subida manual.

## Estado actual
Solo existe el spike de voz (`spikes/chatterbox`). MoneyPrinterTurbo (carpeta local, no versionada) se usó para pruebas iniciales y se retira en el ticket 010.
