"""Génère le site statique bilingue arnauddeturckheim.com : français à la racine, anglais sous /en/.

Contenus : content.py, content/texte.txt (texte de Pierre El Khoury) et content/texte-en.txt (traduction).
Images : img/works (2200 px) et img/thumbs (900 px), exportées depuis Expo/1 - Photos/3 - JPEG.
Usage : python3 build.py
"""
import html
import re
import shutil
import unicodedata
from pathlib import Path

import content as C

HERE = Path(__file__).parent
FR_DIRS = ["photographies", "expositions", "a-propos", "contact"]
CUR = ' aria-current="page"'

# Routes : clé -> (chemin FR, chemin EN)
ROUTES = {
    "home": ("/", "/en/"),
    "photos": ("/photographies/", "/en/photographs/"),
    "expos": ("/expositions/", "/en/exhibitions/"),
    "expo": ("/expositions/ce-qui-demeure/", "/en/exhibitions/ce-qui-demeure/"),
    "about": ("/a-propos/", "/en/about/"),
    "contact": ("/contact/", "/en/contact/"),
    "404": ("/404.html", None),
}

T = {
    "fr": {
        "role": "Photographe", "nav": [("photos", "Photographies"), ("expos", "Expositions"),
                                        ("about", "À propos"), ("contact", "Contact")],
        "switch": "EN", "switch_label": "English version", "rights": "© 2026 · Toutes les images sont protégées", "f_artist": "L’artiste", "f_sales": "Acquisitions et tirages", "f_sales_who": "Pierre El Khoury, commissaire",
        "desc": "Arnaud de Turckheim, photographe. Première exposition personnelle, Ce Qui Demeure, Paris, novembre 2026.",
        "kicker_home": "Photographie", "see_photos": "Voir les photographies", "expo_kicker": "Exposition",
        "discover": "Découvrir l’exposition", "quote": "Être là, regarder, attendre - puis laisser le réel continuer sans soi.",
        "links": [("photos", "Photographies", "Une première sélection, dix-huit images"),
                  ("about", "À propos", "Ingénieur, photographe, geek cowboy"),
                  ("contact", "Contact", "Écrire à l’artiste")],
        "photos_title": "Photographies",
        "photos_lead": "Une première sélection de dix-huit images, exposées dans {expo} et présentées ici dans "
                       "l’ordre de l’accrochage. Les grands formats de l’exposition apparaissent plus grands.",
        "photos_desc": "Photographies d’Arnaud de Turckheim : Japon, États-Unis, Allemagne, Maroc, Sénégal, France.",
        "print": "Tirage", "format": "Format", "edition": "Édition", "exhibition": "Exposition",
        "unframed": "cm, hors cadre", "copies": "{n} exemplaires", "mounted": ", contrecollé sur aluminium",
        "ask": "Se renseigner sur ce tirage", "all": "Toutes",
        "work_desc": "{t}, {p}, {w}. Photographie d’Arnaud de Turckheim.",
        "expos_title": "Expositions", "solo": "Exposition personnelle", "curated": "Commissariat de",
        "by_artist": "Une exposition d’Arnaud de Turckheim",
        "f_dates": "Dates", "f_opening": "Vernissage", "f_venue": "Lieu", "f_curator": "Commissariat",
        "baobab_cap": "<em>La Figure de l’absence</em>, Sine-Saloum, 2019. L’image qui ouvre l’exposition.",
        "works_kicker": "Les œuvres", "works_title": "Dix-huit tirages",
        "works_note": "Tirages jet d’encre pigmentaire sur papier Hahnemühle Photo Rag Baryta, réalisés par Picto "
                      "Bastille. Grands formats 80 × 120 cm, éditions de 3, contrecollés sur aluminium. Petits "
                      "formats 40 × 60 cm, éditions de 5.",
        "essay_kicker": "Texte", "essay_title": "Être là sans s’imposer",
        "essay_by": "Par Pierre El Khoury, commissaire de l’exposition",
        "info": "Informations", "artist": "Artiste", "curator_role": "Commissaire de l’exposition",
        "expo_desc": "Ce Qui Demeure, première exposition personnelle d’Arnaud de Turckheim. {d}, {a}. Commissariat de Pierre El Khoury.",
        "about_title": "À propos",
        "about_lead": "Ingénieur de formation, photographe depuis les années 2000. Une pratique gardée privée "
                      "pendant près de vingt ans, rendue publique en 2026.",
        "statement_kicker": "Démarche", "statement_title": "Ce qui affleure dans l’ordinaire",
        "cv_kicker": "Repères", "cv_title": "Parcours",
        "about_desc": "Arnaud de Turckheim, ingénieur de formation et photographe, né à Paris en 1990. Bio et démarche.",
        "portrait_alt": "Portrait d’Arnaud de Turckheim",
        "contact_title": "Écrire",
        "contact_lead": "Pour une exposition, une publication ou simplement une conversation.",
        "sales_lead": "Pour l’acquisition d’un tirage, écrivez à Pierre El Khoury, commissaire de {expo}.",
        "curator_of": "Acquisitions et tirages", "nf_title": "Rien ici", "nf_text": "Cette page n’existe pas, ou plus.",
        "back_home": "Retour à l’accueil", "translated": "",
    },
    "en": {
        "role": "Photographer", "nav": [("photos", "Photographs"), ("expos", "Exhibitions"),
                                         ("about", "About"), ("contact", "Contact")],
        "switch": "FR", "switch_label": "Version française", "rights": "© 2026 · All images are protected", "f_artist": "The artist", "f_sales": "Sales and prints", "f_sales_who": "Pierre El Khoury, curator",
        "desc": "Arnaud de Turckheim, photographer. First solo exhibition, Ce Qui Demeure, Paris, November 2026.",
        "kicker_home": "Photography", "see_photos": "View the photographs", "expo_kicker": "Exhibition",
        "discover": "Discover the exhibition", "quote": "To be there, to look, to wait - and then let reality go on without oneself.",
        "links": [("photos", "Photographs", "A first selection, eighteen images"),
                  ("about", "About", "Engineer, photographer, geek cowboy"),
                  ("contact", "Contact", "Write to the artist")],
        "photos_title": "Photographs",
        "photos_lead": "A first selection of eighteen images, shown in {expo} and presented here in the order of "
                       "the hang. The exhibition’s large formats appear larger.",
        "photos_desc": "Photographs by Arnaud de Turckheim: Japan, United States, Germany, Morocco, Senegal, France.",
        "print": "Print", "format": "Size", "edition": "Edition", "exhibition": "Exhibition",
        "unframed": "cm, unframed", "copies": "Edition of {n}", "mounted": ", mounted on aluminium",
        "ask": "Enquire about this print", "all": "All",
        "work_desc": "{t}, {p}, {w}. Photograph by Arnaud de Turckheim.",
        "expos_title": "Exhibitions", "solo": "Solo exhibition", "curated": "Curated by",
        "by_artist": "An exhibition by Arnaud de Turckheim",
        "f_dates": "Dates", "f_opening": "Opening", "f_venue": "Venue", "f_curator": "Curator",
        "baobab_cap": "<em>La Figure de l’absence</em>, Sine-Saloum, 2019. The image that opens the exhibition.",
        "works_kicker": "The works", "works_title": "Eighteen prints",
        "works_note": "Archival pigment prints on Hahnemühle Photo Rag Baryta paper, produced by Picto Bastille. "
                      "Large formats 80 × 120 cm, editions of 3, mounted on aluminium. Small formats "
                      "40 × 60 cm, editions of 5.",
        "essay_kicker": "Essay", "essay_title": "To Be There Without Imposing",
        "essay_by": "By Pierre El Khoury, curator of the exhibition",
        "info": "Information", "artist": "Artist", "curator_role": "Curator of the exhibition",
        "expo_desc": "Ce Qui Demeure, Arnaud de Turckheim’s first solo exhibition. {d}, {a}. Curated by Pierre El Khoury.",
        "about_title": "About",
        "about_lead": "An engineer by training, a photographer since the 2000s. A practice kept private for "
                      "nearly twenty years, made public in 2026.",
        "statement_kicker": "Statement", "statement_title": "What Surfaces in the Ordinary",
        "cv_kicker": "Milestones", "cv_title": "Background",
        "about_desc": "Arnaud de Turckheim, engineer by training and photographer, born in Paris in 1990. Biography and statement.",
        "portrait_alt": "Portrait of Arnaud de Turckheim",
        "contact_title": "Get in touch",
        "contact_lead": "For an exhibition, a publication, or simply a conversation.",
        "sales_lead": "To acquire a print, please write to Pierre El Khoury, curator of {expo}.",
        "curator_of": "Sales and prints", "nf_title": "Nothing here", "nf_text": "This page does not exist, or no longer does.",
        "back_home": "Back to the homepage", "translated": "Translated from the French.",
    },
}

DATA = {
    "fr": dict(lead=C.HOME_LEAD, statement=C.STATEMENT, bio=C.BIO, miles=C.MILESTONES, excerpts=C.EXCERPTS,
               paper=C.PAPER, dates=C.EXPO["dates"], opening="Mercredi 4 novembre", credits=C.EXPO["credits"],
               expo_lead=C.EXPO["lead"], intro=C.EXPO["intro"], essay="texte.txt"),
    "en": dict(lead=C.HOME_LEAD_EN, statement=C.STATEMENT_EN, bio=C.BIO_EN, miles=C.MILESTONES_EN,
               excerpts=C.EXCERPTS_EN, paper=C.PAPER_EN, dates=C.EXPO_EN["dates"], opening=C.EXPO_EN["opening"],
               credits=C.EXPO_EN["credits"], expo_lead=C.EXPO_EN["lead"], intro=C.EXPO_EN["intro"],
               essay="texte-en.txt"),
}


def slug(title):
    s = unicodedata.normalize("NFKD", title).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")


def typo(s):
    return s.replace("'", "’")


def esc(s):
    return html.escape(s, quote=True)


def year(when):
    return when.split()[-1]


def when_l(when, L):
    if L == "fr":
        return when
    m, y = when.split()
    return f"{C.MONTHS_EN[m]} {y}"


def country_l(c, L):
    return c if L == "fr" else C.COUNTRIES_EN[c]


def url(key, L):
    return ROUTES[key][0 if L == "fr" else 1]


def work_url(title, L):
    return ("/photographies/" if L == "fr" else "/en/photographs/") + slug(title) + "/"


def img(title, size="thumbs", sizes="100vw", eager=False):
    s = slug(title)
    w, h = (1466, 2200) if title in C.PORTRAIT_WORKS else (2200, 1466)
    load = 'fetchpriority="high"' if eager else 'loading="lazy"'
    return (f'<img src="/img/{size}/{s}.jpg" srcset="/img/thumbs/{s}.jpg 900w, /img/works/{s}.jpg 2200w" '
            f'sizes="{sizes}" width="{w}" height="{h}" {load} decoding="async" alt="{esc(typo(title))}">')


def expo_link(L):
    return f'<a href="{url("expo", L)}"><em>{C.EXPO["title"]}</em></a>'


# ---------------------------------------------------------------- gabarit

def page(L, path, alt, title, body, *, desc="", active="", cls="", og_image="hors-saison"):
    t = T[L]
    full = f"{title} · {C.SITE['name']}" if title else f"{C.SITE['name']} · {t['role']}"
    desc = desc or t["desc"]
    nav = "".join(f'<a href="{url(k, L)}"{CUR if active == k else ""}>{label}</a>' for k, label in t["nav"])
    other = "en" if L == "fr" else "fr"
    switch = f'<a class="lang" href="{alt}" hreflang="{other}" lang="{other}" title="{t["switch_label"]}">{t["switch"]}</a>' if alt else ""
    fr_path, en_path = (path, alt) if L == "fr" else (alt, path)
    alternates = (f'<link rel="alternate" hreflang="fr" href="{C.SITE["url"]}{fr_path}">\n'
                  f'<link rel="alternate" hreflang="en" href="{C.SITE["url"]}{en_path}">\n'
                  f'<link rel="alternate" hreflang="x-default" href="{C.SITE["url"]}{fr_path}">') if alt else ""
    doc = f"""<!doctype html>
<html lang="{L}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(full)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{C.SITE['url']}{path}">
{alternates}
<meta property="og:title" content="{esc(full)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:image" content="{C.SITE['url']}/img/works/{og_image}.jpg">
<meta property="og:locale" content="{'fr_FR' if L == 'fr' else 'en_GB'}">
<meta property="og:type" content="website">
<meta name="theme-color" content="#f1efe9">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;1,300;1,400&family=EB+Garamond:ital,wght@0,400;0,500;1,400&display=swap">
<link rel="stylesheet" href="/style.css">
</head>
<body class="{cls}">
<header class="top"><div class="wrap">
  <a class="brand" href="{url('home', L)}">Arnaud de Turckheim</a>
  <div class="right">
    <nav>{nav}</nav>
    {switch}
    <button class="burger" aria-label="Menu" aria-expanded="false"><span></span><span></span></button>
  </div>
</div></header>
<main>
{body}
</main>
<footer class="foot"><div class="wrap">
  <a class="brand" href="{url('home', L)}">Arnaud de Turckheim</a>
  <div class="foot-col"><span class="k">{t['f_artist']}</span><a href="mailto:{C.SITE['email']}">{C.SITE['email']}</a></div>
  <div class="foot-col"><span class="k">{t['f_sales']}</span><span>{t['f_sales_who']}</span><a href="mailto:{C.EXPO['curator_email']}">{C.EXPO['curator_email']}</a></div>
  <span class="rights">{t['rights']}</span>
</div></footer>
<script>
const b=document.querySelector('.burger');b.addEventListener('click',()=>{{const o=document.body.classList.toggle('menu');b.setAttribute('aria-expanded',o)}});
document.addEventListener('keydown',e=>{{const p=document.querySelector('[data-prev]'),n=document.querySelector('[data-next]'),c=document.querySelector('[data-close]');if(e.key==='ArrowLeft'&&p)location=p.href;if(e.key==='ArrowRight'&&n)location=n.href;if(e.key==='Escape'&&c)location=c.href}});
</script>
</body>
</html>
"""
    out = HERE / ("404.html" if path == "/404.html" else path.strip("/") + "/index.html" if path != "/" else "index.html")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(doc, encoding="utf-8")


def alt_of(key, L):
    return ROUTES[key][1 if L == "fr" else 0]


# ---------------------------------------------------------------- pages

def home(L):
    t, d = T[L], DATA[L]
    w = {x[0]: x for x in C.WORKS}
    baobab, porters = w["La Figure de l'absence"], w["Les porteurs de lumière"]
    links = "".join(f'<a href="{url(k, L)}"><span class="kicker">{a}</span><span class="big">{b}</span></a>'
                    for k, a, b in t["links"])
    body = f"""
<section class="home-hero">
  <div class="home-intro">
    <h1>Arnaud<br>de Turckheim</h1>
    <p class="lead">{d['lead']}</p>
    <p class="links"><a class="arrow" href="{url('photos', L)}">{t['see_photos']}</a></p>
  </div>
  <a class="home-baobab" href="{work_url(baobab[0], L)}">
    {img(baobab[0], "works", "(min-width: 900px) 46vw, 100vw", eager=True)}
    <span class="cap"><em>{typo(baobab[0])}</em>, {baobab[1]}, {year(baobab[3])}</span>
  </a>
</section>

<section class="home-expo"><div class="wrap">
  <a class="expo-card" href="{url('expo', L)}">
    {img("Hors saison", "works", "(min-width: 900px) 64vw, 100vw")}
    <div class="expo-text">
      <p class="kicker">{t['expo_kicker']} · {C.EXPO['year']}</p>
      <h2>{C.EXPO['title']}</h2>
      <p class="meta">{d['dates']}<br>{C.EXPO['address']}</p>
      <p>{d['expo_lead']}</p>
      <span class="arrow">{t['discover']}</span>
    </div>
  </a>
</div></section>

<section class="home-statement"><div class="wrap narrow">
  <blockquote>{t['quote']}</blockquote>
  <p class="attr">Pierre El Khoury, <em>Ce Qui Demeure</em></p>
</div></section>

<section class="home-last"><div class="wrap">
  <a class="wide" href="{work_url(porters[0], L)}">
    {img(porters[0], "works", "100vw")}
    <span class="cap"><em>{typo(porters[0])}</em>, {porters[1]}, {year(porters[3])}</span>
  </a>
  <div class="home-links">{links}</div>
</div></section>
"""
    page(L, url("home", L), alt_of("home", L), "", body, cls="is-home", og_image=slug(baobab[0]))


# Grille « à l'échelle » : chaque image est dimensionnée selon son format de tirage, pas selon son
# orientation. Petit 60 x 40 = 60 unités de large (portrait 40), grand 120 x 80 réduit à 90 (portrait 60),
# soit 1,5 fois plus grand en linéaire. Rangées composées à la main dans l'ordre de l'accrochage,
# 210 unités maximum, alignées en bas.
ROWS = [
    ["Les porteurs de lumière", "L'attente de l'eau", "Le Témoin"],
    ["L'apparition", "La Gardienne", "Le temps suspendu"],
    ["L'ascension", "La charpente du monde", "L'autre côté"],
    ["Les revenantes", "Le détour", "Quiétude"],
    ["La traversée", "Habiter l'absence", "Le songe éveillé"],
    ["L'attente", "La Figure de l'absence", "Hors saison"],
]
assert sorted(sum(ROWS, [])) == sorted(w[0] for w in C.WORKS)


def units(title):
    ed = {w[0]: w[5] for w in C.WORKS}[title]
    port = title in C.PORTRAIT_WORKS
    return (60 if port else 90) if ed == 3 else (40 if port else 60)


def scaled_grid(L, compact=False):
    w = {x[0]: x for x in C.WORKS}
    rows = []
    for row in ROWS:
        tiles = "".join(f"""
      <a class="tile{' big' if w[x][5] == 3 else ''}" style="--u:{units(x)}" href="{work_url(x, L)}">
        {img(x, "works" if w[x][5] == 3 and not compact else "thumbs", f"(min-width: 820px) {round(units(x) * 0.42)}vw, {min(100, round(units(x) / 90 * 100))}vw")}
        <span class="t"><em>{typo(x)}</em></span>
        <span class="m">{w[x][1]}, {year(w[x][3])}</span>
      </a>""" for x in row)
        rows.append(f'<div class="row">{tiles}\n    </div>')
    return f'<div class="scaled{" compact" if compact else ""}">' + "".join(rows) + "</div>"


def photographies(L):
    t = T[L]
    body = f"""
<section class="page-head"><div class="wrap">
  <h1>{t['photos_title']}</h1>
  <p class="lead">{t['photos_lead'].format(expo=expo_link(L))}</p>
</div></section>
<section class="grid-wrap"><div class="wrap">{scaled_grid(L)}</div></section>
"""
    page(L, url("photos", L), alt_of("photos", L), t["photos_title"], body, active="photos", desc=t["photos_desc"])


def work_pages(L):
    t, d = T[L], DATA[L]
    n = len(C.WORKS)
    for i, (title, place, country, when, fmt, ed) in enumerate(C.WORKS):
        prev, nxt = C.WORKS[(i - 1) % n], C.WORKS[(i + 1) % n]
        support = d["paper"] + (t["mounted"] if ed == 3 else "")
        quote = ""
        if title in d["excerpts"]:
            quote = f'<blockquote class="excerpt">{d["excerpts"][title]}<cite>Pierre El Khoury</cite></blockquote>'
        kind = "port" if title in C.PORTRAIT_WORKS else "land"
        w = when_l(when, L)
        body = f"""
<article class="work-page {kind}">
  <figure class="work-img"><a href="/img/works/{slug(title)}.jpg" class="zoom">{img(title, "works", "(min-width: 1000px) 70vw, 100vw", eager=True)}</a></figure>
  <aside class="work-info">
    <p class="kicker">{i + 1:02d} / {n}</p>
    <h1>{typo(title)}</h1>
    <p class="place">{place}, {country_l(country, L)}<br>{w[0].upper() + w[1:]}</p>
    {quote}
    <dl>
      <div><dt>{t['print']}</dt><dd>{support}</dd></div>
      <div><dt>{t['format']}</dt><dd>{fmt} {t['unframed']}</dd></div>
      <div><dt>{t['edition']}</dt><dd>{t['copies'].format(n=ed)}</dd></div>
      <div><dt>{t['exhibition']}</dt><dd>{expo_link(L)}, Paris, {C.EXPO['year']}</dd></div>
    </dl>
    <p class="ask"><a class="arrow" href="mailto:{C.EXPO['curator_email']}?cc={C.SITE['email']}&amp;subject={esc(typo(title))}">{t['ask']}</a></p>
    <nav class="pager">
      <a data-prev href="{work_url(prev[0], L)}">← <em>{typo(prev[0])}</em></a>
      <a data-close href="{url('photos', L)}">{t['all']}</a>
      <a data-next href="{work_url(nxt[0], L)}"><em>{typo(nxt[0])}</em> →</a>
    </nav>
  </aside>
</article>
"""
        page(L, work_url(title, L), work_url(title, "en" if L == "fr" else "fr"), typo(title), body,
             active="photos", cls="is-work", desc=t["work_desc"].format(t=typo(title), p=place, w=w),
             og_image=slug(title))


TEXT_TITLES = ["La Figure de l’absence", "Ce Qui Demeure", "Les Revenantes", "Les Porteurs de lumière",
               "La Traversée", "Le Détour", "Hors saison", "L’Apparition", "La Gardienne",
               "Le Songe éveillé", "The Americans"]
SUP = {"¹": "1", "²": "2", "³": "3", "⁴": "4"}


def essay(L):
    body, notes = (HERE / "content" / DATA[L]["essay"]).read_text().split("---NOTES---")

    def rich(x):
        x = html.escape(x, quote=False)
        for title in TEXT_TITLES:
            x = x.replace(title, f"<em>{title}</em>")
        return x

    paras = []
    for b in body.strip().split("\n\n"):
        x = rich(" ".join(b.split()))
        for k, v in SUP.items():
            x = x.replace(k, f'<sup><a href="#note-{v}" id="ref-{v}">{v}</a></sup>')
        paras.append(f"<p>{x}</p>")
    items = [f'<li id="note-{SUP[n.strip()[0]]}"><a href="#ref-{SUP[n.strip()[0]]}">{SUP[n.strip()[0]]}</a> '
             f'{rich(n.strip()[1:].strip())}</li>' for n in notes.strip().split("\n\n") if n.strip()]
    return "".join(paras), "".join(items)


def expositions(L):
    t, d = T[L], DATA[L]
    body = f"""
<section class="page-head"><div class="wrap">
  <p class="kicker">{t['expos_title']}</p>
  <h1>{t['expos_title']}</h1>
</div></section>
<section><div class="wrap">
  <a class="expo-row" href="{url('expo', L)}">
    <span class="y">{C.EXPO['year']}</span>
    <span class="t"><em>{C.EXPO['title']}</em></span>
    <span class="m">{t['solo']} · {C.EXPO['address']}<br>{t['curated']} {C.EXPO['curator']}</span>
    {img("Hors saison", "thumbs", "240px")}
  </a>
</div></section>
"""
    page(L, url("expos", L), alt_of("expos", L), t["expos_title"], body, active="expos")

    paras, notes = essay(L)
    intro = "".join(f"<p>{p}</p>" for p in d["intro"])
    credits = " · ".join(d["credits"])
    translated = f'<p class="translated">{t["translated"]}</p>' if t["translated"] else ""
    body = f"""
<section class="expo-hero">
  {img("Hors saison", "works", "100vw", eager=True)}
</section>
<section class="expo-band"><div class="wrap">
  <div><p class="kicker">{t['solo']} · {C.EXPO['year']}</p><h1>{C.EXPO['title']}</h1>
    <p class="sub">{t['by_artist']}</p></div>
  <dl class="facts">
    <div><dt>{t['f_dates']}</dt><dd>{d['dates']}</dd></div>
    <div><dt>{t['f_opening']}</dt><dd>{d['opening']}</dd></div>
    <div><dt>{t['f_venue']}</dt><dd>{C.EXPO['address']}</dd></div>
    <div><dt>{t['f_curator']}</dt><dd>{C.EXPO['curator']}</dd></div>
  </dl>
</div></section>

<section class="expo-intro"><div class="wrap two">
  <p class="lead">{d['expo_lead']}</p>
  <div class="prose">{intro}</div>
</div></section>

<section class="expo-baobab"><div class="wrap">
  <figure>{img("La Figure de l'absence", "works", "(min-width: 900px) 40vw, 90vw")}
    <figcaption>{t['baobab_cap']}</figcaption></figure>
</div></section>

<section class="expo-works"><div class="wrap">
  <p class="kicker">{t['works_kicker']}</p><h2>{t['works_title']}</h2>
  <p class="note">{t['works_note']}</p>
  {scaled_grid(L, compact=True)}
  <p class="credits">{credits}</p>
</div></section>

<section class="essay" id="texte"><div class="wrap">
  <div class="essay-head"><p class="kicker">{t['essay_kicker']}</p><h2>{t['essay_title']}</h2>
    <p class="by">{t['essay_by']}</p>{translated}</div>
  <div class="essay-body">{paras}<p class="sig">Pierre El Khoury</p></div>
  <ol class="notes">{notes}</ol>
</div></section>

"""
    page(L, url("expo", L), alt_of("expo", L), C.EXPO["title"], body, active="expos", cls="is-expo",
         desc=t["expo_desc"].format(d=d["dates"], a=C.EXPO["address"]))


def about(L):
    t, d = T[L], DATA[L]
    bio = "".join(f"<p>{p}</p>" for p in d["bio"])
    statement = "".join(f"<p>{p}</p>" for p in d["statement"])
    miles = "".join(f"<div><dt>{a}</dt><dd>{b}</dd></div>" for a, b in d["miles"])
    strip = "".join(f'<a href="{work_url(x, L)}">{img(x, "thumbs", "33vw")}</a>'
                    for x in ["Les revenantes", "Le songe éveillé", "La charpente du monde"])
    body = f"""
<section class="about-head"><div class="wrap about-grid">
  <figure class="portrait"><img src="/img/portrait.jpg" width="900" height="900" alt="{t['portrait_alt']}" fetchpriority="high"></figure>
  <div>
    <p class="kicker">{t['about_title']}</p>
    <h1>Arnaud de Turckheim</h1>
    <p class="lead">{t['about_lead']}</p>
    <div class="prose">{bio}</div>
  </div>
</div></section>

<section class="statement"><div class="wrap two">
  <div><p class="kicker">{t['statement_kicker']}</p><h2>{t['statement_title']}</h2></div>
  <div class="prose">{statement}</div>
</div></section>

<section class="strip"><div class="wrap strip-row">{strip}</div></section>

<section class="cv"><div class="wrap two">
  <div><p class="kicker">{t['cv_kicker']}</p><h2>{t['cv_title']}</h2></div>
  <dl class="facts">{miles}</dl>
</div></section>
"""
    page(L, url("about", L), alt_of("about", L), t["about_title"], body, active="about", desc=t["about_desc"])


def contact(L):
    t = T[L]
    body = f"""
<section class="contact-page"><div class="wrap contact-grid">
  <div>
    <p class="kicker">Contact</p>
    <h1>{t['contact_title']}</h1>
    <p class="lead">{t['contact_lead']}</p>
    <p class="mail"><a href="mailto:{C.SITE['email']}">{C.SITE['email']}</a></p>
    <div class="curator">
      <p class="kicker">{t['curator_of']}</p>
      <p class="sales">{t['sales_lead'].format(expo=expo_link(L))}</p>
      <p class="who">Pierre El Khoury</p>
      <a href="mailto:{C.EXPO['curator_email']}">{C.EXPO['curator_email']}</a>
    </div>
  </div>
  <a class="contact-img" href="{work_url("L'attente", L)}">{img("L'attente", "works", "(min-width: 900px) 40vw, 100vw")}</a>
</div></section>
"""
    page(L, url("contact", L), alt_of("contact", L), "Contact", body, active="contact")


def not_found():
    fr, en = T["fr"], T["en"]
    body = f"""<section class="page-head"><div class="wrap">
  <p class="kicker">404</p><h1>{fr['nf_title']}</h1>
  <p class="lead">{fr['nf_text']} <a href="/">{fr['back_home']}</a>.</p>
  <p class="lead" lang="en">{en['nf_text']} <a href="/en/">{en['back_home']}</a>.</p>
</div></section>"""
    page("fr", "/404.html", None, "Page introuvable", body)


def main():
    for d in FR_DIRS + ["en"]:
        shutil.rmtree(HERE / d, ignore_errors=True)
    for L in ("fr", "en"):
        home(L); photographies(L); work_pages(L); expositions(L); about(L); contact(L)
    not_found()
    print("ok :", len(list(HERE.rglob("index.html"))) + 1, "pages")


if __name__ == "__main__":
    main()
