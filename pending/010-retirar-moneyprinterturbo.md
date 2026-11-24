# 010 — Retirar MoneyPrinterTurbo

## Objetivo
Quitar el motor anterior cuando el render con Remotion (ticket 005) esté funcionando, para liberar unos 2.7 GB y evitar dependencias muertas. Ver la decisión de motor de render en `docs/definiciones/canal-idiomas-es-en.md`.

## Criterios de aceptación (TDD)
- Solo se ejecuta después de que el ticket 005 esté en `done/`.
- Se detienen y eliminan los contenedores (`docker compose down`), se borra la imagen `ghcr.io/harry0703/moneyprinterturbo` y la carpeta `MoneyPrinterTurbo/`, con VoBo del PO antes de borrar.
- Antes de borrar se rescata lo que sirva (por ejemplo, las claves de Pixabay y Gemini se revocan o regeneran en sus portales, porque quedaron escritas en el chat).
- `docs/ARQUITECTURA.md` deja de mencionar MPT como pieza activa.
- Se mide y reporta el espacio liberado.
