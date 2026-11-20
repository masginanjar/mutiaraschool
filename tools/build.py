#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Bangun website statis Mutiara School Bali ke public_html/.
Jalankan: python3 tools/build.py && python3 tools/check.py
Isi teks: tools/sitedata.py. Foto asli Canva: src/assets/img/canva/. Foto galeri lama: src/assets/img/foto/."""
import html, json, os, posixpath, re, shutil, sys
from urllib.parse import quote

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from sitedata import *  # noqa  (tools/sitedata.py)
sys.path.insert(0, os.path.join(HERE, "old"))
from pages import XALT  # alt teks foto galeri lama  # noqa
from content import T as OLDT  # noqa

ROOT = os.path.dirname(HERE)
SRC = os.path.join(ROOT, "src", "assets")
OUT = os.path.join(ROOT, "public_html")
e = html.escape
SIZES = {}  # kunci gambar -> (w, h, folder, small_w)

WA_ICON = ('<svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2" '
           'stroke-linecap="round" stroke-linejoin="round"><path d="M12 3a9 9 0 0 0-7.8 13.5L3 21l4.6-1.2A9 9 0 1 0 12 3Z"/><path d="M9 8.5c0 3.5 3 6.5 6.5 6.5"/></svg>')
CHECK = ('<svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true"><path fill="none" stroke="currentColor" stroke-width="2.8" '
         'stroke-linecap="round" stroke-linejoin="round" d="m5 12.5 4.5 4.5L19 7.5"/></svg>')
ARROW = '<span class="arr" aria-hidden="true">→</span>'
OLD_GAL = ["g1", "hero", "g3", "x2", "g5", "g6", "about", "x0", "x4", "x5", "x8", "x9", "sd", "smp", "x13", "paud", "x1", "x3",
           "x24", "x28", "g2", "x18", "x19", "x20", "x21", "x23", "g4", "x25", "x26", "g7"]
NEW_GAL = ["narasi", "language", "research", "literacy", "leadership", "sentra-art", "sentra-cook", "sentra-block"]


# ------------------------------------------------------------------ util
def upath(lang, pg):
    base = T[lang]["path"]
    return base if pg == "home" else base + SLUG[lang][pg] + "/"


def rel(frm, to):
    r = posixpath.relpath(to, frm)
    return "./" if r == "." else r + "/"


def wa(t, extra=""):
    return e("https://wa.me/%s?text=%s" % (WA, quote(t["wa_msg"] + extra)))


def alt(lang, key):
    if key in ALT and ALT[key]:
        return ALT[key][0 if lang == "en" else 1]
    if key == "hero-kids":
        return T[lang]["hero_alt"]
    if key == "salam":
        return T[lang]["salam_alt"]
    if key.startswith("fac-"):
        return T[lang]["pages"]["facilities"]["labels"][FACILITIES.index(key)]
    # foto galeri lama
    ot = OLDT[lang]
    if key.startswith("g") and key[1:].isdigit():
        return ot["gal_alt"][int(key[1:]) - 1]
    if key in XALT:
        return XALT[key][lang]
    return {"hero": ot["hero_alt"], "paud": ot["progs"][0][4], "sd": ot["progs"][1][4], "smp": ot["progs"][2][4], "about": ot["about_alt"]}[key]


class Ctx:
    A = ""   # prefix ke akar situs


def img(key, alt_text, cls="", eager=False, sizes="(min-width: 900px) 40vw, 100vw"):
    w, h, folder, sw = SIZES[key]
    base = "%sassets/img/%s/%s" % (Ctx.A, folder, key)
    srcset = ' srcset="%s-s.webp %dw, %s.webp %dw" sizes="%s"' % (base, sw, base, w, sizes) if sw else ""
    return '<img src="%s.webp"%s alt="%s" width="%d" height="%d"%s%s>' % (
        base, srcset, e(alt_text), w, h, ' fetchpriority="high"' if eager else ' loading="lazy" decoding="async"',
        ' class="%s"' % cls if cls else "")


def png(key, alt_text, cls=""):
    w, h, _, _ = SIZES[key]
    return '<img src="%sassets/img/canva/%s.png" alt="%s" width="%d" height="%d" loading="lazy" decoding="async"%s>' % (
        Ctx.A, key, e(alt_text), w, h, ' class="%s"' % cls if cls else "")


def ticks(items, cls="ticks"):
    return '<ul class="%s">%s</ul>' % (cls, "".join("<li>%s<span>%s</span></li>" % (CHECK, e(x)) for x in items))


def chips(items):
    return '<ul class="chips">%s</ul>' % "".join("<li>%s</li>" % e(x) for x in items)


def head(k, h, p=None, cls=""):
    return '<div class="head %s"><p class="kick">%s</p><h2>%s</h2>%s</div>' % (cls, e(k), e(h), "<p>%s</p>" % e(p) if p else "")


def btn_wa(t, cls="btn btn-wa", extra=""):
    return '<a class="%s" href="%s" target="_blank" rel="noopener">%s<span>%s</span></a>' % (cls, wa(t, extra), WA_ICON, e(t["cta"]))


# ------------------------------------------------------------------ blok yang dipakai ulang
def accr_band(t):
    lv = [("KB", "kb"), ("TK", "tk"), ("SD", "sd"), ("SMP", "smp")]
    return ('<div class="accr">%s<div><p class="accr-t">%s</p><p class="accr-s">%s</p><ul class="lvchips">%s</ul></div></div>'
            % (png("badge-a", t["accr"], "accr-badge"), e(t["accr"]), e(t["accr_sub"]),
               "".join('<li class="c-%s">%s</li>' % (c, n) for n, c in lv)))


def ppdb_flow(t):
    steps = "".join('<li><span class="num">%d</span><span>%s</span></li>' % (i, e(s)) for i, s in enumerate(t["steps"], 1))
    return ('<div class="flow"><p class="flow-start">%s</p><ol class="flow-steps">%s</ol><p class="flow-end">%s</p></div>'
            % (e(t["ppdb_lead"]), steps, e(t["ppdb_end"])))


def ppdb_section(t, L, full=False):
    return f'''<section id="pendaftaran" class="sec ppdb">
  <div class="wrap two">
    <div>
      <p class="kick light">{e(t["ppdb_k"])}</p>
      <h2>{e(t["ppdb_h"])}</h2>
      <p class="tag">{e(t["ppdb_tag"])}</p>
      <p class="lead-l">{e(t["notice"])}.</p>
      <div class="btns">{btn_wa(t)}<a class="btn btn-light" href="{FORM}" target="_blank" rel="noopener">{e(t["form"])}</a></div>
      {"" if full else '<p class="more"><a class="link light" href="%s">%s %s</a></p>' % (L("admissions"), e(t["notice_more"]), ARROW)}
    </div>
    {ppdb_flow(t)}
  </div>
</section>'''


def testimonials(t):
    cards = ""
    for i, (n, role, q) in enumerate(t["testi"], 1):
        cards += ('<figure class="testi">%s<blockquote><p>“%s”</p></blockquote><figcaption><strong>%s</strong><span>%s</span></figcaption></figure>'
                  % (img("testi-%d" % i, n, "testi-img", sizes="96px"), e(q), e(n), e(role)))
    note = '<p class="small">%s</p>' % e(t["ts_note"]) if t["ts_note"] else ""
    return '<section class="sec"><div class="wrap">%s<div class="testis">%s</div>%s</div></section>' % (head(t["ts_k"], t["ts_h"]), cards, note)


def partners(t):
    logos = "".join('<li>%s</li>' % png(k, "Logo " + n) for k, n in PARTNERS)
    return '<section class="sec partners"><div class="wrap">%s<ul class="logos">%s</ul></div></section>' % (head(t["pt_k"], t["pt_h"]), logos)


def contact_block(t, W):
    soc = "".join('<li><a href="%s" target="_blank" rel="noopener">%s</a></li>' % (u, n) for n, u in SOCIAL)
    mails = "".join('<p><a href="mailto:%s"><bdi dir="ltr">%s</bdi></a></p>' % (m, m) for m in EMAILS)
    return f'''<div class="two top">
      <address class="card con">
        <h3>{e(t["addr_h"])}</h3><p>{e(t["addr"])}</p>
        <h3>{e(t["hours_h"])}</h3><p>{e(t["hours"])}</p>
        <h3>{e(t["wa_h"])}</h3><p><a href="{W}" target="_blank" rel="noopener"><bdi dir="ltr">{WA_SHOW}</bdi></a></p>
        <h3>{e(t["mail_h"])}</h3>{mails}
        <h3>{e(t["social_h"])}</h3><ul class="soc">{soc}</ul>
        <a class="btn btn-ghost" href="{MAP_LINK}" target="_blank" rel="noopener">{e(t["map_b"])}</a>
      </address>
      <div class="map"><iframe src="{e(MAP_EMBED)}" title="{e(t["map_title"])}" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe></div>
    </div>'''


def cta(t):
    return '<section class="cta"><div class="wrap"><h2>%s</h2><p>%s</p>%s</div></section>' % (e(t["cta_h"]), e(t["cta_p"]), btn_wa(t))


# ------------------------------------------------------------------ beranda
def home_body(t, lang, L, W):
    stats = "".join('<div><dt>%s</dt><dd>%s</dd></div>' % (e(b), e(a)) for a, b in t["stats"])
    why = "".join('<li><span class="n">%d</span><h3>%s</h3><p>%s</p></li>' % (i, e(a), e(b)) for i, (a, b) in enumerate(t["why"], 1))
    lv = "".join(
        '<a class="level lv-%s" href="%s#%s"><span class="lv-pic">%s</span><span class="lv-b"><span class="lv-age">%s</span>'
        '<strong>%s</strong><span class="lv-sub">%s</span><span class="lv-p">%s</span><span class="link">%s %s</span></span></a>'
        % (k, L("programs"), k, img(k + "-kid", alt(lang, k + "-kid"), sizes="(min-width: 900px) 30vw, 90vw"), e(age), e(n), e(s), e(p), e(t["learn"]), ARROW)
        for k, n, s, p, age in t["levels"])
    pg = "".join('<article class="pcard">%s<div><h3>%s</h3><p>%s</p></div></article>'
                 % (img(k, alt(lang, k), sizes="(min-width: 900px) 30vw, 100vw"), e(n), e(p)) for k, n, p in t["progs"])
    ach = "".join("<li>%s<span>%s</span></li>" % (CHECK, e(x)) for x in t["ach"][:8])
    fac = "".join('<figure class="ftile">%s<figcaption>%s</figcaption></figure>'
                  % (img(k, alt(lang, k), sizes="(min-width: 900px) 25vw, 50vw"), e(alt(lang, k))) for k in FACILITIES[:4])
    return f'''<section class="hero">
  <div class="wrap hero-in">
    <div class="hero-t">
      <p class="eyebrow">{e(t["welcome"])}</p>
      <h1>{e(t["h1"])}</h1>
      <p class="motto">{e(t["motto"])}</p>
      <p class="lead">{e(t["hero_p"])}</p>
      <div class="btns">{btn_wa(t)}<a class="btn btn-ghost" href="{L("programs")}">{e(t["hero_b2"])}</a></div>
      {accr_band(t)}
    </div>
    <div class="hero-m">{img("hero-kids", t["hero_alt"], eager=True, sizes="(min-width: 900px) 52vw, 100vw")}</div>
  </div>
</section>
<p class="notice"><a href="{L("admissions")}"><strong>{e(t["notice"])}</strong> <span>{e(t["notice_more"])} {ARROW}</span></a></p>
<section class="band"><div class="wrap"><dl class="stats">{stats}</dl></div></section>
<section class="sec">
  <div class="wrap two">
    <div class="pic ring">{img("salam", t["salam_alt"])}</div>
    <div>
      <p class="kick">{e(t["salam_k"])}</p><h2>{e(t["salam_h"])}</h2>
      <p>{e(t["salam_short"])}</p>
      <p class="sign">{e(t["director"])}<span>{e(t["director_role"])}</span></p>
      <p class="more"><a class="link" href="{L("about")}">{e(t["learn"])} {ARROW}</a></p>
    </div>
  </div>
</section>
<section class="sec soft">
  <div class="wrap">{head(t["why_k"], t["why_h"])}<ol class="why">{why}</ol></div>
</section>
<section id="program" class="sec">
  <div class="wrap">{head(t["lv_k"], t["lv_h"], t["lv_p"])}<div class="levels">{lv}</div></div>
</section>
<section class="sec soft">
  <div class="wrap">{head(t["pg_k"], t["pg_h"])}<div class="pcards">{pg}</div></div>
</section>
<section class="sec">
  <div class="wrap two">
    <div>{head(t["ach_k"], t["ach_h"], cls="left")}<ul class="ach">{ach}</ul><p class="small">{e(t["ach_more"])}</p></div>
    <div><div class="ftiles">{fac}</div><p class="more"><a class="link" href="{L("facilities")}">{e(t["nav"][3])} {ARROW}</a></p></div>
  </div>
</section>
{testimonials(t)}
{ppdb_section(t, L)}
{partners(t)}
<section id="kontak" class="sec soft">
  <div class="wrap">{head(t["con_k"], t["con_h"], t["con_p"])}{contact_block(t, W)}</div>
</section>'''


# ------------------------------------------------------------------ halaman dalam
def phero(t, L, p, key, lang):
    return f'''<section class="phero">
  <div class="wrap phero-in">
    <div>
      <nav class="crumb" aria-label="Breadcrumb"><a href="{L("home")}">{e(t["home"])}</a><span aria-hidden="true">/</span><span aria-current="page">{e(p["title"])}</span></nav>
      <h1>{e(p["title"])}</h1>
      <p class="lead">{e(p["intro"])}</p>
    </div>
    <div class="phero-pic">{img(key, alt(lang, key), eager=True, sizes="(min-width: 900px) 40vw, 100vw")}</div>
  </div>
</section>'''


def about_body(t, lang, L, W):
    p = t["pages"]["about"]
    salam = "".join("<p>%s</p>" % e(x) for x in t["salam_full"])
    fnd = "".join('<li>%s<strong>%s</strong><span>%s</span></li>' % (img("founder-%d" % i, n, "round", sizes="120px"), e(n), e(p["roles"][r]))
                  for i, (n, r) in enumerate(FOUNDERS, 1))
    mission = "".join("<li>%s</li>" % e(m) for m in p["mission"])
    return phero(t, L, p, "building", lang) + f'''
<section class="sec">
  <div class="wrap two">
    <div class="pic ring">{img("salam", t["salam_alt"])}</div>
    <div><p class="kick">{e(t["salam_k"])}</p><h2>{e(t["salam_h"])}</h2>{salam}
      <p class="sign">{e(t["salam_sign"])} {e(t["director"])}<span>{e(t["director_role"])}</span></p></div>
  </div>
</section>
<section class="band"><div class="wrap"><dl class="stats">{"".join('<div><dt>%s</dt><dd>%s</dd></div>' % (e(b), e(a)) for a, b in t["stats"])}</dl></div></section>
<section class="sec">
  <div class="wrap narrow"><h2>{e(p["hist_h"])}</h2>{"".join("<p>%s</p>" % e(x) for x in p["hist"])}</div>
</section>
<section class="sec soft">
  <div class="wrap"><div class="head"><h2>{e(p["founders_h"])}</h2></div><ul class="founders">{fnd}</ul></div>
</section>
<section class="sec">
  <div class="wrap narrow"><h2>{e(p["profile_h"])}</h2><p>{e(p["profile"])}</p></div>
  <div class="wrap vm">
    <div class="card vis"><h3>{e(p["vision_h"])}</h3><p>{e(p["vision"])}</p></div>
    <div class="card mis"><h3>{e(p["mission_h"])}</h3><ol>{mission}</ol></div>
  </div>
</section>
<section class="sec soft">
  <div class="wrap two">
    <div><h2>{e(p["teachers_h"])}</h2><p>{e(p["teachers"])}</p></div>
    <div class="pic ring">{img("language", alt(lang, "language"))}</div>
  </div>
</section>
{testimonials(t)}
{cta(t)}'''


def level_block(t, lang, k, d, P, alt_cls):
    facts = '<dl class="kv"><div><dt>%s</dt><dd>%s</dd></div>' % (e(P["lv_hours"]), e(d["hours"])) if isinstance(d.get("hours"), str) else '<dl class="kv">'
    if isinstance(d.get("hours"), list):
        facts += "".join('<div><dt>%s</dt><dd>%s</dd></div>' % (e(a), e(b)) for a, b in d["hours"])
    if d.get("entry"):
        facts += '<div><dt>%s</dt><dd>%s</dd></div>' % (e(P["lv_entry"]), e(d["entry"]))
    facts += "</dl>"
    prof = "".join('<li><h4>%s</h4><p>%s</p></li>' % (e(a), e(b)) for a, b in d["profile"])
    extra = ""
    if d.get("sentra"):
        sent = "".join('<figure>%s<figcaption>%s</figcaption></figure>' % (img(s, alt(lang, s), sizes="(min-width: 900px) 28vw, 100vw"), e(c)) for s, c in d["sentras"])
        extra += '<div class="sentra"><h3>%s</h3><p>%s</p><div class="sentras">%s</div></div>' % (e(d["sentra_h"]), e(d["sentra"]), sent)
    lists = ""
    for lab, key in ((P["lv_subjects"], "subjects"), (P["lv_clubs"], "clubs"), (P["lv_extra"], "extra"), (P["lv_progs"], "progs")):
        if d.get(key):
            lists += '<div class="lst"><h3>%s</h3>%s</div>' % (e(lab), chips(d[key]))
    return f'''<section id="{k}" class="sec lvsec lv-{k}{alt_cls}">
  <div class="wrap">
    <div class="lvhead">
      <div class="lvpic">{img(k + "-kid", alt(lang, k + "-kid"), sizes="(min-width: 900px) 30vw, 70vw")}</div>
      <div><p class="kick">{e(d["sub"])}</p><h2>{e(d["name"])}</h2>{facts}{btn_wa(t, "btn btn-wa sm", " (" + d["name"] + ")")}</div>
    </div>
    {extra}
    <h3 class="sub-h">{e(P["lv_profile"])}</h3>
    <ul class="prof">{prof}</ul>
    <div class="lists">{lists}</div>
  </div>
</section>'''


def programs_body(t, lang, L, W):
    P = t["pages"]["programs"]
    best = "".join('<li><span class="letter" aria-hidden="true">%s</span><h3>%s</h3><p>%s</p></li>' % (a, e(b), e(c)) for a, b, c in P["best"])
    pg = "".join('<article class="pcard">%s<div><h3>%s</h3><p>%s</p></div></article>'
                 % (img(k, alt(lang, k), sizes="(min-width: 900px) 30vw, 100vw"), e(n), e(p)) for k, n, p in t["progs"])
    nav = "".join('<a href="#%s" class="c-%s">%s</a>' % (k, k, e(P[k]["name"])) for k in ("paud", "sd", "smp"))
    return phero(t, L, P, "narasi", lang) + f'''
<nav class="jump" aria-label="{e(P["title"])}"><div class="wrap">{nav}</div></nav>
<section class="sec">
  <div class="wrap">
    <div class="head"><h2>{e(P["cur_h"])}</h2></div>
    <div class="two top">
      <div class="card pad"><h3>{e(P["nat_h"])}</h3>{"".join("<p>%s</p>" % e(x) for x in P["nat"])}</div>
      <div class="card pad"><h3>{e(P["best_h"])}</h3><p>{e(P["best_p"])}</p></div>
    </div>
    <ul class="best">{best}</ul>
  </div>
</section>
<section class="sec soft">
  <div class="wrap narrow"><h2>{e(P["quran_h"])}</h2><p>{e(P["quran"])}</p></div>
</section>
{level_block(t, lang, "paud", P["paud"], P, "")}
{level_block(t, lang, "sd", P["sd"], P, " soft")}
{level_block(t, lang, "smp", P["smp"], P, "")}
<section class="sec soft">
  <div class="wrap">{head(t["pg_k"], t["pg_h"])}<div class="pcards">{pg}</div></div>
</section>
{cta(t)}'''


def facilities_body(t, lang, L, W):
    P = t["pages"]["facilities"]
    tiles = "".join('<figure class="ftile">%s<figcaption>%s</figcaption></figure>'
                    % (img(k, P["labels"][i], sizes="(min-width: 900px) 30vw, (min-width: 600px) 45vw, 100vw"), e(P["labels"][i]))
                    for i, k in enumerate(FACILITIES))
    return phero(t, L, P, "fac-sport", lang) + f'''
<section class="sec"><div class="wrap"><div class="ftiles big">{tiles}</div></div></section>
{cta(t)}'''


def gallery_body(t, lang, L, W):
    P = t["pages"]["gallery"]
    keys = NEW_GAL + OLD_GAL
    g = "".join("<figure>%s</figure>" % img(k, alt(lang, k), sizes="(min-width: 900px) 25vw, 50vw") for k in keys)
    return phero(t, L, P, "leadership", lang) + f'''
<section class="sec"><div class="wrap"><div class="gal">{g}</div><p class="small center">{e(P["note"])}</p></div></section>
{cta(t)}'''


def admissions_body(t, lang, L, W):
    P = t["pages"]["admissions"]
    req = "".join('<div><dt>%s</dt><dd>%s</dd></div>' % (e(a), e(b)) for a, b in P["req"])
    faq = "".join("<details><summary>%s</summary><p>%s</p></details>" % (e(q), e(a)) for q, a in P["faq"])
    return phero(t, L, P, "literacy", lang) + ppdb_section(t, L, full=True) + f'''
<section class="sec">
  <div class="wrap two top">
    <div><h2>{e(P["req_h"])}</h2><dl class="kv">{req}</dl></div>
    <div><h2>{e(P["docs_h"])}</h2>{ticks(P["docs"])}</div>
  </div>
</section>
<section class="sec soft"><div class="wrap narrow"><h2>{e(P["faq_h"])}</h2><div class="faq">{faq}</div></div></section>
{partners(t)}'''


def contact_body(t, lang, L, W):
    P = t["pages"]["contact"]
    return phero(t, L, P, "building", lang) + '<section class="sec"><div class="wrap">%s</div></section>' % contact_block(t, W)


BODY = dict(home=home_body, about=about_body, programs=programs_body, facilities=facilities_body,
            gallery=gallery_body, admissions=admissions_body, contact=contact_body)


# ------------------------------------------------------------------ halaman
def page(lang, pg):
    t = T[lang]
    here = upath(lang, pg)
    url = DOMAIN + here
    L = lambda to: rel(here, upath(lang, to))
    A = rel(here, "/")
    Ctx.A = "" if A == "./" else A
    W = wa(t)
    if pg == "home":
        title, desc = t["title"], t["desc"]
    else:
        title, desc = t["pages"][pg]["meta_t"], t["pages"][pg]["meta_d"]
    alts = "".join('<link rel="alternate" hreflang="%s" href="%s%s">\n' % (l, DOMAIN, upath(l, pg)) for l in LANGS)
    alts += '<link rel="alternate" hreflang="x-default" href="%s%s">\n' % (DOMAIN, upath("en", pg))
    ld = {"@context": "https://schema.org", "@type": "School", "name": "Mutiara School Bali", "alternateName": "Sekolah Mutiara Bali",
          "url": DOMAIN + "/", "logo": DOMAIN + "/assets/img/canva/crest.png", "image": DOMAIN + "/assets/img/og.jpg",
          "email": EMAILS[0], "telephone": "+" + WA, "foundingDate": "2016-05-02", "description": T[lang]["desc"],
          "address": {"@type": "PostalAddress", "streetAddress": "Jl. Lingkar Timur Udayana No. 8", "addressLocality": "Jimbaran, Kuta Selatan",
                      "addressRegion": "Bali", "postalCode": "80361", "addressCountry": "ID"},
          "geo": {"@type": "GeoCoordinates", "latitude": -8.7953327, "longitude": 115.1782181}, "sameAs": [u for _, u in SOCIAL]}
    navl = "".join('<li><a href="%s"%s>%s</a></li>' % (L(x), ' aria-current="page"' if x == pg else "", e(n)) for x, n in zip(PAGES, t["nav"]))
    sw = "".join('<a href="%s" lang="%s" hreflang="%s"%s>%s</a>' % (rel(here, upath(l, pg)), l, l, ' aria-current="true"' if l == lang else "",
                                                               {"id": "ID", "en": "EN"}[l]) for l in LANGS)
    body = BODY[pg](t, lang, L, W)
    soc = "".join('<li><a href="%s" target="_blank" rel="noopener">%s</a></li>' % (u, n) for n, u in SOCIAL)
    return f'''<!DOCTYPE html>
<html lang="{lang}">
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
<meta property="og:image" content="{DOMAIN}/assets/img/og.jpg">
<meta property="og:image:alt" content="{e(t["hero_alt"])}">
<meta property="og:locale" content="{t["og_locale"]}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#2e9f45">
<link rel="icon" href="{Ctx.A}favicon.ico" sizes="any">
<link rel="icon" href="{Ctx.A}assets/img/favicon.png" type="image/png">
<link rel="apple-touch-icon" href="{Ctx.A}assets/img/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap">
<link rel="stylesheet" href="{Ctx.A}assets/css/style.css">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
</head>
<body>
<a class="skip" href="#main">{e(t["skip"])}</a>
<header class="hdr">
  <div class="wrap hdr-in">
    <a class="brand" href="{L("home")}">{png("crest", t["logo_alt"], "crest")}<span class="bname"><b>Mutiara School</b><small>Bali · Jimbaran</small></span></a>
    <button class="burger" type="button" aria-expanded="false" aria-controls="nav" aria-label="{e(t["menu"])}"><span></span><span></span><span></span></button>
    <nav id="nav" class="nav" aria-label="{e(t["menu"])}">
      <ul>{navl}</ul>
      <div class="lang" role="group" aria-label="{e(t["lang_label"])}">{sw}</div>
      {btn_wa(t, "btn btn-wa sm")}
    </nav>
  </div>
</header>
<main id="main">
{body}
</main>
<footer class="ftr">
  <div class="wrap">
    <div class="fgrid">
      <div class="fbrand">{png("crest", t["logo_alt"], "crest")}<div><h2>Mutiara School Bali</h2><p class="motto-f">{e(t["motto"])}</p><p>{e(t["addr"])}</p></div></div>
      <nav aria-label="{e(t["foot_nav"])}"><h3>{e(t["foot_nav"])}</h3><ul>{"".join('<li><a href="%s">%s</a></li>' % (L(x), e(n)) for x, n in zip(PAGES, t["nav"]))}</ul></nav>
      <div><h3>{e(t["con_k"])}</h3><p><a href="{W}" target="_blank" rel="noopener"><bdi dir="ltr">{WA_SHOW}</bdi></a></p>{"".join('<p><a href="mailto:%s">%s</a></p>' % (m, m) for m in EMAILS)}<p>{e(t["hours"])}</p></div>
      <div><h3>{e(t["social_h"])}</h3><ul>{soc}</ul></div>
    </div>
    <p class="copy">© <span id="yr">2026</span> Mutiara School Bali. {e(t["rights"])}</p>
  </div>
</footer>
<a class="fab" href="{W}" target="_blank" rel="noopener" aria-label="{e(t["wa_float"])}">{WA_ICON}</a>
<script src="{Ctx.A}assets/js/main.js" defer></script>
</body>
</html>
'''


# ------------------------------------------------------------------ aset
HTACCESS = """ErrorDocument 404 /404.html

<IfModule mod_deflate.c>
  AddOutputFilterByType DEFLATE text/html text/css application/javascript text/javascript image/svg+xml application/xml text/xml application/json text/plain
</IfModule>
<IfModule mod_expires.c>
  ExpiresActive On
  ExpiresByType image/webp "access plus 1 year"
  ExpiresByType image/jpeg "access plus 1 year"
  ExpiresByType image/png "access plus 1 year"
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
    for d in ("css", "js", "img/foto", "img/canva"):
        os.makedirs(os.path.join(OUT, "assets", d), exist_ok=True)
    with open(os.path.join(OUT, "assets", "css", "style.css"), "w") as f:
        f.write(minify_css(open(os.path.join(SRC, "css", "style.css")).read()))
    shutil.copy(os.path.join(SRC, "js", "main.js"), os.path.join(OUT, "assets", "js", "main.js"))
    for folder in ("foto", "canva"):
        fd = os.path.join(SRC, "img", folder)
        for fn in sorted(os.listdir(fd)):
            k, ext = os.path.splitext(fn)
            if folder == "foto" and k == "hero-l":
                continue
            im = Image.open(os.path.join(fd, fn))
            dst = os.path.join(OUT, "assets", "img", folder, k)
            if ext == ".png":   # logo, lencana, mitra: tetap PNG transparan
                im.save(dst + ".png", optimize=True)
                SIZES[k] = (im.width, im.height, folder, 0)
                continue
            im = im.convert("RGB")
            big = 1400 if k == "hero-kids" else im.width
            if im.width > big:
                im = im.resize((big, round(im.height * big / im.width)), Image.LANCZOS)
            im.save(dst + ".webp", "WEBP", quality=74, method=6)
            sw = 760 if k == "hero-kids" else (0 if im.width <= 520 else 480)
            if sw:
                im.resize((sw, round(im.height * sw / im.width)), Image.LANCZOS).save(dst + "-s.webp", "WEBP", quality=72, method=6)
            SIZES[k] = (im.width, im.height, folder, sw)
    # gambar OG 1200x630 dari foto sampul Canva
    h = Image.open(os.path.join(SRC, "img", "canva", "hero-kids.jpg")).convert("RGB")
    w = 1200; hh = round(h.height * w / h.width); h = h.resize((w, hh), Image.LANCZOS)
    top = max(0, (hh - 630) // 2); h.crop((0, top, 1200, top + 630)).save(os.path.join(OUT, "assets", "img", "og.jpg"), quality=80, optimize=True)
    # favicon dari lambang asli
    cr = Image.open(os.path.join(SRC, "img", "canva", "crest.png")).convert("RGBA")
    def icon(sz, pad):
        bg = Image.new("RGBA", (sz, sz), (255, 255, 255, 255))
        c = cr.copy(); c.thumbnail((sz - 2 * pad, sz - 2 * pad), Image.LANCZOS)
        bg.paste(c, ((sz - c.width) // 2, (sz - c.height) // 2), c); return bg
    icon(180, 14).convert("RGB").save(os.path.join(OUT, "assets", "img", "apple-touch-icon.png"))
    icon(64, 3).save(os.path.join(OUT, "assets", "img", "favicon.png"))
    icon(48, 2).save(os.path.join(OUT, "favicon.ico"), sizes=[(16, 16), (32, 32), (48, 48)])


def main():
    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    assets()
    urls = ""
    for pg in PAGES:
        for l in LANGS:
            d = os.path.join(OUT, upath(l, pg).strip("/"))
            os.makedirs(d, exist_ok=True)
            with open(os.path.join(d, "index.html"), "w", encoding="utf-8") as f:
                f.write(page(l, pg))
            links = "".join('    <xhtml:link rel="alternate" hreflang="%s" href="%s%s"/>\n' % (x, DOMAIN, upath(x, pg)) for x in LANGS)
            links += '    <xhtml:link rel="alternate" hreflang="x-default" href="%s%s"/>\n' % (DOMAIN, upath("en", pg))
            urls += "  <url>\n    <loc>%s%s</loc>\n%s  </url>\n" % (DOMAIN, upath(l, pg), links)
    with open(os.path.join(OUT, "sitemap.xml"), "w") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
                'xmlns:xhtml="http://www.w3.org/1999/xhtml">\n%s</urlset>\n' % urls)
    with open(os.path.join(OUT, "robots.txt"), "w") as f:
        f.write("User-agent: *\nAllow: /\n\nSitemap: %s/sitemap.xml\n" % DOMAIN)
    with open(os.path.join(OUT, "404.html"), "w", encoding="utf-8") as f:
        f.write('<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">'
                '<meta name="robots" content="noindex"><title>Page not found – Mutiara School Bali</title><link rel="stylesheet" href="/assets/css/style.css"></head>'
                '<body><main class="sec"><div class="wrap narrow"><h1>Page not found</h1><p>Halaman tidak ditemukan.</p>'
                '<p class="btns"><a class="btn btn-wa" href="/">Home</a><a class="btn btn-ghost" href="/id/">Beranda</a></p></div></main></body></html>')
    with open(os.path.join(OUT, ".htaccess"), "w") as f:
        f.write(HTACCESS)
    with open(os.path.join(OUT, "CNAME"), "w") as f:
        f.write("mutiaraschool.com\n")
    open(os.path.join(OUT, ".nojekyll"), "w").close()
    print("Build selesai ->", OUT)


if __name__ == "__main__":
    main()
