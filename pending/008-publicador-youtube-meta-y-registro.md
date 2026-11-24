# 008 — Publicador automático (YouTube, Instagram, Facebook) y registro (HU-7)

## Objetivo
Publicar automáticamente los videos aprobados en el horario de cada idioma (ES 19:00 CDMX, EN 18:00 hora del Este de EE. UU.) y dejar TikTok listo para subida manual hasta que se apruebe su auditoría. Ver HU-7 en `docs/definiciones/canal-idiomas-es-en.md`.

## Criterios de aceptación (TDD)
- YouTube: sube con `publishAt` en el horario del idioma. Se confirma en la práctica el comportamiento con un proyecto sin verificar (R6).
- Facebook Reels: se publica con `scheduled_publish_time`, con video de 90 s como máximo.
- Instagram Reels: se publica por cron local (`launchd`) a la hora indicada.
- TikTok: el sistema deja el MP4 y el texto en una carpeta "para subir" y avisa. No publica por API mientras no haya auditoría.
- Un fallo en una plataforma no bloquea a las demás, queda registrado y se reintenta o se avisa.
- El registro guarda, por video y plataforma, el ID o enlace, la fecha y el estado.
- Hay tests con las APIs simuladas (mocks) que cubren éxito, fallo parcial y reintento, en verde en CI.
