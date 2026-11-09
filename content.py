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
    ("Années 2000", "Premières photographies, une pratique tenue privée."),
    ("Avant 2017", "Vit en Chine, en Angleterre puis au Japon."),
    ("2017", "Retour en France."),
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
    "credits": ["Commissariat de Pierre El Khoury", "Lieu prêté par Roka", "Tirages Picto Bastille, Paris"],
    "lead": "Première exposition personnelle d’Arnaud de Turckheim. Dix-huit photographies, une même "
            "question" + NB + ": qu’est-ce qui demeure lorsque tout continue de passer" + NB + "?",
    "intro": [
        "Dix-huit tirages, pris entre 2017 et 2019 au Japon, aux États-Unis, en Allemagne, au Maroc, "
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
