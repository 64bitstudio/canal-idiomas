# 003 — Servicio de voz (Chatterbox partido por idioma) y sincronía (Whisper)

## Objetivo
Convertir los segmentos de narración etiquetados por idioma en un audio único con la voz por defecto de Profe Neto, y obtener el tiempo de cada palabra para subtítulos y animaciones. Decisión aprobada por el PO tras la prueba técnica (`spikes/chatterbox`). Ver Diseño técnico y R4 en `docs/definiciones/canal-idiomas-es-en.md`.

## Criterios de aceptación (TDD)
- Dada una lista de segmentos `{lang, text}`, se genera un WAV único: cada segmento se sintetiza con su `language_id`, con `cfg_weight` acordado y pausas configurables entre segmentos.
- Un segmento de menos de 3 palabras se rechaza con un error explícito, sin arreglarlo en silencio (Chatterbox falla con segmentos de una sola palabra).
- Whisper local (faster-whisper; tamaño de modelo justificado por la medición) devuelve un JSON con palabras y tiempos `[{word, start, end}]`, alineado contra el texto conocido del guion.
- El desfase medido entre audio y tiempos en una muestra de prueba se reporta y queda bajo el umbral que acuerde el PO (propuesta: 150 ms).
- Se mide y documenta el tiempo de voz y alineación de un guion de unos 75 s.
- La marca de agua Perth sigue activa (no se desactiva).
- Hay tests unitarios del partido de segmentos y del formato de salida, en verde en CI.
