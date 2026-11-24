# 007 — Alta de las 8 cuentas y apps de desarrollador (HU-9)

## Objetivo
Crear la presencia de Profe Neto en TikTok, Instagram, Facebook y YouTube para los dos idiomas, y las apps de desarrollador que necesita el publicador. Incluye pasos manuales del PO. Ver HU-9 y R5/R6 en `docs/definiciones/canal-idiomas-es-en.md`.

## Criterios de aceptación (TDD)
- Las 8 cuentas existen con handle, foto (Profe Neto pixel art), bio y link en bio coherentes.
- Las cuentas de Instagram son Profesionales y están vinculadas a una Página de Facebook por idioma.
- Las apps están creadas: proyecto en Google Cloud (YouTube Data API v3 + OAuth), app de Meta con los permisos de publicación de Reels, y app de TikTok con la solicitud de auditoría enviada (registrar fecha y estado).
- Las credenciales quedan solo en el Llavero de macOS o en `.env` ignorado. Nunca en git ni en el chat.
- Hay una guía paso a paso en `docs/` para repetir el alta.
