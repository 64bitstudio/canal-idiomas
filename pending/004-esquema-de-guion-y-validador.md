# 004 — Esquema JSON de guion con escenas, validador y primer lote (HU-4)

## Objetivo
Definir el contrato del guion semanal (segmentos por idioma + escenas + texto por plataforma) y un validador estricto, y producir el primer lote real de 7+7 guiones. Ver HU-4 en `docs/definiciones/canal-idiomas-es-en.md`.

## Criterios de aceptación (TDD)
- Hay un esquema JSON versionado con: tema, formato, segmentos `{lang: es|en, text}`, escenas `{tipo, datos, segmentos ligados}`, texto por plataforma (YT, IG, FB, TikTok) y duración estimada.
- El validador rechaza, con un mensaje claro por error: duración fuera de 65–88 s, segmentos de menos de 3 palabras, tipos de escena inexistentes en la biblioteca, datos de escena que no cumplen el esquema de su tipo, y dos formatos iguales seguidos en el calendario.
- Hay tests con casos válidos e inválidos, uno por regla, en verde en CI.
- El primer lote (7 ES + 7 EN) pasa el validador y cumple la lista de chequeo de la guía (ticket 001).
