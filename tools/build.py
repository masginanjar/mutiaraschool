#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Bangun situs statis ke folder public_html/. Jalankan: python3 tools/build.py"""
import html, json, os, posixpath, re, shutil, sys
from urllib.parse import quote

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from content import *  # noqa
from pages import P, SLUG, HERO_IMG, XALT

ROOT = os.path.dirname(HERE)
OUT = os.path.join(ROOT, "public_html")
LANGS = ["en", "id"]          # en = default di "/"
PAGES = ["home", "about", "programs", "facilities", "gallery", "admissions", "contact"]
SEC = dict(about="tentang", programs="program", facilities="fasilitas", gallery="galeri", admissions="pendaftaran", contact="kontak")
e = html.escape

WA_ICON = ('<svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2" '
           'stroke-linecap="round" stroke-linejoin="round"><path d="M12 3a9 9 0 0 0-7.8 13.5L3 21l4.6-1.2A9 9 0 1 0 12 3Z"/><path d="M9 8.5c0 3.5 3 6.5 6.5 6.5"/></svg>')
CHECK = ('<svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true"><path fill="none" stroke="currentColor" stroke-width="2.6" '
         'stroke-linecap="round" stroke-linejoin="round" d="m5 12.5 4.5 4.5L19 7.5"/></svg>')


def upath(lang, pg):
    base = T[lang]["path"]
    return base if pg == "home" else base + SLUG[lang][pg] + "/"


def rel(frm, to):
    r = posixpath.relpath(to, frm)
    return "./" if r == "." else r + "/"


def wa(t, extra=""):
    return e("https://wa.me/%s?text=%s" % (WA, quote(t["wa_msg"] + extra)))


ASSET = [""]   # prefix relatif ke akar situs untuk halaman yang sedang dibangun
SIZE = {"hero_l": (1600, 940), "logo": (96, 120)}


def img(key, alt, cls="", h=None, eager=False, sz="(min-width: 900px) 45vw, 100vw"):
    w, hh = SIZE.get(key, (794, 528))
    base = ASSET[0] + IMG[key]
    if key == "logo":
        srcset = ""
    else:
        big, small = (1600, 800) if key == "hero_l" else (794, 480)
        if cls == "hero-bg":
            sz = "100vw"
        srcset = ' srcset="%s %dw, %s %dw" sizes="%s"' % (base.replace(".webp", "-s.webp"), small, base, big, sz)
    return '<img src="%s"%s alt="%s" width="%d" height="%d"%s%s>' % (
        base, srcset, e(alt), w, hh, ' fetchpriority="high"' if eager else ' loading="lazy" decoding="async"', ' class="%s"' % cls if cls else "")


def ticks(items):
    return '<ul class="ticks">%s</ul>' % "".join("<li>%s<span>%s</span></li>" % (CHECK, e(x)) for x in items)


HOME_GAL = ["g1", "x1", "g2", "x4", "g4", "x3", "g5", "x20", "g6", "x9", "g3", "x24"]
ALL_GAL = ["g1", "hero", "g3", "x2", "g5", "g6", "about", "x0", "x4", "x5", "x8", "x9", "sd", "smp", "x13", "paud", "x1", "x3", "x24", "x28",
           "g2", "x18", "x19", "x20", "x21", "x23", "g4", "x25", "x26", "g7"]


def gallery_keys(full):
    return ALL_GAL if full else HOME_GAL


def gal_alt(t, lang, key):
    if key.startswith("g"):
        return t["gal_alt"][int(key[1:]) - 1]
    if key in XALT:
        return XALT[key][lang]
    return {"hero": t["hero_alt"], "paud": t["progs"][0][4], "sd": t["progs"][1][4], "smp": t["progs"][2][4], "about": t["about_alt"]}[key]


def gallery(t, lang, full):
    return '<div class="gal%s">%s</div>' % (" full" if full else "", "".join(
        "<figure>%s</figure>" % img(k, gal_alt(t, lang, k), sz="(min-width: 900px) 25vw, (min-width: 600px) 33vw, 50vw") for k in gallery_keys(full)))


def contact_block(t, W):
    soc = "".join('<li><a href="%s" target="_blank" rel="noopener">%s</a></li>' % (u, n) for n, u in SOCIAL)
    return f'''<div class="two top">
      <address class="card con">
        <h3>{e(t["addr_h"])}</h3><p>{e(t["addr"])}</p>
        <h3>{e(t["hours_h"])}</h3><p>{e(t["hours"])}</p>
        <h3>{e(t["wa_h"])}</h3><p><a href="{W}" target="_blank" rel="noopener"><bdi dir="ltr">{WA_SHOW}</bdi></a></p>
        <h3>{e(t["mail_h"])}</h3><p><a href="mailto:{EMAIL}"><bdi dir="ltr">{EMAIL}</bdi></a></p>
        <h3>{e(t["social_h"])}</h3><ul class="soc">{soc}</ul>
        <a class="btn btn-ghost" href="{MAP_LINK}" target="_blank" rel="noopener">{e(t["map_b"])}</a>
      </address>
      <div class="map"><iframe src="{e(MAP_EMBED)}" title="{e(t["map_title"])}" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe></div>
    </div>'''


def steps_html(items):
    return '<ol class="steps n%d">%s</ol>' % (len(items), "".join(
        '<li><span class="num" aria-hidden="true">%d</span><div><h3>%s</h3><p>%s</p></div></li>' % (i, e(a), e(b)) for i, (a, b) in enumerate(items, 1)))


def home_body(t, lang, L, W):
    stats = "".join('<div><dt>%s</dt><dd>%s</dd></div>' % (e(b), e(a)) for a, b in t["stats"])
    more = lambda pg: '<p class="more"><a class="link" href="%s">%s <span aria-hidden="true" class="arr">→</span></a></p>' % (L(pg), e(t["learn"]))
    progs = ""
    for key, (name, sub, p, pts, alt) in zip(["paud", "sd", "smp"], t["progs"]):
        progs += ('<article class="card prog">%s<div class="card-b"><h3>%s</h3><p class="sub">%s</p><p>%s</p>%s'
                  '<a class="link" href="%s#%s">%s <span aria-hidden="true" class="arr">→</span></a></div></article>'
                  % (img(key, alt, sz="(min-width: 900px) 33vw, 100vw"), e(name), e(sub), e(p), ticks(pts), L("programs"), key, e(t["learn"])))
    best = "".join('<div class="best"><span class="letter" aria-hidden="true">%s</span><h3>%s</h3><p>%s</p></div>' % (a, e(b), e(c)) for a, b, c in t["best"])
    why = "".join('<div class="why"><h3>%s</h3><p>%s</p></div>' % (e(a), e(b)) for a, b in t["why"])
    mission = "".join("<li>%s</li>" % e(m) for m in t["mission"])
    about_p = "".join("<p>%s</p>" % e(p) for p in t["about_p"])
    quote = next(x for x in P[lang]["about"]["blocks"] if x[0] == "quote")
    qhtml = block(quote, t, lang, W, 0)
    return f'''<section class="hero">
  {img("hero_l", t["hero_alt"], cls="hero-bg", eager=True)}
  <div class="wrap hero-in">
    <p class="eyebrow">{e(t["welcome"])}</p>
    <h1>{e(t["school"])}</h1>
    <p class="lead">{e(t["h1"])}</p>
    <div class="btns center">
      <a class="btn btn-wa" href="{W}" target="_blank" rel="noopener">{WA_ICON}<span>{e(t["cta"])}</span></a>
      <a class="btn btn-ghost" href="{L("programs")}">{e(t["hero_b2"])}</a>
    </div>
  </div>
</section>
<section class="notice"><div class="wrap"><p><strong>{e(t["badge"])}</strong> <a href="{L("admissions")}">{e(t["learn"])} <span aria-hidden="true" class="arr">→</span></a></p></div></section>
<section class="sec intro"><div class="wrap"><p class="kick">{e(t["fact_k"])}</p><p class="bigp">{e(t["hero_p"])}</p><dl class="stats">{stats}</dl></div></section>
<section id="tentang" class="sec">
  <div class="wrap two">
    <div class="pic">{img("about", t["about_alt"])}</div>
    <div><p class="kick">{e(t["about_k"])}</p><h2>{e(t["about_h"])}</h2>{about_p}{more("about")}</div>
  </div>
  <div class="wrap vm">
    <div class="card vis"><h3>{e(t["vision_h"])}</h3><p>{e(t["vision"])}</p></div>
    <div class="card mis"><h3>{e(t["mission_h"])}</h3><ol>{mission}</ol></div>
  </div>
</section>
<section id="program" class="sec alt">
  <div class="wrap">
    <div class="head"><p class="kick">{e(t["prog_k"])}</p><h2>{e(t["prog_h"])}</h2><p>{e(t["prog_p"])}</p></div>
    <div class="grid3">{progs}</div>
    <div class="head mt"><p class="kick">{e(t["best_k"])}</p><h2>{e(t["best_h"])}</h2></div>
    <div class="grid4">{best}</div>
  </div>
</section>
{qhtml}
<section id="fasilitas" class="sec">
  <div class="wrap">
    <div class="head"><p class="kick">{e(t["fac_k"])}</p><h2>{e(t["fac_h"])}</h2><p>{e(t["fac_p"])}</p></div>
    <div class="fac">{ticks(t["fac"])}</div>
    <div class="whys">{why}</div>
    {more("facilities")}
  </div>
</section>
<section id="galeri" class="sec alt">
  <div class="wrap">
    <div class="head"><p class="kick">{e(t["gal_k"])}</p><h2>{e(t["gal_h"])}</h2></div>
    {gallery(t, lang, False)}
    <p class="more"><a class="link" href="{L("gallery")}">{e(t["gal_more"])} <span aria-hidden="true" class="arr">→</span></a></p>
  </div>
</section>
<section id="pendaftaran" class="sec reg">
  <div class="wrap">
    <div class="head"><p class="kick">{e(t["reg_k"])}</p><h2>{e(t["reg_h"])}</h2><p>{e(t["reg_p"])}</p></div>
    {steps_html(t["steps"])}
    <p class="note">{e(t["reg_note"])}</p>
    <div class="btns center">
      <a class="btn btn-wa" href="{W}" target="_blank" rel="noopener">{WA_ICON}<span>{e(t["cta"])}</span></a>
      <a class="btn btn-light" href="{L("admissions")}">{e(t["learn"])}</a>
    </div>
  </div>
</section>
<section id="kontak" class="sec">
  <div class="wrap">
    <div class="head"><p class="kick">{e(t["con_k"])}</p><h2>{e(t["con_h"])}</h2></div>
    {contact_block(t, W)}
  </div>
</section>'''


def block(b, t, lang, W, i):
    k = b[0]
    alt = " alt" if i % 2 else ""
    sec = lambda inner, cls="": '<section class="sec%s%s"><div class="wrap">%s</div></section>' % (alt, cls, inner)
    if k == "text":
        return sec('<div class="prose"><h2>%s</h2>%s</div>' % (e(b[1]), "".join("<p>%s</p>" % e(p) for p in b[2])))
    if k == "split":
        return ('<section class="sec%s"><div class="wrap two"><div class="pic">%s</div><div><h2>%s</h2>%s</div></div></section>'
                % (alt, img(b[3], b[4]), e(b[1]), "".join("<p>%s</p>" % e(p) for p in b[2])))
    if k == "facts":
        return sec('<div class="head"><h2>%s</h2></div><dl class="stats big">%s</dl>' % (e(b[1]), "".join('<div><dt>%s</dt><dd><bdi>%s</bdi></dd></div>' % (e(l), e(n)) for n, l in b[2])))
    if k == "cards":
        intro = '<p>%s</p>' % e(b[2]) if b[2] else ""
        return sec('<div class="head"><h2>%s</h2>%s</div><div class="cards c%d">%s</div>' % (
            e(b[1]), intro, len(b[3]), "".join('<div class="best"><h3>%s</h3><p>%s</p></div>' % (e(a), e(c)) for a, c in b[3])))
    if k == "list":
        return sec('<div class="head"><h2>%s</h2></div><div class="fac one">%s</div>' % (e(b[1]), ticks(b[3])))
    if k == "level":
        _, lid, name, sub, desc, facts, pts, ik, ialt = b
        fx = "".join('<div><dt>%s</dt><dd>%s</dd></div>' % (e(a), e(c)) for a, c in facts)
        return ('<section id="%s" class="sec%s"><div class="wrap two level"><div class="pic">%s</div><div><p class="kick">%s</p><h2>%s</h2><p>%s</p>'
                '<dl class="kv" aria-label="%s">%s</dl>%s<a class="btn btn-wa sm" href="%s" target="_blank" rel="noopener">%s<span>%s</span></a></div></div></section>'
                % (lid, alt, img(ik, ialt), e(sub), e(name), e(desc), e(t["facts_l"]), fx, ticks(pts), wa(t, " (" + name + ")"), WA_ICON, e(t["more"])))
    if k == "photos":
        return '<div class="strip">%s</div>' % "".join(img(x, gal_alt(t, lang, x), sz="(min-width: 600px) 33vw, 100vw") for x in b[1])
    if k == "steps":
        return '<section class="sec reg"><div class="wrap"><div class="head"><h2>%s</h2></div>%s<div class="btns center"><a class="btn btn-wa" href="%s" target="_blank" rel="noopener">%s<span>%s</span></a><a class="btn btn-light" href="%s" target="_blank" rel="noopener">%s</a></div></div></section>' % (
            e(b[1]), steps_html(b[2]), W, WA_ICON, e(t["cta"]), FORM, e(t["reg_b2"]))
    if k == "faq":
        return sec('<div class="head"><h2>%s</h2></div><div class="faq">%s</div>' % (e(b[1]), "".join(
            "<details><summary>%s</summary><p>%s</p></details>" % (e(q), e(a)) for q, a in b[2])))
    if k == "quote":
        return sec('<figure class="quote"><blockquote><p>%s</p></blockquote><figcaption><strong><bdi>%s</bdi></strong><span>%s</span></figcaption></figure>' % (e(b[1]), e(b[2]), e(b[3])))
    if k == "note":
        return '<div class="wrap"><p class="pnote">%s</p></div>' % e(b[1])
    if k == "gallery":
        return sec(gallery(t, lang, True))
    if k == "contact":
        return sec(contact_block(t, W))
    raise ValueError(k)


def inner_body(pg, t, lang, L, W):
    p = P[lang][pg]
    out = f'''<section class="phero">
  {img(HERO_IMG[pg], gal_alt(t, lang, HERO_IMG[pg]), cls="hero-bg", eager=True)}
  <div class="wrap">
    <nav class="crumb" aria-label="Breadcrumb"><a href="{L("home")}">{e(t["home"])}</a><span aria-hidden="true">/</span><span aria-current="page">{e(p["title"])}</span></nav>
    <h1>{e(p["title"])}</h1>
    <p class="lead">{e(p["intro"])}</p>
  </div>
</section>
'''
    i = 0
    for b in p["blocks"]:
        out += block(b, t, lang, W, i) + "\n"
        if b[0] not in ("note", "photos"):
            i += 1
    if pg not in ("admissions",):
        out += f'''<section class="cta"><div class="wrap"><h2>{e(t["cta_h"])}</h2><p>{e(t["cta_p"])}</p>
<a class="btn btn-wa" href="{W}" target="_blank" rel="noopener">{WA_ICON}<span>{e(t["cta"])}</span></a></div></section>
'''
    return out


def page(lang, pg):
    t = T[lang]
    here = upath(lang, pg)
    url = DOMAIN + here
    L = lambda to: rel(here, upath(lang, to))
    A = rel(here, "/")
    A = "" if A == "./" else A
    W = wa(t)
    ASSET[0] = A
    if pg == "home":
        title, desc, og_img, og_alt_t = t["title"], t["desc"], DOMAIN + "/assets/img/og.jpg", t["hero_alt"]
    else:
        p = P[lang][pg]
        title, desc = p["meta_t"], p["meta_d"]
        og_img, og_alt_t = DOMAIN + "/assets/img/og.jpg", t["hero_alt"]
    fonts = ("Tajawal:wght@400;500;700;800" if lang == "ar"
             else "Manrope:wght@400..800")
    alts = "".join('<link rel="alternate" hreflang="%s" href="%s%s">\n' % (l, DOMAIN, upath(l, pg)) for l in LANGS)
    alts += '<link rel="alternate" hreflang="x-default" href="%s%s">\n' % (DOMAIN, upath("en", pg))
    og_loc = "".join('<meta property="og:locale:alternate" content="%s">\n' % T[l]["og_locale"] for l in LANGS if l != lang)
    ld = {"@context": "https://schema.org", "@type": "School", "name": "Mutiara School Bali", "alternateName": "Sekolah Mutiara Bali",
          "url": DOMAIN + T[lang]["path"], "logo": DOMAIN + "/" + IMG["logo"], "image": DOMAIN + "/assets/img/og.jpg", "email": EMAIL, "telephone": "+" + WA,
          "foundingDate": "2016-05-02", "description": T[lang]["desc"],
          "address": {"@type": "PostalAddress", "streetAddress": "Jl. Lingkar Timur Udayana No. 8", "addressLocality": "Jimbaran, Kuta Selatan",
                      "addressRegion": "Bali", "postalCode": "80361", "addressCountry": "ID"},
          "geo": {"@type": "GeoCoordinates", "latitude": -8.7953327, "longitude": 115.1782181}, "sameAs": [u for _, u in SOCIAL]}
    navl = "".join('<li><a href="%s"%s>%s</a></li>' % (L(x), ' aria-current="page"' if x == pg else "", e(n)) for x, n in zip(PAGES, t["nav"]))
    sw = "".join('<a href="%s" lang="%s" hreflang="%s"%s>%s</a>' % (rel(here, upath(l, pg)), l, l, ' aria-current="true"' if l == lang else "",
                                                               {"id": "ID", "en": "EN", "ar": "العربية"}[l]) for l in LANGS)
    body = home_body(t, lang, L, W) if pg == "home" else inner_body(pg, t, lang, L, W)
    return f'''<!DOCTYPE html>
<html lang="{lang}" dir="{t["dir"]}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{url}">
{alts}<meta property="og:type" content="website">
<meta property="og:site_name" content="Mutiara School Bali">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{og_img}">
<meta property="og:image:alt" content="{e(og_alt_t)}">
<meta property="og:locale" content="{t["og_locale"]}">
{og_loc}<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0c6b3c">
<link rel="icon" href="{A}favicon.ico" sizes="any">
<link rel="icon" href="{A}assets/img/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="{A}assets/img/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family={fonts}&display=swap">
<link rel="stylesheet" href="{A}assets/css/style.css">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
</head>
<body id="top">
<a class="skip" href="#main">{e(t["skip"])}</a>
<header class="hdr">
  <div class="wrap hdr-in">
    <a class="brand" href="{L("home")}"><span class="crest">{img("logo", t["logo_alt"], eager=True)}</span><span class="bname" dir="ltr"><b>Mutiara School</b><small>Bali · Jimbaran</small></span></a>
    <button class="burger" type="button" aria-expanded="false" aria-controls="nav" aria-label="{e(t["menu"])}"><span></span><span></span><span></span></button>
    <nav id="nav" class="nav" aria-label="{e(t["menu"])}">
      <ul>{navl}</ul>
      <div class="lang" role="group" aria-label="{e(t["lang_label"])}">{sw}</div>
      <a class="btn btn-wa sm" href="{W}" target="_blank" rel="noopener">{WA_ICON}<span>{e(t["cta"])}</span></a>
    </nav>
  </div>
</header>
<main id="main">
{body}
</main>
<footer class="ftr">
  <div class="wrap">
    <div class="fgrid">
      <div><h2>Mutiara School Bali</h2><p class="fsub">Jimbaran</p><p class="motto">{e(t["foot"].split("·")[-1].strip())}</p><p>{e(t["addr"])}</p></div>
      <nav aria-label="{e(t["foot_nav"])}"><h3>{e(t["foot_nav"])}</h3><ul>{"".join('<li><a href="%s">%s</a></li>' % (L(x), e(n)) for x, n in zip(PAGES, t["nav"]))}</ul></nav>
      <div><h3>{e(t["con_k"])}</h3><p><a href="{W}" target="_blank" rel="noopener"><bdi dir="ltr">{WA_SHOW}</bdi></a></p><p><a href="mailto:{EMAIL}"><bdi dir="ltr">{EMAIL}</bdi></a></p><p>{e(t["hours"])}</p></div>
      <div><h3>{e(t["social_h"])}</h3><ul>{"".join('<li><a href="%s" target="_blank" rel="noopener">%s</a></li>' % (u, n) for n, u in SOCIAL)}</ul></div>
    </div>
    <p class="copy">© <span id="yr">2026</span> Mutiara School Bali. {e(t["rights"])}</p>
  </div>
</footer>
<a class="fab" href="{W}" target="_blank" rel="noopener" aria-label="{e(t["wa_float"])}">{WA_ICON}</a>
<script src="{A}assets/js/main.js" defer></script>
</body>
</html>
'''


def favicons():
    from PIL import Image, ImageDraw
    d = os.path.join(OUT, "assets", "img")
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "favicon.svg"), "w") as f:
        f.write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="14" fill="#0c6b3c"/>'
                '<path d="M32 10 50 16v16c0 12-8 19-18 22-10-3-18-10-18-22V16Z" fill="#fdd100"/>'
                '<circle cx="32" cy="31" r="9" fill="#0c6b3c"/><circle cx="32" cy="31" r="4" fill="#fdd100"/></svg>')
    S = 512; k = S / 64
    im = Image.new("RGBA", (S, S), (0, 0, 0, 0)); dr = ImageDraw.Draw(im)
    dr.rounded_rectangle([0, 0, S - 1, S - 1], radius=112, fill="#0c6b3c")
    dr.polygon([(32*k, 10*k), (50*k, 16*k), (50*k, 34*k), (44*k, 46*k), (32*k, 54*k), (20*k, 46*k), (14*k, 34*k), (14*k, 16*k)], fill="#fdd100")
    dr.ellipse([23*k, 22*k, 41*k, 40*k], fill="#0c6b3c"); dr.ellipse([28*k, 27*k, 36*k, 35*k], fill="#fdd100")
    im.resize((180, 180), Image.LANCZOS).save(os.path.join(d, "apple-touch-icon.png"))
    im.save(os.path.join(OUT, "favicon.ico"), sizes=[(16, 16), (32, 32), (48, 48)])


HTACCESS = """ErrorDocument 404 /404.html

# Kompresi teks
<IfModule mod_deflate.c>
  AddOutputFilterByType DEFLATE text/html text/css application/javascript text/javascript image/svg+xml application/xml text/xml application/json text/plain
</IfModule>

# Cache browser: gambar/css/js lama, halaman HTML singkat
<IfModule mod_expires.c>
  ExpiresActive On
  ExpiresByType image/webp "access plus 1 year"
  ExpiresByType image/jpeg "access plus 1 year"
  ExpiresByType image/png "access plus 1 year"
  ExpiresByType image/svg+xml "access plus 1 year"
  ExpiresByType image/x-icon "access plus 1 year"
  ExpiresByType text/css "access plus 1 month"
  ExpiresByType application/javascript "access plus 1 month"
  ExpiresByType text/html "access plus 10 minutes"
</IfModule>
<IfModule mod_mime.c>
  AddType image/webp .webp
</IfModule>
"""


def minify_css(c):
    c = re.sub(r"/\*.*?\*/", "", c, flags=re.S)
    c = re.sub(r"\s+", " ", c)
    c = re.sub(r"\s*([{};,>])\s*", r"\1", c)
    c = re.sub(r":\s+", ":", c)
    return c.replace(";}", "}").strip()


def assets():
    from PIL import Image
    src = os.path.join(ROOT, "src", "assets")
    os.makedirs(os.path.join(OUT, "assets", "css")); os.makedirs(os.path.join(OUT, "assets", "js")); os.makedirs(os.path.join(OUT, "assets", "img", "foto"))
    with open(os.path.join(OUT, "assets", "css", "style.css"), "w") as f:
        f.write(minify_css(open(os.path.join(src, "css", "style.css")).read()))
    js = open(os.path.join(src, "js", "main.js")).read()
    with open(os.path.join(OUT, "assets", "js", "main.js"), "w") as f:
        f.write(re.sub(r"\n\s*", "", re.sub(r"\s*([{}();,=<>?:+])\s*", r"\1", js)).replace("functionf", "function f").replace("returnh", "return h"))
    fd = os.path.join(src, "img", "foto")
    for fn in sorted(os.listdir(fd)):
        im = Image.open(os.path.join(fd, fn)).convert("RGB"); k = fn[:-4]
        small = 800 if k == "hero-l" else 480
        im.save(os.path.join(OUT, "assets", "img", "foto", k + ".webp"), "WEBP", quality=68 if k == "hero-l" else 72, method=6)
        im.resize((small, round(im.height * small / im.width)), Image.LANCZOS).save(os.path.join(OUT, "assets", "img", "foto", k + "-s.webp"), "WEBP", quality=70, method=6)
        if k == "hero-l":
            im.resize((1200, round(im.height * 1200 / im.width)), Image.LANCZOS).crop((0, 37, 1200, 667)).save(os.path.join(OUT, "assets", "img", "og.jpg"), quality=80, optimize=True, progressive=True)
    c = Image.open(os.path.join(src, "img", "crest.png")).convert("RGB")
    c.resize((96, round(c.height * 96 / c.width)), Image.LANCZOS).save(os.path.join(OUT, "assets", "img", "crest.webp"), "WEBP", quality=90, method=6)


def main():
    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    assets()
    urls = ""
    for pg in PAGES:
        for l in LANGS:
            d = os.path.join(OUT, upath(l, pg).strip("/"))
            os.makedirs(d, exist_ok=True)
            out = page(l, pg)
            if l == "ar":  # rentang angka (jam, kelas) tetap terbaca kiri-ke-kanan di teks RTL
                out = re.sub(r"(\d[\d:.]*) ?– ?(\d[\d:.]*)", "\u2066\\1–\\2\u2069", out)
            with open(os.path.join(d, "index.html"), "w", encoding="utf-8") as f:
                f.write(out)
            links = "".join('    <xhtml:link rel="alternate" hreflang="%s" href="%s%s"/>\n' % (x, DOMAIN, upath(x, pg)) for x in LANGS)
            links += '    <xhtml:link rel="alternate" hreflang="x-default" href="%s%s"/>\n' % (DOMAIN, upath("en", pg))
            urls += "  <url>\n    <loc>%s%s</loc>\n%s  </url>\n" % (DOMAIN, upath(l, pg), links)
    favicons()
    with open(os.path.join(OUT, "sitemap.xml"), "w") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
                'xmlns:xhtml="http://www.w3.org/1999/xhtml">\n%s</urlset>\n' % urls)
    with open(os.path.join(OUT, "robots.txt"), "w") as f:
        f.write("User-agent: *\nAllow: /\n\nSitemap: %s/sitemap.xml\n" % DOMAIN)
    with open(os.path.join(OUT, "404.html"), "w", encoding="utf-8") as f:
        f.write('<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">'
                '<meta name="robots" content="noindex"><title>Page not found – Mutiara School Bali</title><link rel="stylesheet" href="/assets/css/style.css"></head>'
                '<body><main class="phero" style="min-height:100vh"><div class="wrap"><h1>Page not found</h1><p class="lead">Halaman tidak ditemukan</p>'
                '<p class="btns"><a class="btn btn-wa" href="/">Home</a><a class="btn btn-ghost" href="/id/">Beranda</a></p></div></main></body></html>')
    with open(os.path.join(OUT, ".htaccess"), "w") as f:
        f.write(HTACCESS)
    # untuk GitHub Pages
    with open(os.path.join(OUT, "CNAME"), "w") as f:
        f.write("mutiaraschool.com\n")
    open(os.path.join(OUT, ".nojekyll"), "w").close()
    print("Build selesai ->", OUT)


if __name__ == "__main__":
    main()
