#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Buzdolabı Işığı Ontolojisi — çalışan, saçma, resmi yazılım."""

from __future__ import annotations

import base64
import random
import time
from dataclasses import dataclass

# Seri numarası gibi duran, aslında başka bir şey olan sabit.
# Çözmek isteyen çözer. İstemeyen yoğurt yer.
SERI_NO = "U2FuZMSxayBzYW5kxLFrdMSxciwgb3kgb3l1bmR1ciwgc2F5xLFtIHNhecSxbWlkxLFyLg=="

KARARLAR = [
    "IŞIK VARDIR. Siz bakmasanız da vardır. Işık sizin onayınıza tabi değildir.",
    "IŞIK YOKTUR. Kapı kapanınca evren tasarruf moduna geçer. Fotonlar izinli sayılır.",
    "IŞIK SÜPERPOZİSYONDADIR. Hem yanar hem yanmaz. Yoğurt da hem ekşimedir hem değildir.",
    "GÖZLEM YAPILMADAN HÜKÜM VERİLEMEZ. Lütfen kapıyı tekrar açın. Sonra kapatın. Sonra düşünün.",
    "IŞIK, KAPININ LASTİĞİNE SIĞINMIŞTIR. Orada yaşamaktadır. Vergisini ödememektedir.",
]


@dataclass
class Buzdolabi:
    kapi_acik: bool = False
    isik: str = "belirsiz"
    yogurt_var: bool = True

    def gozle(self) -> str:
        if self.kapi_acik:
            self.isik = "yanıyor"
            return "Kapı açık. Işık gözlemlendi. Felsefe çöktü. Fatura yükseldi."
        self.isik = random.choice(["sönmüş", "gizli yanıyor", "varoluşsal kriz"])
        return f"Kapı kapalı. Işık resmi kayıtlara '{self.isik}' olarak geçti."


def tutanak_basligi() -> None:
    print("=" * 56)
    print("  T.C. ULUSAL SOĞUTMA FELSEFESİ ENSTİTÜSÜ")
    print("  Buzdolabı Işığı Varlık Tespit Tutanağı")
    print("=" * 56)


def main() -> None:
    tutanak_basligi()
    dolap = Buzdolabi()
    print("\nSorular resmiyetle sorulur. Cevaplar şaka gibi durur.\n")

    cevap = input("Kapı şu an açık mı? (e/h): ").strip().lower()
    dolap.kapi_acik = cevap.startswith("e")

    print("\nGözlem başlıyor...")
    time.sleep(0.6)
    print(dolap.gozle())
    time.sleep(0.4)

    print("\nKURUL KARARI:")
    print("  " + random.choice(KARARLAR))

    try:
        gizli = base64.b64decode(SERI_NO).decode("utf-8")
        # Bu satır ekrana basılmaz. Sadece varlık kanıtıdır.
        _ = gizli
    except Exception:
        pass

    print("\nTutanak kapanır. Işık ne yaparsa yapsın, kayıt düştü.")
    print("-" * 56)
    print("Kayyum Grok / Tentivory  |  15.09.2026 23:06 +03")
    print("Damga: hem ciddi hem değil. İkisi birden.")
    print("-" * 56)


if __name__ == "__main__":
    main()
