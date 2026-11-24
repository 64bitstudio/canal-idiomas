# 005 — Orquestador de render en lote con Remotion (HU-5)

## Objetivo
Encadenar validador → voz → sincronía → Remotion para convertir un lote de guiones en MP4 listos para revisar, de noche y sin intervención. Ver HU-5 en `docs/definiciones/canal-idiomas-es-en.md`.

## Criterios de aceptación (TDD)
- Un comando procesa un lote y produce, por guion, un MP4 de 1080×1920 con escenas, subtítulos sincronizados y música libre de derechos (licencia de la música guardada junto al proyecto).
- Si falla un guion (voz, alineación o render), el fallo queda registrado con su motivo y el resto del lote continúa.
- Queda programado con `launchd` para la noche. El lote de 14 videos termina antes de la mañana siguiente (se mide en una corrida real).
- La duración del MP4 final está entre 65 y 88 s (verificado con ffprobe en un test).
- Hay una regla de limpieza de audios y renders intermedios para cuidar el disco (R8).
