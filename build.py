#!/usr/bin/env python3
"""Génère les pages HTML du site ASE. Usage : python3 build.py (ou modifier directement les .html générés)."""
LOGO = open("images/logo.svg").read().replace('<svg ', '<svg aria-hidden="true" ')
NAV = [("index.html","Accueil"),("qui-sommes-nous.html","Qui sommes-nous ?"),("expertises.html","Nos expertises"),("equipe.html","Notre équipe"),("actualites.html","Actualités"),("contact.html","Contact")]
PLAY = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 7c0-2 1-3 3-3h12c2 0 3 1 3 3v10c0 2-1 3-3 3H6c-2 0-3-1-3-3zM10 8.5v7l6-3.5z"/></svg>'
def soc(): return f'<a class="rs" href="#" rel="noopener" aria-label="LinkedIn">in</a><a class="rs" href="#" rel="noopener" aria-label="Facebook">f</a><a class="rs" href="#" rel="noopener" aria-label="YouTube">{PLAY}</a>'
PH = '<span class="tag">À compléter</span>'
ic = lambda d, c="": f'<svg viewBox="0 0 48 48" aria-hidden="true"{c}>{d}</svg>'
LEAF = '<path d="M10 38C8 20 20 8 40 8c0 20-10 32-28 30zM10 38L26 22"/>'
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
<header><div class="w"><a class="logo" href="index.html" aria-label="ASE – Accueil">
    <img src="images/ASE-symbole-seul.svg" alt="Symbole ASE">

    <div class="logo-text">
        <strong>ASE</strong>
        <span>ALL SOLUTION ENGINEERING</span>
        <small>Solutions related to each need</small>
    </div>
</a><div class="hdr"><nav aria-label="Navigation principale">{nav}</nav><div class="soc">{soc()}</div></div></div></header>
<main id="main">{top}{body}</main>
<footer><div class="w"><div><div class="brand">
    <img src="images/ASE-symbole-seul.svg" alt="Symbole ASE">
    <span class="brand-name">
        <strong>ASE</strong>
        <small>ALL SOLUTION ENGINEERING</small>
        <em>Solutions related to each need</em>
    </span>
</div><p><em>Ensemble pour un avenir durable</em></p></div>
<div><h3>Liens utiles</h3><a href="mentions-legales.html">Mentions légales</a><a href="confidentialite.html">Politique de confidentialité</a><a href="plan-du-site.html">Plan du site</a></div>
<div><h3>Suivez-nous</h3><div>{soc()}</div></div>
<div><h3>Newsletter</h3><p>Restez informé de nos actualités</p><form class="aseform nl" data-key="newsletterEndpoint"><label class="skip" for="nl-{fn[:-5]}">Votre e-mail</label><input id="nl-{fn[:-5]}" name="email" type="email" placeholder="Votre e-mail" required autocomplete="email"><button type="submit" aria-label="S’inscrire">→</button></form><div class="fmsg" role="status"></div></div></div>
<div class="legal">© ASE – Tous droits réservés.</div><div class="hills" aria-hidden="true"></div></footer>
<script src="js/config.js"></script><script src="js/main.js"></script></body></html>'''
    open(fn,"w",encoding="utf-8").write(html)

hero = '''<div class="hero"><div class="w"><h1>Construire aujourd’hui des solutions durables pour demain.</h1><p>ASE vous accompagne dans vos projets grâce à une expertise technique adaptée à vos enjeux.</p><a class="btn" href="expertises.html">Découvrir nos expertises →</a></div></div>'''
DOMS = [("Agriculture &amp; Agroalimentaire","Conseil et accompagnement des filières agricoles.",ic('<path d="M24 42V22M24 26c-9 0-12-6-12-12 8 0 12 4 12 12zM24 30c7 0 10-5 10-10-7 0-10 4-10 10z"/>')),
("Bâtiments &amp; Travaux publics","Expertise et accompagnement de vos projets.",ic('<path d="M8 32a16 16 0 0132 0zM6 36h36M24 14v18"/>')),
("Gestion des déchets","Valorisation et solutions durables.",ic('<path d="M16 14l8-6 8 6M32 14l6 10M38 24l-6 10M32 34H18M18 34l-6-10M12 24l4-10"/>')),
("Développement durable","Agir ensemble pour un avenir responsable.",ic('<circle cx="24" cy="24" r="16"/><ellipse cx="24" cy="24" rx="7" ry="16"/><path d="M8 24h32"/>'))]
doms = '<div class="w"><div class="dom">' + "".join(f'<div class="card">{i}<h3>{t}</h3><p>{d}</p></div>' for t,d,i in DOMS) + '</div></div>'
VALS = [("Responsabilité sociale et environnementale",'<circle cx="24" cy="16" r="6"/><circle cx="10" cy="20" r="4"/><circle cx="38" cy="20" r="4"/><path d="M12 40c0-8 24-8 24 0M2 36c0-6 8-8 11-6M46 36c0-6-8-8-11-6"/>'),("Durabilité",LEAF),("Excellence",'<path d="M16 8h16v10a8 8 0 01-16 0zM16 12H8c0 8 4 10 8 10M32 12h8c0 8-4 10-8 10M24 26v8M16 40h16M18 34h12"/>'),("Écoute",'<path d="M8 28v-6a16 16 0 0132 0v6M8 26h6v10H8zM34 26h6v10h-6zM40 36c0 4-6 6-12 6"/>'),("Innovation",'<path d="M17 30c-5-4-6-8-6-11a13 13 0 0126 0c0 3-1 7-6 11v4H17zM18 40h12M20 44h8"/>')]
vals_list = '<ul class="vals">' + "".join(f"<li>{v}</li>" for v,_ in VALS) + '</ul>'
band = '<div class="band"><div class="w"><h2>Nos valeurs</h2>' + "".join(f'<div class="vi">{ic(d)}{v}</div>' for v,d in VALS) + '</div></div>'
PRES = "Le cabinet ASE est spécialisé dans le conseil agricole en accompagnant des acteurs de la filière agricole et agroalimentaire, des bâtiments et travaux publics et de la gestion des déchets. Nous offrons une expertise technique adaptée à chaque besoin."
MIS = f'<div class="mis">{ic(LEAF)}<div><strong>Notre mission</strong><br>Aider nos clients à atteindre leurs objectifs de développement durable.</div></div>'
phimg = lambda t,h=180: f'<div class="ph" style="min-height:{h}px" role="img" aria-label="Emplacement photo">{t}</div>'
def news(n=3): return '<div class="news"><div class="grid">' + "".join(f'<article class="card"><div class="newsimg" role="img" aria-label="Image de l’article"></div><span class="tag">Exemple de mise en page</span><p>Date</p><h3>Titre de l’actualité</h3><p>Résumé à venir.</p></article>' for _ in range(n)) + '</div></div>'
MAP = '<div class="map" role="img" aria-label="Emplacement de la carte"><svg viewBox="0 0 200 120"><path d="M20 70c0-30 30-50 60-45 20-15 60-10 75 15 20 5 30 25 15 45-15 15-45 5-65 10-30 8-85 5-85-25z" fill="#c9dcc2"/><path d="M100 95S80 70 80 55a20 20 0 0140 0c0 15-20 40-20 40z" fill="#286B45"/><circle cx="100" cy="55" r="7" fill="#fff"/></svg><br>Carte à intégrer</div>'
CI = lambda i,t: f'<div class="ci">{ic(i)}<span>{t}</span></div>'
PIN='<path d="M24 44S10 28 10 19a14 14 0 0128 0c0 9-14 25-14 25z"/><circle cx="24" cy="19" r="5"/>'
TEL='<path d="M12 6l8 2-3 9c3 6 7 10 13 13l6-5 8 3-1 8c-2 3-6 4-11 2C19 33 10 22 8 14 6 9 8 7 12 6z"/>'
MAIL='<rect x="6" y="12" width="36" height="26" rx="3"/><path d="M6 14l18 14 18-14"/>'

page("index.html","Accueil","ASE, cabinet de conseil agricole : expertise technique pour l’agriculture, l’agroalimentaire, le BTP et la gestion des déchets.",
 doms + f'<section class="home-qui"><div class="w" style="display:contents"></div></section>'.replace('<div class="w" style="display:contents"></div>', f'<div class="w" style="display:grid;grid-template-columns:1fr 1.2fr;padding:0 0 0 20px"><div class="txt"><h2>Qui sommes-nous ?</h2><p>{PRES}</p>{MIS}<a class="btn" href="qui-sommes-nous.html">En savoir plus →</a></div><div class="teamph" role="img" aria-label="L’équipe ASE sur le terrain"></div></div>')
 + band
 + f'<section><div class="w nc"><div class="news"><h2>Actualités</h2><a class="more" href="actualites.html">Voir toutes les actualités →</a>{news()}</div><div><h2>Nous contacter</h2><p>Une question ? Un projet ?<br>Contactez notre équipe !</p>{CI(PIN,"[adresse postale]")}{CI(TEL,"[téléphone]")}{CI(MAIL,"[e-mail]")}{PH}{MAP}<p><a class="btn" href="contact.html">Nous écrire →</a></p></div></div></section>', hero)

page("qui-sommes-nous.html","Qui sommes-nous ?","Présentation, mission et valeurs du cabinet ASE.",
 f'<section><div class="w"><div class="two"><div><h2>Présentation</h2><p>{PRES}</p>{MIS}</div><div class="teamph" style="min-height:260px;border-radius:12px" role="img" aria-label="L’équipe ASE"></div></div></div></section>{band}')

EXP = [("Agriculture et agroalimentaire","Accompagnement des acteurs de la filière agricole et agroalimentaire."),("Bâtiments et travaux publics","Expertise technique pour les acteurs du bâtiment et des travaux publics."),("Gestion et valorisation des déchets","Accompagnement dans la gestion des déchets."),("Développement durable","Aider nos clients à atteindre leurs objectifs de développement durable.")]
page("expertises.html","Nos expertises","Les domaines d’expertise du cabinet ASE.",
 '<section><div class="w"><div class="grid">' + "".join(f'<div class="card">{phimg("Photo à ajouter",120)}<h3>{t}</h3><p>{d}</p><p>{PH} Détail des prestations à confirmer par le cabinet.</p></div>' for t,d in EXP) + '</div></div></section>')

AV = '<div class="av"><svg width="40" height="40" viewBox="0 0 40 40" aria-hidden="true"><circle cx="20" cy="15" r="8" fill="#78A96B"/><path d="M5 38c2-12 28-12 30 0z" fill="#78A96B"/></svg></div>'
page("equipe.html","Notre équipe","Les collaborateurs du cabinet ASE.",
 '<section><div class="w"><p>Modèle de fiche à dupliquer pour chaque collaborateur.</p><div class="grid">' + "".join(f'<div class="card">{AV}<span class="tag">Contenu provisoire</span><h3>Prénom Nom</h3><p><strong>Fonction :</strong> à compléter</p><p><strong>Biographie :</strong> à compléter</p><p><strong>Compétences et expériences :</strong> à compléter</p></div>' for _ in range(3)) + '</div></div></section>')

page("actualites.html","Actualités","Actualités, projets, événements, publications et partenariats d’ASE.",
 f'<section><div class="w"><p>Actualités du cabinet, projets réalisés, événements, publications et partenariats. Dupliquer un bloc « article » pour chaque publication (image, date, titre, résumé).</p>{news(3)}</div></section>')

page("contact.html","Contact","Contacter le cabinet ASE : adresse, téléphone, e-mail et formulaire.",
 f'''<section><div class="w"><div class="two"><div><h2>Nos coordonnées</h2>{CI(PIN,"[adresse postale]")}{CI(TEL,"[téléphone]")}{CI(MAIL,"[e-mail]")}{PH}{MAP}<div class="soc" style="margin-top:12px">{soc()}</div></div>
<div><h2>Écrivez-nous</h2><form class="aseform" data-key="formEndpoint"><div><label for="n">Nom</label><input id="n" name="nom" required autocomplete="name"></div><div><label for="e">E-mail</label><input id="e" name="email" type="email" required autocomplete="email"></div><div><label for="s">Sujet</label><input id="s" name="sujet" required></div><div><label for="m">Message</label><textarea id="m" name="message" rows="5" required></textarea></div><input class="hp" name="website" tabindex="-1" autocomplete="off" aria-hidden="true"><button class="btn" type="submit">Envoyer</button></form><p class="fmsg" role="status"></p></div></div></div></section>''')

page("mentions-legales.html","Mentions légales","Mentions légales du site ASE.",f'<section><div class="w"><p>{PH} Texte à rédiger avec les informations officielles du cabinet (raison sociale, forme juridique, adresse du siège, numéro d’immatriculation, directeur de la publication, hébergeur).</p></div></section>')
page("confidentialite.html","Politique de confidentialité","Politique de confidentialité du site ASE.",f'<section><div class="w"><p>{PH} Texte à rédiger : données collectées via le formulaire de contact et la newsletter, finalités, durée de conservation, droits des personnes (RGPD), contact.</p></div></section>')
page("plan-du-site.html","Plan du site","Plan du site ASE.",'<section><div class="w"><ul>'+"".join(f'<li><a href="{h}">{t}</a></li>' for h,t in NAV+[("mentions-legales.html","Mentions légales"),("confidentialite.html","Politique de confidentialité")])+'</ul></div></section>')
