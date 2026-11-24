# 006 — Página local de revisión de videos (HU-6)

## Objetivo
Que Marco revise y apruebe o rechace los videos del día en menos de 5 minutos, viendo también el texto que se publicará en cada plataforma. Ver HU-6 en `docs/definiciones/canal-idiomas-es-en.md`.

## Criterios de aceptación (TDD)
- La página local (solo `127.0.0.1`) lista los videos pendientes, los reproduce y muestra el texto por plataforma.
- Aprobar mueve el video al estado "aprobado". Rechazar exige un motivo y evita que se publique.
- Hay tests de las transiciones de estado (pendiente → aprobado/rechazado) en verde.
- Accesible desde teclado y con contraste suficiente. Revisión visual en vivo antes de cerrar.
- Revisar 2 videos toma menos de 5 minutos (lo valida el PO).
