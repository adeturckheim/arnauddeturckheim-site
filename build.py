"""Site arnauddeturckheim.com : page unique autour de l'exposition « Ce Qui Demeure ».

Contenu repris du preview (Drive : Expo/9 - Preview/build.py), sans les prix.
Le texte de Pierre El Khoury vient de content/texte.txt (copie de Expo/8 - Texte exposition/texte.txt).
Usage : python3 build.py  -> écrit index.html
"""
import html
import re
import unicodedata
from pathlib import Path

HERE = Path(__file__).parent
DATES = "Du 4 au 19 novembre 2026"
ADDRESS = "10 rue Lincoln, 75008 Paris"
PAPER = "Tirage pigmentaire sur papier Hahnemühle Photo Rag Baryta"
EMAIL_ARNAUD = "adeturckheim@gmail.com"
EMAIL_PIERRE = "pek.elkhoury@gmail.com"

# (titre, lieu, date de prise de vue, format H x L, édition) - ordre de la feuille de salle
WORKS = [
    ("Les porteurs de lumière", "Shimoda", "juillet 2017", "80 × 120", 3),
    ("L'attente de l'eau", "Ise", "juillet 2017", "40 × 60", 5),
    ("Le Témoin", "Berlin", "octobre 2017", "40 × 60", 5),
    ("L'apparition", "Provence", "janvier 2018", "40 × 60", 5),
    ("La Gardienne", "Paris", "janvier 2018", "80 × 120", 3),
    ("Le temps suspendu", "Iidabashi", "juin 2017", "40 × 60", 5),
    ("L'ascension", "Los Angeles", "avril 2017", "40 × 60", 5),
    ("La charpente du monde", "San Francisco", "avril 2017", "40 × 60", 5),
    ("L'autre côté", "Hakone", "juillet 2017", "40 × 60", 5),
    ("Les revenantes", "Provence", "décembre 2017", "40 × 60", 5),
    ("Le détour", "Tokyo", "mai 2017", "80 × 120", 3),
    ("Quiétude", "Nakano", "mai 2017", "40 × 60", 5),
    ("La traversée", "Tokyo", "juillet 2017", "40 × 60", 5),
    ("Habiter l'absence", "Marrakech", "octobre 2017", "40 × 60", 5),
    ("Le songe éveillé", "Shimoda", "juillet 2017", "60 × 40", 5),
    ("L'attente", "Hakone", "juillet 2017", "120 × 80", 3),
    ("La Figure de l'absence", "Sine-Saloum", "mai 2019", "120 × 80", 3),
    ("Hors saison", "Los Angeles", "février 2018", "40 × 60", 5),
]
PORTRAIT_WORKS = {"L'attente", "La Figure de l'absence", "Le songe éveillé"}
COVER = "Hors saison"

# Bio du preview ; Arnaud veut le trait d'union, jamais de tiret long
BIO = [
    "Ingénieur de formation, Arnaud de Turckheim photographie depuis les années 2000. Une pratique "
    "d’abord privée, tenue en retrait pendant près de vingt ans, qu’il choisit aujourd’hui de rendre "
    "publique pour la première fois.",
    "Élevé entre Paris et la Provence, dans une famille où l’image est une langue familière - sa mère "
    "est photographe -, il vit en Chine, en Angleterre puis au Japon, avant de rentrer en France en 2017. "
    "De ces années nomades, il garde un goût pour l’observation discrète : il ne cherche pas "
    "l’événement, mais ce qui affleure dans l’ordinaire - un geste, une lumière, une géométrie. "
    "Ses proches le décrivent volontiers comme un « geek cowboy », partagé entre la logique de "
    "l’ingénieur et l’attrait des grands espaces.",
    "Son écriture photographique est reconnaissable : contre-jours tenus, lumières rasantes, contrastes "
    "francs, nuances de gris et de vert. Le portrait rapproché y croise l’abstraction urbaine, "
    "l’ethnographie discrète y répond à une forme de méditation formelle. Les images sont numériques, "
    "honnêtes : il revendique une photographie cadrée par l’œil, sans artifice.",
    "<em>Ce Qui Demeure</em> réunit dix-huit tirages pris au Japon, en Californie, au Maroc, au Sénégal "
    "et en France. L’exposition est assumée comme <strong>pré-IA</strong> : l’image telle "
    "qu’elle se faisait avant la bascule générative, cadrée par un regard et non par un modèle. Une première "
    "monstration, et l’ouverture d’une conversation que l’auteur entend prolonger.",
]

TEXT_TITLES = ["La Figure de l’absence", "Ce Qui Demeure", "Les Revenantes", "Les Porteurs de lumière",
               "La Traversée", "Le Détour", "Hors saison", "L’Apparition", "La Gardienne",
               "Le Songe éveillé", "The Americans"]
SUPERSCRIPTS = {"¹": "1", "²": "2", "³": "3", "⁴": "4"}


def slug(title):
    s = unicodedata.normalize("NFKD", title).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")


def typo(s):
    return s.replace("'", "’")


def rich(t):
    t = html.escape(t, quote=False)
    for title in TEXT_TITLES:
        t = t.replace(title, f"<em>{title}</em>")
    for k, v in SUPERSCRIPTS.items():
        t = t.replace(k, f'<sup><a href="#note-{v}" id="ref-{v}">{v}</a></sup>', 1)
    return t


def essay():
    body, notes = (HERE / "content" / "texte.txt").read_text().split("---NOTES---")
    paras = "".join(f"<p>{rich(' '.join(b.split()))}</p>" for b in body.strip().split("\n\n") if b.strip())
    items = []
    for n in notes.strip().split("\n\n"):
        n = n.strip()
        if not n:
            continue
        num = SUPERSCRIPTS.get(n[0], "")
        text = html.escape(n[1:].strip(), quote=False)
        for title in TEXT_TITLES:
            text = text.replace(title, f"<em>{title}</em>")
        items.append(f'<li id="note-{num}"><a href="#ref-{num}">{num}</a> {text}</li>')
    return paras, "".join(items)


def caption(title, place, when, fmt, ed):
    support = PAPER + (", contrecollé sur aluminium" if ed == 3 else "")
    return f"""<p class="t">{typo(title)}</p>
          <p>{place}, {when}</p>
          <p>{support}</p>
          <p>{fmt} cm, hors cadre · Édition de {ed}</p>"""


def works():
    out = []
    for i, w in enumerate(WORKS, 1):
        s = slug(w[0])
        kind = "port" if w[0] in PORTRAIT_WORKS else "land"
        w_, h_ = (1466, 2200) if kind == "port" else (2200, 1466)
        out.append(f"""
      <figure class="work {kind}" id="{s}">
        <a class="frame" href="img/works/{s}.jpg" data-full>
          <img src="img/thumbs/{s}.jpg" srcset="img/thumbs/{s}.jpg 900w, img/works/{s}.jpg 2200w"
               sizes="(min-width: 900px) 62vw, 100vw" width="{w_}" height="{h_}" loading="lazy"
               alt="{html.escape(typo(w[0]))}, {w[1]}, {w[2]}">
        </a>
        <figcaption><span class="n">{i:02d}</span>{caption(*w)}</figcaption>
      </figure>""")
    return "".join(out)


CSS = """
:root { --ink:#16203a; --soft:#5b6275; --rule:#cdc9bf; --paper:#f1efe9; --paper2:#e9e6de;
        --serif:'EB Garamond', Georgia, serif; --display:'Cormorant Garamond', Georgia, serif; }
* { box-sizing:border-box; margin:0; padding:0; }
html { scroll-behavior:smooth; scroll-padding-top:64px; }
body { background:var(--paper); color:var(--ink); font-family:var(--serif); font-size:18px; line-height:1.6;
       -webkit-font-smoothing:antialiased; }
a { color:inherit; }
img { display:block; max-width:100%; height:auto; }
.wrap { max-width:1180px; margin:0 auto; padding:0 24px; }

header.top { position:sticky; top:0; z-index:10; background:rgba(241,239,233,.92); backdrop-filter:blur(8px);
             border-bottom:.5px solid var(--rule); }
header.top .wrap { display:flex; justify-content:space-between; align-items:center; height:56px; gap:16px; }
.brand { font-family:var(--display); font-size:21px; font-weight:400; text-decoration:none; letter-spacing:.01em; white-space:nowrap; }
nav { display:flex; gap:22px; font-size:13px; letter-spacing:.14em; text-transform:uppercase; }
nav a { text-decoration:none; color:var(--soft); }
nav a:hover { color:var(--ink); }

.hero { position:relative; }
.hero img { width:100%; height:min(78vh, 66vw); object-fit:cover; object-position:50% 62%; }
.band { display:flex; justify-content:space-between; align-items:flex-end; gap:24px; padding:36px 0 56px;
        border-bottom:.5px solid var(--rule); }
h1, h2 { font-family:var(--display); font-weight:300; line-height:1.02; }
h1 { font-size:clamp(44px, 7vw, 88px); }
.sub { font-family:var(--display); font-style:italic; font-weight:300; font-size:clamp(19px, 2.2vw, 26px); margin-top:8px; }
.band .right { text-align:right; font-size:19px; line-height:1.55; }
.band .right .soft { color:var(--soft); font-size:16px; }

section { padding:96px 0; }
.label { font-size:12.5px; letter-spacing:.2em; text-transform:uppercase; color:var(--soft); }
h2 { font-size:clamp(36px, 4.6vw, 56px); margin:10px 0 36px; }

.intro { display:grid; grid-template-columns:1fr 1fr; gap:64px; align-items:start; }
.intro .lead { font-family:var(--display); font-size:clamp(23px, 2.4vw, 30px); line-height:1.35; font-weight:300; }
.facts { border-top:.5px solid var(--rule); }
.facts div { display:flex; justify-content:space-between; gap:20px; padding:13px 0; border-bottom:.5px solid var(--rule); }
.facts dt { color:var(--soft); }
.facts dd { text-align:right; }

.works { display:flex; flex-direction:column; gap:120px; padding-top:24px; }
.work { display:grid; grid-template-columns:minmax(0,1fr) 240px; gap:44px; align-items:end; }
.work.port { grid-template-columns:minmax(0,1fr) 240px; }
.work.port .frame { width:min(100%, 520px); justify-self:center; }
.work:nth-child(even) { grid-template-columns:240px minmax(0,1fr); }
.work:nth-child(even) .frame { order:2; }
.frame { display:block; cursor:zoom-in; }
.frame img { width:100%; box-shadow:0 6px 22px rgba(22,32,58,.16); }
.work.port .frame img { width:auto; max-height:84vh; margin:0 auto; }
figcaption { font-size:15.5px; line-height:1.5; color:var(--soft); }
figcaption .n { display:block; font-size:12px; letter-spacing:.2em; margin-bottom:10px; }
figcaption .t { font-style:italic; font-size:22px; line-height:1.2; color:var(--ink); margin-bottom:6px; }

.essay { background:var(--paper2); }
.essay .meta { color:var(--soft); padding-bottom:28px; border-bottom:.5px solid var(--rule); margin-bottom:40px; }
.essay .body { columns:2; column-gap:56px; text-align:justify; hyphens:auto; font-size:17.5px; }
.essay .body p { orphans:3; widows:3; }
.essay .body p + p { margin-top:14px; }
.essay sup { font-size:.62em; line-height:0; }
.essay sup a { text-decoration:none; color:var(--soft); }
.essay .sig { font-style:italic; text-align:right; margin-top:20px; }
.notes { list-style:none; margin-top:48px; padding-top:20px; border-top:.5px solid var(--rule); font-size:14.5px;
         color:var(--soft); columns:2; column-gap:56px; }
.notes li { break-inside:avoid; margin-bottom:10px; }
.notes a { text-decoration:none; color:var(--ink); }

.bio { display:grid; grid-template-columns:340px 1fr; gap:72px; align-items:start; }
.bio img { width:100%; aspect-ratio:3/4; object-fit:cover; border:.5px solid var(--rule); }
.bio .name { margin-top:22px; letter-spacing:.18em; text-transform:uppercase; font-size:14px; }
.bio .body { text-align:justify; hyphens:auto; }
.bio .body p + p { margin-top:14px; }

.contact { border-top:.5px solid var(--rule); }
.contact .rows { display:grid; grid-template-columns:1fr 1fr; gap:48px; }
.contact .who { font-family:var(--display); font-size:30px; font-weight:300; }
.contact .role { color:var(--soft); margin-bottom:8px; }
.contact a.mail { font-size:19px; text-decoration-thickness:.5px; text-underline-offset:4px; }
footer { padding:28px 0 40px; color:var(--soft); font-size:14px; border-top:.5px solid var(--rule); }
footer .wrap { display:flex; justify-content:space-between; gap:16px; flex-wrap:wrap; }

.lightbox { position:fixed; inset:0; background:rgba(14,18,30,.94); display:none; align-items:center;
            justify-content:center; z-index:50; cursor:zoom-out; padding:24px; }
.lightbox.on { display:flex; }
.lightbox img { max-width:100%; max-height:100%; object-fit:contain; }

@media (max-width: 900px) {
  body { font-size:17px; }
  nav { display:none; }
  .band { flex-direction:column; align-items:flex-start; padding:28px 0 40px; }
  .band .right { text-align:left; }
  section { padding:64px 0; }
  .intro, .bio, .contact .rows { grid-template-columns:1fr; gap:36px; }
  .bio img { max-width:320px; }
  .works { gap:72px; }
  .work, .work.port, .work:nth-child(even) { grid-template-columns:1fr; gap:16px; }
  .work:nth-child(even) .frame { order:0; }
  .essay .body, .notes { columns:1; }
}
"""

JS = """
const lb = document.querySelector('.lightbox'), lbi = lb.querySelector('img');
document.querySelectorAll('[data-full]').forEach(a => a.addEventListener('click', e => {
  e.preventDefault(); lbi.src = a.href; lbi.alt = a.querySelector('img').alt; lb.classList.add('on');
}));
lb.addEventListener('click', () => { lb.classList.remove('on'); lbi.removeAttribute('src'); });
document.addEventListener('keydown', e => { if (e.key === 'Escape') lb.click(); });
"""


def main():
    paras, notes = essay()
    bio = "".join(f"<p>{p}</p>" for p in BIO)
    cover = slug(COVER)
    page = f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Arnaud de Turckheim · Ce Qui Demeure</title>
<meta name="description" content="Ce Qui Demeure, première exposition photographique d’Arnaud de Turckheim. {DATES}, {ADDRESS}. Commissariat de Pierre El Khoury.">
<meta property="og:title" content="Ce Qui Demeure · Arnaud de Turckheim">
<meta property="og:description" content="Première exposition photographique d’Arnaud de Turckheim. {DATES}, {ADDRESS}.">
<meta property="og:image" content="https://arnauddeturckheim.com/img/works/{cover}.jpg">
<meta property="og:type" content="website">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' fill='%2316203a'/%3E%3Ctext x='16' y='22' font-family='Georgia' font-size='16' fill='%23f1efe9' text-anchor='middle'%3EAT%3C/text%3E%3C/svg%3E">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;1,300&family=EB+Garamond:ital,wght@0,400;0,600;1,400&display=swap">
<style>{CSS}</style>
</head>
<body>
<header class="top"><div class="wrap">
  <a class="brand" href="#">Arnaud de Turckheim</a>
  <nav><a href="#exposition">Exposition</a><a href="#oeuvres">Œuvres</a><a href="#texte">Texte</a><a href="#bio">Bio</a><a href="#contact">Contact</a></nav>
</div></header>

<main>
<div class="hero"><img src="img/works/{cover}.jpg" width="2200" height="1466" alt="Hors saison, Los Angeles, février 2018" fetchpriority="high"></div>
<div class="wrap"><div class="band">
  <div><h1>Ce Qui Demeure</h1><p class="sub">Une exposition d’Arnaud de Turckheim</p></div>
  <div class="right"><p>{DATES}</p><p>{ADDRESS}</p><p class="soft">Commissariat de Pierre El Khoury</p></div>
</div></div>

<section id="exposition"><div class="wrap intro">
  <div><p class="label">L’exposition</p><h2>Dix-huit tirages, une première</h2>
    <p class="lead">Une décennie de photographie restée privée, montrée pour la première fois. Des images prises au Japon, en Californie, au Maroc, au Sénégal et en France, réunies autour d’une même question&nbsp;: qu’est-ce qui demeure lorsque tout continue de passer&nbsp;?</p></div>
  <dl class="facts">
    <div><dt>Dates</dt><dd>4 - 19 novembre 2026</dd></div>
    <div><dt>Lieu</dt><dd>{ADDRESS}</dd></div>
    <div><dt>Commissariat</dt><dd>Pierre El Khoury</dd></div>
    <div><dt>Œuvres</dt><dd>18 tirages pigmentaires</dd></div>
    <div><dt>Papier</dt><dd>Hahnemühle Photo Rag Baryta</dd></div>
    <div><dt>Formats</dt><dd>40 × 60 cm, éditions de 5<br>80 × 120 cm, éditions de 3</dd></div>
  </dl>
</div></section>

<section id="oeuvres"><div class="wrap">
  <p class="label">Les œuvres</p><h2>Liste des œuvres</h2>
  <div class="works">{works()}
  </div>
</div></section>

<section id="texte" class="essay"><div class="wrap">
  <p class="label">Texte d’exposition</p><h2>Ce Qui Demeure</h2>
  <p class="meta">Par Pierre El Khoury, commissaire de l’exposition</p>
  <div class="body">{paras}<p class="sig">Pierre El Khoury</p></div>
  <ol class="notes">{notes}</ol>
</div></section>

<section id="bio"><div class="wrap bio">
  <div><img src="img/portrait.jpg" width="900" height="900" alt="Portrait d’Arnaud de Turckheim" loading="lazy">
    <p class="name">Arnaud de Turckheim</p></div>
  <div><p class="label">L’artiste</p><h2>Bio</h2><div class="body">{bio}</div></div>
</div></section>

<section id="contact" class="contact"><div class="wrap">
  <p class="label">Contact</p><h2>Écrire</h2>
  <div class="rows">
    <div><p class="who">Arnaud de Turckheim</p><p class="role">Artiste</p>
      <a class="mail" href="mailto:{EMAIL_ARNAUD}">{EMAIL_ARNAUD}</a></div>
    <div><p class="who">Pierre El Khoury</p><p class="role">Commissaire de l’exposition</p>
      <a class="mail" href="mailto:{EMAIL_PIERRE}">{EMAIL_PIERRE}</a></div>
  </div>
</div></section>
</main>

<footer><div class="wrap">
  <span>© 2026 Arnaud de Turckheim. Toutes les images sont protégées.</span>
  <span>Commissariat de Pierre El Khoury · Lieu prêté par Roka</span>
</div></footer>

<div class="lightbox" role="dialog" aria-label="Image en grand"><img alt=""></div>
<script>{JS}</script>
</body>
</html>
"""
    (HERE / "index.html").write_text(page, encoding="utf-8")
    print("index.html")


if __name__ == "__main__":
    main()
