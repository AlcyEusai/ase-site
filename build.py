#!/usr/bin/env python3
"""Génère les pages HTML du site ASE. Usage : python3 build.py (ou modifier directement les .html générés)."""
LOGO = open("images/logo.svg").read().replace('<svg ', '<svg aria-hidden="true" ')
NAV = [("index.html","Accueil"),("qui-sommes-nous.html","Qui sommes-nous ?"),("expertises.html","Nos expertises"),("equipe.html","Notre équipe"),("actualites.html","Actualités"),("contact.html","Contact")]
SOC = '<a href="#" rel="noopener">LinkedIn</a><a href="#" rel="noopener">Facebook</a><a href="#" rel="noopener">YouTube</a>'
PH = '<span class="tag">À compléter</span>'
def page(fn, title, desc, body, hero=None):
    nav = "".join(f'<a href="{h}"{" aria-current=\"page\"" if h==fn else ""}>{t}</a>' for h,t in NAV)
    top = hero or f'<div class="page-title"><div class="w"><h1>{title}</h1></div></div>'
    html = f'''<!DOCTYPE html>
<html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} – ASE</title><meta name="description" content="{desc}">
<meta property="og:title" content="{title} – ASE"><meta property="og:description" content="{desc}"><meta property="og:type" content="website">
<link rel="icon" href="images/logo.svg" type="image/svg+xml">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700&display=swap">
<link rel="stylesheet" href="css/style.css"></head><body>
<a class="skip" href="#main">Aller au contenu</a>
<header><div class="w"><a class="logo" href="index.html" aria-label="ASE – Accueil">{LOGO}<span><b>ASE</b><small>Agriculture, Services et Expertise</small></span></a><nav aria-label="Navigation principale">{nav}</nav></div></header>
<main id="main">{top}{body}</main>
<footer><div class="w"><div><strong style="font-size:22px">ASE</strong><br>Agriculture, Services et Expertise<p>Cabinet de conseil agricole : une expertise technique adaptée à chaque besoin.</p></div>
<div><h3>Navigation</h3>{"".join(f'<a href="{h}">{t}</a>' for h,t in NAV[1:])}</div>
<div><h3>Coordonnées</h3><p>[adresse postale]<br>[téléphone]<br>[e-mail]</p>{PH}</div>
<div><h3>Suivez-nous</h3><div class="soc">{SOC}</div><p><a href="mentions-legales.html">Mentions légales</a><a href="confidentialite.html">Politique de confidentialité</a></p></div></div>
<div class="legal">© ASE – Tous droits réservés.</div></footer>
<script src="js/config.js"></script><script src="js/main.js"></script></body></html>'''
    open(fn,"w",encoding="utf-8").write(html)

hero = '''<div class="hero"><svg viewBox="0 0 800 220" preserveAspectRatio="none" aria-hidden="true"><circle cx="620" cy="30" r="30" fill="#f6c94c"/><path d="M0 70Q200 20 400 60T800 40V220H0z" fill="#9cc47a"/><path d="M0 110Q200 70 420 100T800 85V220H0z" fill="#78A96B"/><path d="M0 160Q220 120 440 150T800 135V220H0z" fill="#4f9060"/><path d="M0 200Q250 170 480 195T800 185V220H0z" fill="#286B45"/></svg>
<div class="w"><h1>Construire aujourd’hui des solutions durables pour demain.</h1><p>ASE vous accompagne dans vos projets grâce à une expertise technique adaptée à vos enjeux.</p><a class="btn" href="expertises.html">Découvrir nos expertises →</a></div></div>'''
ic = lambda d: f'<svg viewBox="0 0 48 48" aria-hidden="true">{d}</svg>'
DOMS = [("Agriculture & agroalimentaire","Conseil et accompagnement des filières.",ic('<path d="M24 42V22M24 26c-9 0-12-6-12-12 8 0 12 4 12 12zM24 30c7 0 10-5 10-10-7 0-10 4-10 10z"/>')),
("Bâtiments & travaux publics","Expertise technique pour vos projets.",ic('<path d="M8 32a16 16 0 0132 0zM6 36h36M24 14v18"/>')),
("Gestion des déchets","Valorisation et solutions durables.",ic('<path d="M16 14l8-6 8 6M32 14l6 10M38 24l-6 10M32 34H18M18 34l-6-10M12 24l4-10"/>')),
("Développement durable","Agir ensemble pour un avenir responsable.",ic('<circle cx="24" cy="24" r="16"/><ellipse cx="24" cy="24" rx="7" ry="16"/><path d="M8 24h32"/>'))]
doms = '<div class="w"><div class="dom">' + "".join(f'<div class="card">{i}<h3>{t}</h3><p>{d}</p></div>' for t,d,i in DOMS) + '</div></div>'
VALS = ["Responsabilité sociale et environnementale","Durabilité","Excellence","Écoute","Innovation"]
vals = '<ul class="vals">' + "".join(f"<li>{v}</li>" for v in VALS) + '</ul>'
PRES = "Le cabinet ASE est spécialisé dans le conseil agricole en accompagnant des acteurs de la filière agricole et agroalimentaire, des bâtiments et travaux publics et de la gestion des déchets. Nous offrons une expertise technique adaptée à chaque besoin."
MIS = '<div class="mis"><strong>Notre mission</strong><br>Aider nos clients à atteindre leurs objectifs de développement durable.</div>'
phimg = lambda t,h=180: f'<div class="ph" style="min-height:{h}px" role="img" aria-label="Emplacement photo">{t}</div>'
def news(n=3): return '<div class="grid">' + "".join(f'<article class="card">{phimg("Image de l’article",100)}<span class="tag">Exemple de mise en page</span><h3>Titre de l’article</h3><p>Date · résumé à venir.</p></article>' for _ in range(n)) + '</div>'

page("index.html","Accueil","ASE, cabinet de conseil agricole : expertise technique pour l’agriculture, l’agroalimentaire, le BTP et la gestion des déchets.",
 doms + f'<section><div class="w"><div class="two"><div><h2>Qui sommes-nous ?</h2><p>{PRES}</p>{MIS}<a class="btn" href="qui-sommes-nous.html">En savoir plus →</a></div>{phimg("Photo à ajouter : l’équipe ASE sur le terrain",240)}</div></div></section>'
 f'<section class="alt"><div class="w"><h2>Nos valeurs</h2>{vals}</div></section>'
 f'<section><div class="w"><h2>Dernières actualités</h2>{news()}<p><a href="actualites.html">Voir toutes les actualités →</a></p></div></section>'
 f'<section class="alt"><div class="w"><h2>Nous contacter</h2><p>Une question ? Un projet ? Contactez notre équipe.</p><a class="btn" href="contact.html">Nous écrire →</a></div></section>', hero)

page("qui-sommes-nous.html","Qui sommes-nous ?","Présentation, mission et valeurs du cabinet ASE.",
 f'<section><div class="w"><div class="two"><div><h2>Présentation</h2><p>{PRES}</p>{MIS}</div>{phimg("Photo à ajouter",240)}</div><h2 style="margin-top:40px">Nos valeurs</h2>{vals}</div></section>')

EXP = [("Agriculture et agroalimentaire","Accompagnement des acteurs de la filière agricole et agroalimentaire."),("Bâtiments et travaux publics","Expertise technique pour les acteurs du bâtiment et des travaux publics."),("Gestion et valorisation des déchets","Accompagnement dans la gestion des déchets."),("Développement durable","Aider nos clients à atteindre leurs objectifs de développement durable.")]
page("expertises.html","Nos expertises","Les domaines d’expertise du cabinet ASE.",
 '<section><div class="w"><div class="grid">' + "".join(f'<div class="card">{phimg("Photo à ajouter",120)}<h3>{t}</h3><p>{d}</p><p>{PH} Détail des prestations à confirmer par le cabinet.</p></div>' for t,d in EXP) + '</div></div></section>')

AV = '<div class="av"><svg width="40" height="40" viewBox="0 0 40 40" aria-hidden="true"><circle cx="20" cy="15" r="8" fill="#78A96B"/><path d="M5 38c2-12 28-12 30 0z" fill="#78A96B"/></svg></div>'
page("equipe.html","Notre équipe","Les collaborateurs du cabinet ASE.",
 '<section><div class="w"><p>Modèle de fiche à dupliquer pour chaque collaborateur.</p><div class="grid">' + "".join(f'<div class="card">{AV}<span class="tag">Contenu provisoire</span><h3>Prénom Nom</h3><p><strong>Fonction :</strong> à compléter</p><p><strong>Biographie :</strong> à compléter</p><p><strong>Compétences et expériences :</strong> à compléter</p></div>' for _ in range(3)) + '</div></div></section>')

page("actualites.html","Actualités","Actualités, projets, événements, publications et partenariats d’ASE.",
 f'<section><div class="w"><p>Actualités du cabinet, projets réalisés, événements, publications et partenariats. Dupliquer un bloc « article » pour chaque publication (image, date, titre, résumé).</p>{news(3)}</div></section>')

page("contact.html","Contact","Contacter le cabinet ASE : adresse, téléphone, e-mail et formulaire.",
 f'''<section><div class="w"><div class="two"><div><h2>Nos coordonnées</h2><p><strong>Adresse postale</strong><br>[à compléter]</p><p><strong>Téléphone</strong> : [à compléter]<br><strong>E-mail</strong> : [à compléter]</p>{PH}<p>Carte de localisation : à intégrer lorsque l’adresse sera communiquée.</p><div class="soc">{SOC}</div></div>
<div><h2>Écrivez-nous</h2><form id="contact-form"><div><label for="n">Nom</label><input id="n" name="nom" required autocomplete="name"></div><div><label for="e">E-mail</label><input id="e" name="email" type="email" required autocomplete="email"></div><div><label for="s">Sujet</label><input id="s" name="sujet" required></div><div><label for="m">Message</label><textarea id="m" name="message" rows="5" required></textarea></div><input class="hp" name="website" tabindex="-1" autocomplete="off" aria-hidden="true"><button class="btn" type="submit">Envoyer</button><p id="msg" role="status"></p></form></div></div></div></section>''')

page("mentions-legales.html","Mentions légales","Mentions légales du site ASE.",f'<section><div class="w"><p>{PH} Texte à rédiger avec les informations officielles du cabinet (raison sociale, forme juridique, adresse du siège, numéro d’immatriculation, directeur de la publication, hébergeur).</p></div></section>')
page("confidentialite.html","Politique de confidentialité","Politique de confidentialité du site ASE.",f'<section><div class="w"><p>{PH} Texte à rédiger : données collectées via le formulaire de contact, finalités, durée de conservation, droits des personnes (RGPD), contact.</p></div></section>')
