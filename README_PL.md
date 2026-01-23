# Ayo Up

Minimalistyczna aplikacja do powiększania obrazów (upscaling),
oparta o **waifu2x-ncnn-vulkan**.

Autor: **Klucznik**

---

## Czym jest Ayo Up?

**Ayo Up** to niewielka aplikacja desktopowa służąca do powiększania obrazów,
zbudowana wokół silnika **waifu2x-ncnn-vulkan**.

Projekt powstał z myślą o:
- prostocie,
- czytelnym i spokojnym interfejsie,
- jednej, jasno określonej funkcji.

Ayo Up robi jedną rzecz — i nie próbuje robić więcej.

---

## Funkcje (v1.0)

- powiększanie obrazów **x2** oraz **x4**
- obsługa przeciągnij i upuść (drag & drop)
- podgląd obrazu
- wybór katalogu zapisu
- automatyczne nazewnictwo plików (`_AUPx2`, `_AUPx4`)
- motywy: jasny / ciemny / systemowy
- wielojęzyczny interfejs użytkownika:
  - PL / EN / UA
  - LV / LT / EE

---

## Czego Ayo Up nie robi

- nie jest edytorem graficznym
- nie obsługuje upscalingu wsadowego (batch) — jeszcze
- nie instaluje silnika waifu2x za użytkownika
- nie jest „kombajnem AI”

---

## Wymagania

- Linux
- Python 3.9 lub nowszy
- waifu2x-ncnn-vulkan (zainstalowany lub dostarczony ręcznie)
- karta graficzna z obsługą Vulkan (zalecane)

---

## Uruchamianie aplikacji

```bash
python AyoUp.py
