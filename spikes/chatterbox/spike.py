"""Prueba técnica: voz bilingüe con Chatterbox Multilingual (una sola voz, segmentos por idioma)."""
import sys
import time

import torch
import torchaudio as ta
from chatterbox.mtl_tts import ChatterboxMultilingualTTS

OUT = sys.argv[1]
REF = sys.argv[2] if len(sys.argv) > 2 else None  # clip de referencia opcional (voz a clonar)

device = "mps" if torch.backends.mps.is_available() else "cpu"
t0 = time.time()
model = ChatterboxMultilingualTTS.from_pretrained(device=device)
print(f"modelo cargado en {time.time() - t0:.0f}s ({device})", flush=True)

ES = [
    ("es", "Deja de decir:"), ("en", "I am agree."),
    ("es", "Eso está mal. Los nativos dicen:"), ("en", "I agree."),
    ("es", "O si quieres sonar más natural:"), ("en", "I couldn't agree more."),
]
EN = [
    ("en", "Stop saying:"), ("es", "Estoy embarazada."),
    ("en", "when you feel embarrassed. That means you are pregnant! Instead, say:"),
    ("es", "Me da vergüenza."), ("en", "or you can also say"), ("es", "Qué pena."),
    ("en", "Trust me, your Mexican friends will thank you."),
]


def render(segments, name, cfg_weight):
    pause = torch.zeros(1, int(model.sr * 0.25))
    parts = []
    t = time.time()
    for lang, text in segments:
        wav = model.generate(text, language_id=lang, audio_prompt_path=REF,
                             cfg_weight=cfg_weight, exaggeration=0.6)
        parts += [wav.cpu(), pause]
    ta.save(f"{OUT}/{name}.wav", torch.cat(parts, dim=1), model.sr)
    print(f"ok {name} ({time.time() - t:.0f}s)", flush=True)


def render_single(segments, lang, name):
    text = " ".join(s for _, s in segments)
    t = time.time()
    wav = model.generate(text, language_id=lang, audio_prompt_path=REF, exaggeration=0.6)
    ta.save(f"{OUT}/{name}.wav", wav.cpu(), model.sr)
    print(f"ok {name} ({time.time() - t:.0f}s)", flush=True)


import os
if not os.environ.get("ONLY_EN"):
    render(ES, "7-canalES-chatterbox-segmentado", cfg_weight=0.0)
    render_single(ES, "es", "8-canalES-chatterbox-sin-segmentar")
render(EN, "9-canalEN-chatterbox-segmentado", cfg_weight=0.0)
render_single(EN, "en", "10-canalEN-chatterbox-sin-segmentar")
