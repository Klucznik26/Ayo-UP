# Ayo Up

Minimalist image upscaler based on **waifu2x-ncnn-vulkan**.

Author: **Klucznik**

---

## What is Ayo Up?

**Ayo Up** is a small desktop application for image upscaling,
built around the **waifu2x-ncnn-vulkan** engine.

The project was created to provide:
- a simple tool,
- a clear and readable interface,
- one well-defined purpose.

Ayo Up does one thing — and does not try to do more.

---

## Features (v1.0)

- image upscaling **x2** and **x4**
- drag & drop support
- image preview
- output directory selection
- automatic output file naming (`_AUPx2`, `_AUPx4`)
- themes: light / dark / system
- multilingual user interface:
  - PL / EN / UA
  - LV / LT / EE

---

## What Ayo Up is NOT

- not a graphic editor
- no batch upscaling (yet)
- does not install the waifu2x engine for the user
- not an “all-in-one AI tool”

---

## Requirements

- Linux
- Python 3.9 or newer
- waifu2x-ncnn-vulkan (installed or provided manually)
- Vulkan-capable GPU (recommended)

---

## Running the application

```bash
python AyoUp.py
