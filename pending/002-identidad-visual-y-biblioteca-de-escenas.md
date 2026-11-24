# 002 — Identidad visual y biblioteca de escenas en Remotion (HU-3)

## Objetivo
Darle al canal una identidad visual propia, **inspirada (no copiada)** en la referencia 4 (Curiosfer): papel cálido, tarjetas con profundidad, Profe Neto en pixel art y subtítulos palabra por palabra arriba. Además, construir la biblioteca de escenas en Remotion. Ver HU-3 en `docs/definiciones/canal-idiomas-es-en.md`.

## Criterios de aceptación (TDD)
- **Primero, el mockup:** se presentan 3–4 fotogramas (paleta, tipografía, Profe Neto y subtítulos) y el PO los aprueba antes de implementar el resto. En el mockup se calibra el intervalo de ritmo (cada cuánto cambia algo en pantalla).
- Profe Neto está dibujado con código (sprite o matriz), es idéntico entre renders y tiene al menos 4 poses: saludo, señalar, aprobar ✅ y reprobar ❌. Se verifica con un test que compara snapshots del sprite.
- Componente de subtítulos: arriba, palabra por palabra (la actual resaltada y las siguientes atenuadas), con resaltado de la palabra clave, tomando los tiempos de un JSON de entrada.
- Al menos 6 tipos de escena: frase incorrecta → corregida, burbujas de chat, tarjeta de pronunciación, comparación ES vs EN, mini-quiz y cierre con CTA "Comenta GUIA". Cada tipo tiene un esquema de props tipado.
- Un video de demo de unos 20 s con datos de ejemplo se renderiza a MP4 de 1080×1920 sin errores.
- El `Jenkinsfile` gana `buildAndTest` (lint, tests y SonarQube) y el pipeline pasa en verde.
