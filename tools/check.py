#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cek hasil build. GAGAL (exit 1) kalau kata terlarang masih ada di isi file,
nama file, atau URL; juga cek link/asset lokal yang rusak dan alt foto kosong.
Jalankan: python3 tools/check.py [folder]   (default: public_html)"""
import os, re, sys, unicodedata
from urllib.parse import unquote

ROOT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "public_html")
TEXT = (".html", ".css", ".js", ".xml", ".txt", ".svg", ".json", ".webmanifest", ".htaccess")
# Latin: tangkap islam/islami/islamic/keislaman dst. Arab: إسلام / اسلام / أسلام + turunannya.
LATIN = re.compile(r"[iıİ]\W{0,2}s\W{0,2}l\W{0,2}a\W{0,2}m", re.I)
ARAB = re.compile(r"[إاأٱآ]سلام")
STRIP = re.compile(r"[ً-ٰٟـ​-‏­]")  # harakat, tatweel, zero-width

def norm(s):
    s = unquote(s)
    s = unicodedata.normalize("NFKC", s)
    s = re.sub(r"&#x?[0-9a-f]+;|&[a-z]+;", lambda m: __import__("html").unescape(m.group(0)), s, flags=re.I)
    return STRIP.sub("", s)

def hits(s):
    s = norm(s)
    return [m for rx in (LATIN, ARAB) for m in rx.finditer(s)], s

errors, warns, n = [], [], 0
for dp, _, fs in os.walk(ROOT):
    for fn in fs:
        p = os.path.join(dp, fn); rel = os.path.relpath(p, ROOT); n += 1
        if hits(rel)[0]:
            errors.append("NAMA FILE terlarang: %s" % rel)
        if not fn.lower().endswith(TEXT):
            continue
        raw = open(p, encoding="utf-8", errors="replace").read()
        hs, s = hits(raw)
        for m in hs:
            line = s.count("\n", 0, m.start()) + 1
            errors.append("KATA TERLARANG di %s baris %d: ...%s..." % (rel, line, s[max(0, m.start()-30):m.end()+30].replace("\n", " ")))
        if fn.endswith(".html"):
            for tag in re.findall(r"<img\b[^>]*>", raw):
                if not re.search(r'\balt="[^"]{5,}"', tag):
                    errors.append("ALT kosong di %s: %s" % (rel, tag[:90]))
            ids = set(re.findall(r'\bid="([^"]+)"', raw))
            for href in re.findall(r'(?:href|src)="([^"]+)"', raw):
                if href.startswith("#"):
                    if href[1:] and href[1:] not in ids:
                        errors.append("ANCHOR rusak di %s: %s" % (rel, href))
                elif not re.match(r"^(https?:|mailto:|tel:|data:)", href):
                    h = href.split("#")[0].split("?")[0]
                    t = os.path.normpath(os.path.join(ROOT, h.lstrip("/")) if h.startswith("/") else os.path.join(dp, h))
                    if os.path.isdir(t):
                        t = os.path.join(t, "index.html")
                    if not os.path.exists(t):
                        errors.append("LINK rusak di %s: %s" % (rel, href))
            if fn != "404.html" and (not re.search(r'hreflang="en"', raw) or not re.search(r'hreflang="id"', raw)):
                errors.append("hreflang tidak lengkap di %s" % rel)

print("Diperiksa: %d file di %s" % (n, ROOT))
for x in errors:
    print("  [GAGAL]", x)
if errors:
    print("HASIL: GAGAL (%d masalah)" % len(errors)); sys.exit(1)
print("HASIL: LULUS - tidak ada kata terlarang, link rusak, atau alt kosong.")
