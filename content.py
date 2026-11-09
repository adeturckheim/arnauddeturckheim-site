"""Contenus éditoriaux du site. Règle d'Arnaud : trait d'union, jamais de tiret long.

Sources : Expo/2 - Contenu (bio publique, introduction), Expo/9 - Preview/build.py (liste et bio),
Expo/8 - Texte exposition/texte.txt (texte de Pierre El Khoury), carton du 4 novembre (dates).
"""

NB = " "

SITE = {
    "name": "Arnaud de Turckheim",
    "url": "https://arnauddeturckheim.com",
    "email": "adeturckheim@gmail.com",
    "tagline": "Photographe. Paris.",
}

# (titre, lieu, pays, date de prise de vue, format H x L, édition) - ordre de l'accrochage
WORKS = [
    ("Les porteurs de lumière", "Shimoda", "Japon", "juillet 2017", "80 × 120", 3),
    ("L'attente de l'eau", "Ise", "Japon", "juillet 2017", "40 × 60", 5),
    ("Le Témoin", "Berlin", "Allemagne", "octobre 2017", "40 × 60", 5),
    ("L'apparition", "Provence", "France", "janvier 2018", "40 × 60", 5),
    ("La Gardienne", "Paris", "France", "janvier 2018", "80 × 120", 3),
    ("Le temps suspendu", "Iidabashi", "Japon", "juin 2017", "40 × 60", 5),
    ("L'ascension", "Los Angeles", "États-Unis", "avril 2017", "40 × 60", 5),
    ("La charpente du monde", "San Francisco", "États-Unis", "avril 2017", "40 × 60", 5),
    ("L'autre côté", "Hakone", "Japon", "juillet 2017", "40 × 60", 5),
    ("Les revenantes", "Provence", "France", "décembre 2017", "40 × 60", 5),
    ("Le détour", "Tokyo", "Japon", "mai 2017", "80 × 120", 3),
    ("Quiétude", "Nakano", "Japon", "mai 2017", "40 × 60", 5),
    ("La traversée", "Tokyo", "Japon", "juillet 2017", "40 × 60", 5),
    ("Habiter l'absence", "Marrakech", "Maroc", "octobre 2017", "40 × 60", 5),
    ("Le songe éveillé", "Shimoda", "Japon", "juillet 2017", "60 × 40", 5),
    ("L'attente", "Hakone", "Japon", "juillet 2017", "120 × 80", 3),
    ("La Figure de l'absence", "Sine-Saloum", "Sénégal", "mai 2019", "120 × 80", 3),
    ("Hors saison", "Los Angeles", "États-Unis", "février 2018", "40 × 60", 5),
]
PORTRAIT_WORKS = {"L'attente", "La Figure de l'absence", "Le songe éveillé"}
PAPER = "Tirage jet d’encre pigmentaire sur papier Hahnemühle Photo Rag Baryta 315 g"

# Extraits du texte de Pierre El Khoury, affichés sur la page de l'œuvre concernée
EXCERPTS = {
    "La Figure de l'absence": "Un baobab centenaire qui se dresse, seul, face à la lumière.",
    "Les porteurs de lumière": "Les figures des travailleurs et leurs ombres se répondent, ouvrant un espace "
                               "entre le vivant et sa trace.",
    "Les revenantes": "L’ombre semble conserver la mémoire d’un corps.",
    "Hors saison": "La piscine vide semble privée de sa fonction habituelle.",
    "L'apparition": "Le grain et la texture photographique participent à la présence du sujet.",
    "La Gardienne": "Une zone d’opacité qui laisse au visage sa liberté et son mystère.",
    "Le songe éveillé": "Les portraits ne cherchent pas à tout révéler" + NB + ": ils préservent une part de retrait.",
    "La traversée": "Le déplacement ne devient pas le prétexte à raconter une histoire de voyage, mais "
                    "l’occasion de saisir un instant dont le sens reste ouvert.",
    "Le détour": "Saisir un instant dont le sens reste ouvert.",
}

HOME_LEAD = (
    "Des images trouvées plutôt que fabriquées" + NB + ": un geste, une lumière, une géométrie "
    "qui affleurent dans l’ordinaire."
)

STATEMENT = [
    "Arnaud de Turckheim photographie ce qui se donne sans avoir été demandé. Ses images ne naissent "
    "ni d’une commande ni d’une mise en scène" + NB + ": deux ouvriers et leurs ombres sur un quai de "
    "Shimoda, un passage à niveau à Nakano, une piscine vide à Los Angeles, un baobab dans le "
    "Sine-Saloum. Rien de spectaculaire, mais l’instant précis où l’ordinaire bascule.",
    "Le regard refuse le pittoresque. Pas de Japon folklorique, pas d’Afrique de carte postale, pas "
    "d’Amérique de cinéma" + NB + ": il cherche l’angle mort du cliché. Souvent, une figure seule tient "
    "un cadre large. La lumière, rasante ou à contre-jour, sculpte autant qu’elle révèle. Les images "
    "respirent plutôt qu’elles ne parlent.",
    "Ce sont des photographies numériques, honnêtes, cadrées par l’œil et non par un modèle. Faites "
    "avant la bascule générative, elles appartiennent à un temps où une image se trouvait plutôt "
    "qu’elle ne se générait.",
]

BIO = [
    "Né à Paris en 1990, Arnaud de Turckheim grandit entre Paris et la Provence, dans une famille où "
    "l’image est une langue familière" + NB + ": sa mère est photographe. Ingénieur de formation, il vit "
    "en Chine, en Angleterre puis au Japon, avant de rentrer en France en 2017.",
    "Il photographie depuis les années 2000. Une pratique longtemps tenue en retrait, presque vingt ans "
    "d’images gardées pour soi, qu’il rend publique pour la première fois en novembre 2026 avec "
    "<em>Ce Qui Demeure</em>, sous le commissariat de Pierre El Khoury.",
    "De ses années nomades, il garde un goût pour l’observation discrète. Ses proches le décrivent "
    "volontiers comme un «" + NB + "geek cowboy" + NB + "», partagé entre la logique de l’ingénieur et "
    "l’attrait des grands espaces. Son écriture est reconnaissable" + NB + ": contre-jours tenus, "
    "lumières rasantes, contrastes francs, nuances de gris et de vert.",
    "Un mot revient souvent à propos de son travail" + NB + ": <em>intense</em>. Il dit la manière dont "
    "il se tient face à ses sujets, à la fois dedans et dehors du moment, dans cet entre-deux attentif "
    "qui fait la photographie.",
]

MILESTONES = [
    ("1990", "Naissance à Paris."),
    ("Années 2000", "Premières photographies, une pratique gardée privée."),
    ("Années 2010", "Études d’ingénieur et premières années dans la tech. Vit en Chine, en Angleterre et au "
                    "Japon. La décennie où naissent la plupart de ses images."),
    ("2020", "Fonde sa propre entreprise."),
    ("2026", "<em>Ce Qui Demeure</em>, première exposition personnelle, Paris."),
]

EXPO = {
    "slug": "ce-qui-demeure",
    "title": "Ce Qui Demeure",
    "year": "2026",
    "dates": "4 - 19 novembre 2026",
    "opening": "Vernissage le mercredi 4 novembre 2026",
    "address": "10 rue Lincoln, 75008 Paris",
    "curator": "Pierre El Khoury",
    "curator_email": "pek.elkhoury@gmail.com",
    "sales_phone": "06 50 85 07 98",  # Pierre, contact acquisitions (accord d'Arnaud)
    "sales_tel": "+33650850798",
    "credits": ["Commissariat de Pierre El Khoury", "Lieu prêté par Roka", "Tirages Picto Bastille, Paris"],
    "lead": "Première exposition personnelle d’Arnaud de Turckheim. Dix-huit photographies, une même "
            "question" + NB + ": qu’est-ce qui demeure lorsque tout continue de passer" + NB + "?",
    "intro": [
        "Dix-huit tirages, pris au Japon, aux États-Unis, en Allemagne, au Maroc, "
        "au Sénégal et en France. L’exposition ne suit pourtant ni une géographie ni une chronologie"
        + NB + ": les images se détachent de leur lieu pour se répondre les unes aux autres.",
        "Elle s’ouvre sur un baobab centenaire, <em>La Figure de l’absence</em>, présence silencieuse "
        "qui donne le ton" + NB + ": être là sans s’imposer. Suivent des portraits qui gardent leur part "
        "d’ombre, des scènes de rue saisies dans leurs heures creuses, des formes que la lumière "
        "rend étranges.",
        "<em>Ce Qui Demeure</em> est assumée comme une exposition pré-IA" + NB + ": l’image telle "
        "qu’elle se faisait avant la bascule générative, cadrée par un regard et non par un modèle. "
        "Une première monstration, et le début d’une conversation.",
    ],
}


# ================================================================ English
# Titres des œuvres conservés en français (usage des galeries) ; tout le reste est traduit.

MONTHS_EN = {"janvier": "January", "février": "February", "mars": "March", "avril": "April", "mai": "May",
             "juin": "June", "juillet": "July", "août": "August", "septembre": "September",
             "octobre": "October", "novembre": "November", "décembre": "December"}
COUNTRIES_EN = {"Japon": "Japan", "Allemagne": "Germany", "France": "France", "États-Unis": "United States",
                "Maroc": "Morocco", "Sénégal": "Senegal"}
PAPER_EN = "Archival pigment print on Hahnemühle Photo Rag Baryta 315 gsm paper"

EXCERPTS_EN = {
    "La Figure de l'absence": "A century-old baobab standing alone against the light.",
    "Les porteurs de lumière": "The figures of the workers and their shadows answer one another, opening a "
                               "space between the living and its trace.",
    "Les revenantes": "The shadow seems to keep the memory of a body.",
    "Hors saison": "The empty swimming pool seems deprived of its usual function.",
    "L'apparition": "Grain and photographic texture contribute to the presence of the subject.",
    "La Gardienne": "A zone of opacity that leaves the face its freedom and its mystery.",
    "Le songe éveillé": "The portraits do not seek to reveal everything: they preserve a share of withdrawal.",
    "La traversée": "Movement does not become a pretext for telling a travel story, but an occasion to seize "
                    "an instant whose meaning remains open.",
    "Le détour": "To seize an instant whose meaning remains open.",
}

HOME_LEAD_EN = "Images found rather than made: a gesture, a light, a geometry surfacing in the ordinary."

STATEMENT_EN = [
    "Arnaud de Turckheim photographs what offers itself without being asked for. His images are born "
    "neither of a commission nor of staging: two workers and their shadows on a platform in Shimoda, a "
    "level crossing in Nakano, an empty swimming pool in Los Angeles, a baobab in the Sine-Saloum. "
    "Nothing spectacular, only the precise moment when the ordinary tips over.",
    "His eye refuses the picturesque. No folkloric Japan, no postcard Africa, no movie-set America: he "
    "looks for the blind spot of the cliché. Often a single figure holds a wide frame. Light, raking or "
    "backlit, sculpts as much as it reveals. The images breathe rather than speak.",
    "These are digital photographs, honest ones, framed by the eye and not by a model. Made before the "
    "generative shift, they belong to a time when an image was found rather than generated.",
]

BIO_EN = [
    "Born in Paris in 1990, Arnaud de Turckheim grew up between Paris and Provence, in a family where the "
    "image is a familiar language: his mother is a photographer. An engineer by training, he lived in "
    "China, England and then Japan before returning to France in 2017.",
    "He has been taking photographs since the 2000s. A practice long kept to himself, nearly twenty years "
    "of images held back, which he makes public for the first time in November 2026 with "
    "<em>Ce Qui Demeure</em>, curated by Pierre El Khoury.",
    "From his nomadic years he has kept a taste for discreet observation. Friends readily describe him as "
    "a “geek cowboy”, torn between the engineer’s logic and the pull of wide open spaces. His style is "
    "recognisable: sustained backlight, raking light, frank contrasts, shades of grey and green.",
    "One word often comes up about his work: <em>intense</em>. It speaks to the way he stands before his "
    "subjects, both inside and outside the moment, in that attentive in-between that makes photography.",
]

MILESTONES_EN = [
    ("1990", "Born in Paris."),
    ("2000s", "First photographs, a practice kept private."),
    ("2010s", "Engineering studies and first years in tech. Lives in China, England and Japan. The decade "
              "in which most of his images are made."),
    ("2020", "Founds his own company."),
    ("2026", "<em>Ce Qui Demeure</em>, first solo exhibition, Paris."),
]

EXPO_EN = {
    "dates": "4 - 19 November 2026",
    "opening": "Wednesday 4 November",
    "credits": ["Curated by Pierre El Khoury", "Venue courtesy of Roka", "Prints by Picto Bastille, Paris"],
    "lead": "Arnaud de Turckheim’s first solo exhibition. Eighteen photographs, one question: what remains "
            "when everything keeps passing?",
    "intro": [
        "Eighteen prints, taken in Japan, the United States, Germany, Morocco, "
        "Senegal and France. Yet the exhibition follows neither a geography nor a chronology: the images "
        "detach themselves from their place and answer one another.",
        "It opens on a century-old baobab, <em>La Figure de l’absence</em>, a silent presence that sets "
        "the tone: to be there without imposing oneself. Then come portraits that keep their share of "
        "shadow, street scenes caught in their off hours, forms made strange by light.",
        "<em>Ce Qui Demeure</em> (What Remains) is assumed as a pre-AI exhibition: the image as it was made "
        "before the generative shift, framed by a gaze and not by a model. A first showing, and the "
        "beginning of a conversation.",
    ],
}
