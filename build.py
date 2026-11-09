"""Génère le site statique arnauddeturckheim.com (pages en dossiers, URLs propres).

Contenus : content.py et content/texte.txt (texte de Pierre El Khoury).
Images : img/works (2200 px) et img/thumbs (900 px), exportées depuis Expo/1 - Photos/3 - JPEG.
Usage : python3 build.py
"""
import html
import re
import shutil
import unicodedata
from pathlib import Path

from content import (BIO, EXCERPTS, EXPO, HOME_LEAD, MILESTONES, NB, PAPER, PORTRAIT_WORKS, SITE,
                     STATEMENT, WORKS)

HERE = Path(__file__).parent
OUT_DIRS = ["photographies", "expositions", "a-propos", "contact"]


def slug(title):
    s = unicodedata.normalize("NFKD", title).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")


def typo(s):
    return s.replace("'", "’")


def esc(s):
    return html.escape(s, quote=True)


def dims(title):
    return (1466, 2200) if title in PORTRAIT_WORKS else (2200, 1466)


def year(when):
    return when.split()[-1]


def img(title, size="thumbs", sizes="100vw", cls="", eager=False):
    s = slug(title)
    w, h = dims(title)
    load = 'fetchpriority="high"' if eager else 'loading="lazy"'
    return (f'<img class="{cls}" src="/img/{size}/{s}.jpg" '
            f'srcset="/img/thumbs/{s}.jpg 900w, /img/works/{s}.jpg 2200w" sizes="{sizes}" '
            f'width="{w}" height="{h}" {load} decoding="async" alt="{esc(typo(title))}">')


# ---------------------------------------------------------------- gabarit

CUR = ' aria-current="page"'



def page(path, title, body, *, desc="", active="", cls="", og_image="hors-saison"):
    full = f"{title} · {SITE['name']}" if title else f"{SITE['name']} · Photographe"
    desc = desc or "Arnaud de Turckheim, photographe. Première exposition personnelle, Ce Qui Demeure, Paris, novembre 2026."
    nav = "".join(
        f'<a href="/{p}/"{CUR if active == p else ""}>{label}</a>'
        for p, label in [("photographies", "Photographies"), ("expositions", "Expositions"),
                         ("a-propos", "À propos"), ("contact", "Contact")])
    doc = f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(full)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{SITE['url']}{path}">
<meta property="og:title" content="{esc(full)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:image" content="{SITE['url']}/img/works/{og_image}.jpg">
<meta property="og:type" content="website">
<meta name="theme-color" content="#f1efe9">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;1,300;1,400&family=EB+Garamond:ital,wght@0,400;0,500;1,400&display=swap">
<link rel="stylesheet" href="/style.css">
</head>
<body class="{cls}">
<header class="top"><div class="wrap">
  <a class="brand" href="/">Arnaud de Turckheim</a>
  <button class="burger" aria-label="Menu" aria-expanded="false"><span></span><span></span></button>
  <nav>{nav}</nav>
</div></header>
<main>
{body}
</main>
<footer class="foot"><div class="wrap">
  <a class="brand" href="/">Arnaud de Turckheim</a>
  <span><a href="mailto:{SITE['email']}">{SITE['email']}</a></span>
  <span>© 2026 · Toutes les images sont protégées</span>
</div></footer>
<script>
const b=document.querySelector('.burger');b.addEventListener('click',()=>{{const o=document.body.classList.toggle('menu');b.setAttribute('aria-expanded',o)}});
document.addEventListener('keydown',e=>{{const p=document.querySelector('[data-prev]'),n=document.querySelector('[data-next]');if(e.key==='ArrowLeft'&&p)location=p.href;if(e.key==='ArrowRight'&&n)location=n.href;if(e.key==='Escape'&&document.querySelector('[data-close]'))location=document.querySelector('[data-close]').href}});
</script>
</body>
</html>
"""
    out = HERE / path.strip("/") / "index.html" if path != "/404.html" else HERE / "404.html"
    if path == "/":
        out = HERE / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(doc, encoding="utf-8")


# ---------------------------------------------------------------- pages

def home():
    w = {t[0]: t for t in WORKS}
    baobab, pool, porters = w["La Figure de l'absence"], w["Hors saison"], w["Les porteurs de lumière"]
    body = f"""
<section class="home-hero">
  <div class="home-intro">
    <p class="kicker">Photographie</p>
    <h1>Arnaud<br>de Turckheim</h1>
    <p class="lead">{HOME_LEAD}</p>
    <p class="links"><a class="arrow" href="/photographies/">Voir les photographies</a></p>
  </div>
  <a class="home-baobab" href="/photographies/{slug(baobab[0])}/">
    {img(baobab[0], "works", "(min-width: 900px) 46vw, 100vw", eager=True)}
    <span class="cap"><em>{typo(baobab[0])}</em>, {baobab[1]}, {year(baobab[3])}</span>
  </a>
</section>

<section class="home-expo"><div class="wrap">
  <a class="expo-card" href="/expositions/{EXPO['slug']}/">
    {img(pool[0], "works", "(min-width: 900px) 64vw, 100vw")}
    <div class="expo-text">
      <p class="kicker">Exposition · {EXPO['year']}</p>
      <h2>{EXPO['title']}</h2>
      <p class="meta">{EXPO['dates']}<br>{EXPO['address']}</p>
      <p>{EXPO['lead']}</p>
      <span class="arrow">Découvrir l’exposition</span>
    </div>
  </a>
</div></section>

<section class="home-statement"><div class="wrap narrow">
  <blockquote>Être là, regarder, attendre - puis laisser le réel continuer sans soi.</blockquote>
  <p class="attr">Pierre El Khoury, <em>Ce Qui Demeure</em></p>
</div></section>

<section class="home-last"><div class="wrap">
  <a class="wide" href="/photographies/{slug(porters[0])}/">
    {img(porters[0], "works", "100vw")}
    <span class="cap"><em>{typo(porters[0])}</em>, {porters[1]}, {year(porters[3])}</span>
  </a>
  <div class="home-links">
    <a href="/photographies/"><span class="kicker">Photographies</span><span class="big">Dix-huit images, 2017 - 2019</span></a>
    <a href="/a-propos/"><span class="kicker">À propos</span><span class="big">Ingénieur, photographe, geek cowboy</span></a>
    <a href="/contact/"><span class="kicker">Contact</span><span class="big">Écrire à l’artiste</span></a>
  </div>
</div></section>
"""
    page("/", "", body, cls="is-home", og_image=slug(baobab[0]))


def photographies():
    items = "".join(f"""
    <a class="tile" href="/photographies/{slug(t[0])}/">
      {img(t[0], "thumbs", "(min-width: 1100px) 30vw, (min-width: 640px) 45vw, 100vw")}
      <span class="t"><em>{typo(t[0])}</em></span>
      <span class="m">{t[1]}, {year(t[3])}</span>
    </a>""" for t in WORKS)
    body = f"""
<section class="page-head"><div class="wrap">
  <p class="kicker">Photographies</p>
  <h1>2017 - 2019</h1>
  <p class="lead">Japon, États-Unis, Allemagne, Maroc, Sénégal, France. Dix-huit images exposées pour la
  première fois dans <a href="/expositions/{EXPO['slug']}/"><em>{EXPO['title']}</em></a>, présentées ici dans
  l’ordre de l’accrochage.</p>
</div></section>
<section class="grid-wrap"><div class="wrap"><div class="masonry">{items}
</div></div></section>
"""
    page("/photographies/", "Photographies", body, active="photographies",
         desc="Dix-huit photographies d’Arnaud de Turckheim, 2017 - 2019 : Japon, États-Unis, Allemagne, Maroc, Sénégal, France.")


def work_pages():
    n = len(WORKS)
    for i, (title, place, country, when, fmt, ed) in enumerate(WORKS):
        prev, nxt = WORKS[(i - 1) % n], WORKS[(i + 1) % n]
        support = PAPER + (", contrecollé sur aluminium" if ed == 3 else "")
        quote = ""
        if title in EXCERPTS:
            quote = f"""<blockquote class="excerpt">{EXCERPTS[title]}<cite>Pierre El Khoury</cite></blockquote>"""
        kind = "port" if title in PORTRAIT_WORKS else "land"
        body = f"""
<article class="work-page {kind}">
  <figure class="work-img"><a href="/img/works/{slug(title)}.jpg" class="zoom">{img(title, "works", "(min-width: 1000px) 70vw, 100vw", eager=True)}</a></figure>
  <aside class="work-info">
    <p class="kicker">{i + 1:02d} / {n}</p>
    <h1>{typo(title)}</h1>
    <p class="place">{place}, {country}<br>{when.capitalize()}</p>
    {quote}
    <dl>
      <div><dt>Tirage</dt><dd>{support}</dd></div>
      <div><dt>Format</dt><dd>{fmt} cm, hors cadre</dd></div>
      <div><dt>Édition</dt><dd>{ed} exemplaires</dd></div>
      <div><dt>Exposition</dt><dd><a href="/expositions/{EXPO['slug']}/"><em>{EXPO['title']}</em></a>, Paris, {EXPO['year']}</dd></div>
    </dl>
    <p class="ask"><a class="arrow" href="mailto:{SITE['email']}?subject={esc(typo(title))}">Se renseigner sur ce tirage</a></p>
    <nav class="pager">
      <a data-prev href="/photographies/{slug(prev[0])}/">← <em>{typo(prev[0])}</em></a>
      <a data-close href="/photographies/">Toutes</a>
      <a data-next href="/photographies/{slug(nxt[0])}/"><em>{typo(nxt[0])}</em> →</a>
    </nav>
  </aside>
</article>
"""
        page(f"/photographies/{slug(title)}/", typo(title), body, active="photographies", cls="is-work",
             desc=f"{typo(title)}, {place}, {when}. Photographie d’Arnaud de Turckheim.", og_image=slug(title))


TEXT_TITLES = ["La Figure de l’absence", "Ce Qui Demeure", "Les Revenantes", "Les Porteurs de lumière",
               "La Traversée", "Le Détour", "Hors saison", "L’Apparition", "La Gardienne",
               "Le Songe éveillé", "The Americans"]
SUP = {"¹": "1", "²": "2", "³": "3", "⁴": "4"}


def essay():
    body, notes = (HERE / "content" / "texte.txt").read_text().split("---NOTES---")

    def rich(t):
        t = html.escape(t, quote=False)
        for title in TEXT_TITLES:
            t = t.replace(title, f"<em>{title}</em>")
        return t

    paras = []
    for b in body.strip().split("\n\n"):
        t = rich(" ".join(b.split()))
        for k, v in SUP.items():
            t = t.replace(k, f'<sup><a href="#note-{v}" id="ref-{v}">{v}</a></sup>')
        paras.append(f"<p>{t}</p>")
    items = []
    for n in notes.strip().split("\n\n"):
        n = n.strip()
        v = SUP[n[0]]
        items.append(f'<li id="note-{v}"><a href="#ref-{v}">{v}</a> {rich(n[1:].strip())}</li>')
    return "".join(paras), "".join(items)


def expositions():
    body = f"""
<section class="page-head"><div class="wrap">
  <p class="kicker">Expositions</p>
  <h1>Expositions</h1>
</div></section>
<section><div class="wrap">
  <a class="expo-row" href="/expositions/{EXPO['slug']}/">
    <span class="y">{EXPO['year']}</span>
    <span class="t"><em>{EXPO['title']}</em></span>
    <span class="m">Exposition personnelle · {EXPO['address']}<br>Commissariat de {EXPO['curator']}</span>
    {img("Hors saison", "thumbs", "240px")}
  </a>
</div></section>
"""
    page("/expositions/", "Expositions", body, active="expositions")

    paras, notes = essay()
    intro = "".join(f"<p>{p}</p>" for p in EXPO["intro"])
    works = "".join(f"""
      <a class="tile" href="/photographies/{slug(t[0])}/">
        {img(t[0], "thumbs", "(min-width: 900px) 22vw, 45vw")}
        <span class="t"><em>{typo(t[0])}</em></span><span class="m">{t[1]}, {year(t[3])}</span>
      </a>""" for t in WORKS)
    credits = " · ".join(EXPO["credits"])
    body = f"""
<section class="expo-hero">
  {img("Hors saison", "works", "100vw", eager=True)}
</section>
<section class="expo-band"><div class="wrap">
  <div><p class="kicker">Exposition personnelle · {EXPO['year']}</p><h1>{EXPO['title']}</h1>
    <p class="sub">Une exposition d’Arnaud de Turckheim</p></div>
  <dl class="facts">
    <div><dt>Dates</dt><dd>{EXPO['dates']}</dd></div>
    <div><dt>Vernissage</dt><dd>Mercredi 4 novembre</dd></div>
    <div><dt>Lieu</dt><dd>{EXPO['address']}</dd></div>
    <div><dt>Commissariat</dt><dd>{EXPO['curator']}</dd></div>
  </dl>
</div></section>

<section class="expo-intro"><div class="wrap two">
  <p class="lead">{EXPO['lead']}</p>
  <div class="prose">{intro}</div>
</div></section>

<section class="expo-baobab"><div class="wrap">
  <figure>{img("La Figure de l'absence", "works", "(min-width: 900px) 40vw, 90vw")}
    <figcaption><em>La Figure de l’absence</em>, Sine-Saloum, 2019. L’image qui ouvre l’exposition.</figcaption></figure>
</div></section>

<section class="expo-works"><div class="wrap">
  <p class="kicker">Les œuvres</p><h2>Dix-huit tirages</h2>
  <p class="note">Tirages jet d’encre pigmentaire sur papier Hahnemühle Photo Rag Baryta, réalisés par Picto Bastille.
  Grands formats 80 × 120 cm, éditions de 3, contrecollés sur aluminium. Petits formats 40 × 60 cm, éditions de 5.</p>
  <div class="mini-grid">{works}
  </div>
</div></section>

<section class="essay" id="texte"><div class="wrap">
  <div class="essay-head"><p class="kicker">Texte</p><h2>Être là sans s’imposer</h2>
    <p class="by">Par Pierre El Khoury, commissaire de l’exposition</p></div>
  <div class="essay-body">{paras}<p class="sig">Pierre El Khoury</p></div>
  <ol class="notes">{notes}</ol>
</div></section>

<section class="expo-contact"><div class="wrap two">
  <div><p class="kicker">Informations</p><h2>Contact</h2></div>
  <div class="contact-list">
    <div><p class="who">Arnaud de Turckheim</p><p class="role">Artiste</p><a href="mailto:{SITE['email']}">{SITE['email']}</a></div>
    <div><p class="who">Pierre El Khoury</p><p class="role">Commissaire de l’exposition</p><a href="mailto:{EXPO['curator_email']}">{EXPO['curator_email']}</a></div>
    <p class="credits">{credits}</p>
  </div>
</div></section>
"""
    page(f"/expositions/{EXPO['slug']}/", EXPO["title"], body, active="expositions", cls="is-expo",
         desc=f"Ce Qui Demeure, première exposition personnelle d’Arnaud de Turckheim. {EXPO['dates']}, {EXPO['address']}. Commissariat de Pierre El Khoury.")


def about():
    bio = "".join(f"<p>{p}</p>" for p in BIO)
    statement = "".join(f"<p>{p}</p>" for p in STATEMENT)
    miles = "".join(f"<div><dt>{a}</dt><dd>{b}</dd></div>" for a, b in MILESTONES)
    body = f"""
<section class="about-head"><div class="wrap about-grid">
  <figure class="portrait"><img src="/img/portrait.jpg" width="900" height="900" alt="Portrait d’Arnaud de Turckheim" fetchpriority="high"></figure>
  <div>
    <p class="kicker">À propos</p>
    <h1>Arnaud de Turckheim</h1>
    <p class="lead">Ingénieur de formation, photographe depuis les années 2000. Une pratique gardée privée
    pendant près de vingt ans, rendue publique en 2026.</p>
    <div class="prose">{bio}</div>
  </div>
</div></section>

<section class="statement"><div class="wrap two">
  <div><p class="kicker">Démarche</p><h2>Ce qui affleure dans l’ordinaire</h2></div>
  <div class="prose">{statement}</div>
</div></section>

<section class="strip"><div class="wrap strip-row">
  {"".join(f'<a href="/photographies/{slug(t)}/">{img(t, "thumbs", "33vw")}</a>' for t in ["Les revenantes", "Le songe éveillé", "La charpente du monde"])}
</div></section>

<section class="cv"><div class="wrap two">
  <div><p class="kicker">Repères</p><h2>Parcours</h2></div>
  <dl class="facts">{miles}</dl>
</div></section>
"""
    page("/a-propos/", "À propos", body, active="a-propos",
         desc="Arnaud de Turckheim, ingénieur de formation et photographe, né à Paris en 1990. Bio et démarche.")


def contact():
    body = f"""
<section class="contact-page"><div class="wrap contact-grid">
  <div>
    <p class="kicker">Contact</p>
    <h1>Écrire</h1>
    <p class="lead">Pour un tirage, une exposition, une publication ou simplement une conversation.</p>
    <p class="mail"><a href="mailto:{SITE['email']}">{SITE['email']}</a></p>
    <div class="curator">
      <p class="kicker">Commissariat de <em>{EXPO['title']}</em></p>
      <p class="who">Pierre El Khoury</p>
      <a href="mailto:{EXPO['curator_email']}">{EXPO['curator_email']}</a>
    </div>
  </div>
  <a class="contact-img" href="/photographies/l-attente/">{img("L'attente", "works", "(min-width: 900px) 40vw, 100vw")}</a>
</div></section>
"""
    page("/contact/", "Contact", body, active="contact")


def not_found():
    body = f"""<section class="page-head"><div class="wrap">
  <p class="kicker">404</p><h1>Rien ici</h1>
  <p class="lead">Cette page n’existe pas, ou plus. <a href="/">Retour à l’accueil</a>.</p>
</div></section>"""
    page("/404.html", "Page introuvable", body)


def main():
    for d in OUT_DIRS:
        shutil.rmtree(HERE / d, ignore_errors=True)
    home(); photographies(); work_pages(); expositions(); about(); contact(); not_found()
    print("ok :", len(list(HERE.rglob("index.html"))) + 1, "pages")


if __name__ == "__main__":
    main()
