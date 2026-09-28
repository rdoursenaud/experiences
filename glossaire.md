---
title: Glossaire Technique
subject: Glossaire
abbreviations:
  README: null # Prevents AD replacement
  SDIG: null  # Prevents SDI replacement
---

# Glossaire Technique

Ce glossaire regroupe les définitions des sigles, {term}`protocoles <Protocole>` et concepts techniques utilisés dans mes projets de R&D, d’audiovisuel et d’infrastructure.

## Électronique
:::{glossary}
1-Wire
: Un bus conçu par Dallas Semiconductor qui permet de connecter des composants avec seulement deux fils.  
[Source](https://fr.wikipedia.org/wiki/1-Wire)

Adafruit Matrix Portal M4
: Afficheur matriciel RGB connecté à Internet, piloté par {term}`CircuitPython`. Conçu pour l’affichage dynamique de données en temps réel sur des panneaux de LED, il combine la simplicité de la programmation Python avec la réactivité d’un microcontrôleur dédié.  
[Documentation](https://learn.adafruit.com/adafruit-matrixportal-m4/overview)  
[Boutique](https://www.adafruit.com/product/4745)

CircuitPython
: Un langage de programmation s’appuyant sur {term}`MicroPython`, conçu pour faciliter l’apprentissage de la programmation et l’expérimentation sur des cartes à faible coût équipées de microcontrôleurs. 
[Site officiel](https://circuitpython.org)

Embarqué
: Domaine technique désignant des systèmes informatiques spécialisés, intégrés dans un appareil plus large (électroménager, véhicule, instrument de musique, etc.) pour en contrôler le fonctionnement. Contrairement à un ordinateur généraliste, un système embarqué est conçu pour une tâche spécifique, avec des contraintes fortes de temps réel, de consommation énergétique et/ou de fiabilité.

MicroPython
: Une implémentation du langage de programmation {term}`Libre <Logiciel Libre>`, sous licence MIT, de {term}`Python`, adapté au monde des microcontrôleurs, écrite par l’ingénieur australien Damien George pour l’architecture STM32F405 (ARM Cortex-M) et portée ensuite sur de nombreuses autres architectures.  
[Source](https://fr.wikipedia.org/wiki/MicroPython)  
[Site officiel](https://micropython.org)
:::

## Informatique, Sécurité & Développement

:::{glossary}
Alpha
: Version nommée comme la première lettre de l’alphabet grec, elle n’est pas censée être accessible à un large public : c’est une version interne. C’est la première phase de développement concret du logiciel après la programmation de l’application. Généralement, un produit en test alpha — on utilise couramment le terme anglais alpha-test — n’a pas toutes les fonctionnalités prévues dans le produit final, contrairement à un produit en test bêta qui devrait être complet. L’alpha est donc dépourvue de certaines fonctionnalités, et contient un nombre de bugs encore important.  
Le but de cette phase est d’implémenter toutes les fonctionnalités du logiciel final, et la version correspondante est traitée à l’intérieur même du studio de développement.  
Toutefois, dans l’écosystème du {term}`Logiciel Libre` et des méthodologies agiles, il est courant de publier des versions Alpha en accès public (Open Alpha) pour recueillir des retours précoces de la communauté. Dans ce cas elle désigne un logiciel qui n’est pas fonctionnellement complet et peut présenter des risques (bugs majeurs).  
[Source](https://fr.wikipedia.org/wiki/Version_d%27un_logiciel)

Android
: Un système d’exploitation mobile {term}`open source` fondé sur le noyau {term}`Linux` et développé par un consortium d’entreprises, l’Open Handset Alliance, sponsorisé par Google.  
[Source](https://fr.wikipedia.org/wiki/Android)  
[Site officiel](https://www.openhandsetalliance.com)  
[Site commercial](https://www.android.com)

Apple macOS
: Un système d’exploitation partiellement propriétaire annoncé par Apple en 1998 et commercialisé depuis 2001.  
[Source](https://fr.wikipedia.org/wiki/MacOS)  
[Site officiel](https://www.apple.com/fr/os/macos/)

Arch Linux
: Une distribution GNU/Linux créée par Judd Vinet qui met l’accent sur la simplicité de conception - selon le principe KISS.  
[Source](https://fr.wikipedia.org/wiki/Arch_Linux)  
[Site officiel](https://archlinux.org)

Assembleur
: Le langage de plus bas niveau qui représente le langage machine sous une forme lisible par un humain. Les combinaisons de bits du langage machine sont représentées par des symboles dits « mnémoniques », c’est-à-dire faciles à retenir. Le programme assembleur convertit ces mnémoniques en langage machine, ainsi que les valeurs en binaire et les libellés d’emplacements en adresses, en vue de créer par exemple un fichier objet ou un fichier exécutable.  
[Source](https://fr.wikipedia.org/wiki/Assembleur)

Base64
: Un codage de l’information utilisant 64 caractères, choisis pour être disponibles sur la majorité des systèmes. Défini en tant qu’encodage MIME dans la RFC 2045, il est principalement utilisé pour la transmission de messages (courrier électronique et forums Usenet) sur Internet. Il est par ailleurs défini en propre dans la RFC 4648.  
[Source](https://fr.wikipedia.org/wiki/Base64)

Bibliothèque
: Une collection de routines, qui peuvent être déjà compilées et prêtes à être utilisées par des programmes. Les bibliothèques sont enregistrées dans des fichiers semblables, voire identiques aux fichiers de programmes, sous la forme d’une collection de fichiers de code objet rassemblés accompagnée d’un index permettant de retrouver facilement chaque routine. Le mot « librairie » est souvent utilisé pour désigner une bibliothèque logicielle. Il s’agit d’un anglicisme dû au faux-ami library.  
Les bibliothèques sont apparues dans les années 1950, et sont devenues un sujet incontournable de programmation. Elles sont utilisées pour réaliser des interfaces de programmation, des framework, des plugins ainsi que des langages de programmation. Les routines contenues dans les bibliothèques sont typiquement en rapport avec des opérations fréquentes en programmation : manipulation des interfaces utilisateur, manipulation des bases de données ou calculs mathématiques.  
Les bibliothèques sont manipulées par l’éditeur de lien et le système d’exploitation. Les manipulations sont différentes suivant que la bibliothèque est statique ou partagée. Les emplacements et les noms des bibliothèques varient selon les systèmes d’exploitation.  
[Source](https://fr.wikipedia.org/wiki/Biblioth%C3%A8que_logicielle)

Bluetooth
: Une norme de télécommunications permettant l’échange bidirectionnel de données à courte distance en utilisant des ondes radio UHF. Son but est de simplifier les connexions entre des appareils électroniques proches en supprimant des liaisons filaires.  
[Source](https://fr.wikipedia.org/wiki/Bluetooth)  
[Site officiel: Bluetooth SIG](https://www.bluetooth.com)

bolt
: Un démon système, écrit par Christian Kellner, conçu pour gérer les périphériques {term}`Thunderbolt`™ sous {term}`Linux` facilement et de manière sécurisée.
[Code source](https://gitlab.freedesktop.org/bolt/bolt)
[Blog de Christian Kellner](https://christian.kellner.me)

C
: Un langage de programmation impératif, généraliste et de bas niveau. Inventé au début des années 1970 par Dennis Ritchie pour réécrire Unix, il est encore largement utilisé aujourd’hui. Sa syntaxe et ses fondements, formalisés par le célèbre livre **K&R** (*The C Programming Language*), offrent au développeur une marge de contrôle importante sur la machine.  
[Source](https://fr.wikipedia.org/wiki/C_(langage))

COSMIC
: Un environnement de bureau et compositeur Wayland {term}`Libre <Logiciel Libre>` pour Linux. Initialement une version modifiée de GNOME conçue pour Pop!_OS, il a ensuite été entièrement réécrit comme environnement de bureau autonome en utilisant le langage Rust et le toolkit Iced. Il prend en charge l’empilement et le pavage des fenêtres, et chaque fenêtre peut fonctionner comme un onglet.  
[Source](https://en.wikipedia.org/wiki/COSMIC_desktop)  
[Site officiel](https://system76.com/cosmic)

Cython
: Extensions {term}`C` pour {term}`Python`.  
Un compilateur static optimisant pour le language de programmation {term}`Python` et le langage de programmation étendu Cython (Basé sur Pyrex). Il permet de rendre l’écriture d’extensions {term}`C` pour {term}`Python` aussi facile que {term}`Python` lui-même.  
[Site officiel](https://cython.org)

cython-hidapi
: Une interface de liaison écrite en (*wrapper*) {term}`Python` utilisant {term}`Cython` pour accéder à la {term}`bibliothèque` {term}`hidapi`. Initialement développée par Trezor, un acteur majeur des portefeuilles matériels pour crytomonnaies, cet outil a été conçu pour garantir des communications matérielles sécurisées et fiables. Il permet aux développeurs {term}`Python` d’interagir directement avec les périphériques HID (claviers, souris, contrôleurs ou clés de sécurité) sans écrire de code {term}`C` ou de pilotes {term}`noyau <Kernel>`, tout en bénéficiant des performances et de la sécurité éprouvées dans l’industrie de la cryptographie.  
[Code Source](https://github.com/trezor/cython-hidapi)

Dear ImGui
: Une interface graphique pour C++ exempte de superflu (bloat-free) et avec un minimum de dépendances. Basée sur le principe du mode immédiat (redessin complet de l’interface à chaque image), elle est particulièrement adaptée aux outils de développement, au débogage et aux applications temps réel.  
[Site officiel](https://www.dearimgui.com)  
[Code Source](https://github.com/ocornut/imgui)  
[Principe](https://en.wikipedia.org/wiki/Immediate_mode_(computer_graphics))

Dear PyGui
: Une boîte à outils d’interface graphique rapide et puissante pour Python, avec un minimum de dépendances. Elle agit comme une interface de liaison (*wrapper*) performante autour de la {term}`bibliothèque` {term}`Dear ImGui`, offrant les avantages du mode immédiat dans l’écosystème Python.  
[Code Source](https://github.com/hoffstadt/DearPyGui)  
[Principe](https://en.wikipedia.org/wiki/Immediate_mode_(computer_graphics))

Debian
: Une distribution Linux, composée presque exclusivement de {term}`Logiciels Libres <Logiciel Libre>`.  
[Source](https://fr.wikipedia.org/wiki/Debian)  
[Site officiel](https://www.debian.org)

Dissector
: Un dissecteur est un greffon (*plugin*) ou une routine interne de {term}`Wireshark` qui analyse (*parse*) un {term}`protocole` réseau spécifique, séparant les octets de paquets bruts en une structure d’arbre hiérarchique, lisible par l’humain, au sein de l’interface graphique.
[Documentation](https://www.wireshark.org/docs/wsdg_html_chunked/ChDissectAdd.html)
(*L’auteur de ces pages a [contribué](https://github.com/wireshark/wireshark/commits?author=rdoursenaud) le dissecteur {term}`HiQnet` officiellement intégré depuis 2014. C’est aussi à cette occasion qu’il a introduit son premier bug de sécurité et obtenu sa première CVE ; Oups.*)

Django
: Un framework web {term}`open source` en {term}`Python`. Il a pour but de rendre le développement d’applications web simple et basé sur la réutilisation de code. Développé en 2003 pour le journal local de Lawrence, Django a été publié sous licence BSD à partir de juillet 2005.  
[Source](https://fr.wikipedia.org/wiki/Django_(framework))  
[Site officiel](https://www.djangoproject.com/)

Docker
: Une {term}`bibliothèque` et une plateforme logicielle permettant de faire tourner certaines applications dans des conteneurs.  
[Source](https://fr.wikipedia.org/wiki/Docker_(logiciel))

Dolibarr
: Dolibarr ERP/CRM est un progiciel de gestion intégré et gestion de la relation client {term}`open source` pour les entreprises de toutes tailles, de la PME au grand groupe mais aussi pour les indépendants, auto-entrepreneurs ou les associations.  
Il est développé en PHP.
[Source](https://fr.wikipedia.org/wiki/Dolibarr)  
[Site officiel](https://www.dolibarr.org)  
[Code source](https://github.com/dolibarr)  
*(L’auteur de ces pages est [utilisateur](https://lists.nongnu.org/archive/cgi-bin/namazu.cgi?query=rdoursenaud&submit=Search%21&idxname=dolibarr-user&max=20&result=normal&sort=date) depuis 2007 et [a](https://lists.nongnu.org/archive/cgi-bin/namazu.cgi?query=rdoursenaud&submit=Search%21&idxname=dolibarr-bugtrack&max=20&result=normal&sort=date) [été](https://lists.nongnu.org/archive/cgi-bin/namazu.cgi?query=rdoursenaud&submit=Search%21&idxname=dolibarr-dev&max=20&result=normal&sort=date) [un](https://github.com/Dolibarr/dolibarr/issues?q=is%3Aissue%20state%3Aclosed%20rdoursenaud) [important](https://github.com/Dolibarr/dolibarr/pulls?q=is%3Apr+state%3Aclosed+rdoursenaud) [contributeur](https://github.com/Dolibarr/dolibarr/commits?author=rdoursenaud) du 5 juin 2012 à 2018, release manager à partir de 2014 et membre de l’association. Notre société [GPC.solutions](https://gpcsolutions.fr) a été Dolibarr Preferred Partner à partir de juin 2013 et organisatrice d’un DevCamp à Pau en 2015.)*

Doxygen
: Un générateur de documentation sous licence {term}`Libre <Logiciel Libre>` capable de produire une documentation logicielle à partir du code source d’un programme. Pour cela, il tient compte de la syntaxe du langage dans lequel est écrit le code source, ainsi que des commentaires s’ils sont écrits dans un format particulier.  
[Source](https://fr.wikipedia.org/wiki/Doxygen)  
[Site officiel](https://www.doxygen.org)

Ethernet
: Un {term}`protocole` de communication utilisé pour les réseaux informatiques filaires, exploitant la commutation de paquets. Il réalise les fonctions de la couche physique et de la couche liaison de données du modèle OSI. C’est une norme internationale ISO/IEC/IEEE 8802-3.  
[Source](https://fr.wikipedia.org/wiki/Ethernet)

FireWire
: Une norme d’interface pour un bus série permettant des communications à grande vitesse et le transfert isochrone de données en temps réel. Elle a été développée à la fin des années 1980 et au début des années 1990 par Apple en collaboration avec plusieurs entreprises, principalement Sony et Panasonic. Elle est le plus souvent connue sous le nom de FireWire (Apple), bien qu’il existe d’autres noms de marque tels que i.LINK (Sony) et Lynx (Texas Instruments).  
Le câble en cuivre utilisé dans sa mise en œuvre la plus courante peut mesurer jusqu’à 4,5 mètres (15 pieds) de long. L’alimentation électrique et les données sont transportées par ce câble, permettant ainsi aux appareils nécessitant une alimentation modérée de fonctionner sans alimentation électrique séparée. FireWire est également disponible en versions Cat 5 et fibre optique.  
L’interface 1394 est comparable à l’USB, bien que l’USB a été développé ultérieurement et a acquis une part de marché beaucoup plus importante. Contrairement à l’USB qui requiert un contrôleur hôte, l’IEEE 1394 est géré de manière coopérative par les appareils connectés.  
[Source](https://fr.wikipedia.org/wiki/FireWire)

Flask
: Un micro framework {term}`open-source <open source>` de développement web en {term}`Python`. Il est classé comme microframework car il est très léger. Flask a pour objectif de garder un noyau simple mais extensible. Il n’intègre pas de système d’authentification, pas de couche d’abstraction de base de données, ni d’outil de validation de formulaires. Cependant, de nombreuses extensions permettent d’ajouter facilement des fonctionnalités. Il est distribué sous licence BSD.  
[Source](https://fr.wikipedia.org/wiki/Flask_(framework))  
[Site officiel](https://flask.palletsprojects.com)

G Suite
: Voir {term}`Google Workspace`.

gettext
: gettext est la {term}`bibliothèque` logicielle du projet GNU qui sert à l'internationalisation de logiciels (i18n). Elle est couramment utilisée pour écrire des programmes multilingues.  
[Source](https://fr.wikipedia.org/wiki/GNU_gettext)  
[Site officiel](https://www.gnu.org/software/gettext/)

Git
: Git est un logiciel de gestion de versions décentralisé. C’est un {term}`Logiciel Libre` et gratuit, créé en 2005 par Linus Torvalds, auteur du noyau {term}`Linux`, et distribué selon les termes de la licence publique générale GNU version 2. Git est maintenu par Junio Hamano depuis juillet 2005.  
Depuis les années 2010, il s’agit du logiciel de gestion de versions le plus populaire dans le développement logiciel et web, qui est utilisé par 12 millions de personnes, sur tous les environnements ({term}`Microsoft Windows`, {term}`macOS <Apple macOS>`, {term}`Linux`). Git est aussi le système à la base du célèbre site web GitHub, le plus important hébergeur de code informatique.
[Source](https://fr.wikipedia.org/wiki/Git)  
[Site officiel](https://git-scm.com)

GitHub
: Un service web d’hébergement et de gestion de développement de logiciels, utilisant le logiciel de gestion de versions {term}`Git`. Ce site est développé en Ruby on Rails et Erlang par Chris Wanstrath, PJ Hyett et Tom Preston-Werner. GitHub propose des comptes professionnels payants, ainsi que des comptes gratuits pour les projets de {term}`Logiciels Libres <Logiciel Libre>`. Dans le giron de Microsoft depuis son rachat le 4 juin 2018.  
[Source](https://fr.wikipedia.org/wiki/GitHub)  
[Site officiel](https://github.com)

GitLab
: Un {term}`Logiciel Libre` de forge basé sur {term}`Git` proposant les fonctionnalités de wiki, un système de suivi des bugs, l’intégration continue et la livraison continue. Développé par GitLab Inc. et créé par Dmitriy Zaporozhets et par Valery Sizov, le logiciel est utilisé par plusieurs grandes entreprises informatique, dont IBM, Sony, le Centre de recherche de Jülich, la NASA, Alibaba, Oracle, Invincea, O’Reilly Media, Leibniz Rechenzentrum, le CERN, European XFEL, la GNOME Foundation, KDE, Boeing, Autodata, SpaceX, Symbio et Altares.  
[Source](https://fr.wikipedia.org/wiki/GitLab)  
[Site officiel](https://about.gitlab.com)

GObject
: Une interface de programmation et une {term}`bibliothèque` logicielle multiplate-forme publiée sous licence {term}`Libre <Logiciel Libre>` (LGPL), qui offre la possibilité de manipuler des objets en langage de programmation {term}`C`, ainsi qu'une palette d'objets élémentaires. Elle peut être utilisée dans d'autres langages de programmation.  
[Source](https://fr.wikipedia.org/wiki/GObject)

Google App Engine
: Google App Engine (GAE) est une plateforme de conception et d’hébergement d’applications web basée sur les serveurs de Google.  
[Source](https://fr.wikipedia.org/wiki/Google_App_Engine)  
[Site officiel](https://cloud.google.com/appengine)

Google Apps
: Voir {term}`Google Workspace`.

Google Cloud Datastore
: Était un service de base de données NoSQL géré sur la GCP, aujourd’hui remplacé par Google Cloud Firestore en mode de compatibilité Datastore ; Une base de données de documents NoSQL conçue pour le scaling automatique, les hautes performances et la convivialité de développement des applications.  
[Documentation](https://docs.cloud.google.com/datastore/docs/concepts/overview?hl=fr)

Google Cloud SQL
: Service de base de données relationnelle entièrement géré pour {term}`PostgreSQL`, {term}`MySQL` et SQL Server.  
[Site officiel](https://cloud.google.com/sql)

Google Compute Engine
: C’est le composant IaaS de GCP.  
[Source](https://en.wikipedia.org/wiki/Google_Compute_Engine)  
[Site officiel](https://cloud.google.com/products/compute)

Google Gmail Gadgets
: Étaient des mini-applications intégrées à l’interface de Gmail, permettant par exemple d’afficher une calculatrice, des outils de recherche ou des modules contextuels via des liens XML, des iframes et du {term}`JavaScript` sandboxé

Google Workspace
: (Anciennement Google Apps puis Google Apps for Work et G-Suite) Une suite d’outils et de logiciels de productivité de type {term}`Cloud` computing et de groupware destinée aux professionnels, proposée par Google sous la forme d’un abonnement.  
La suite inclut les applications Web de Google les plus courantes, comme Gmail, Google Chat, Google Meet, Google Agenda, Currents (anciennement Google+) jusqu’à sa disparition en 2022, Google Drive, Google Docs, Sheets, Slides, Forms et Google Sites. Google Workspace inclut des fonctionnalités répondant aux besoins des entreprises, comme les adresses de courrier électronique personnalisées (\@votre_entreprise.fr), un espace de stockage de 30 Go pour les documents et les courriels, ainsi qu’une assistance 24h/24, 7j/7 par téléphone et par messagerie électronique. Contrairement aux logiciels de productivité standard qui stockent les données sur des serveurs classiques dans les locaux des entreprises, cette solution de Cloud computing stocke les données sur le réseau de centres de données sécurisés de Google.  
Selon Google, plus de 5 millions d’entreprises dans le monde utilisent Google Workspace en 2014, parmi lesquelles figurent 60 % des entreprises Fortune 500. En 2018, Google Workspace est le second acteur de logiciels bureautique cloud, avec 19 % de parts de marché, derrière Microsoft 365, avec 65 %.  
[Source](https://fr.wikipedia.org/wiki/Google_Workspace)  
[Site officiel](https://workspace.google.com)

GTK+
: Un ensemble de {term}`bibliothèques <Bibliothèque>` logicielles, c’est-à-dire un ensemble de fonctions permettant de réaliser des interfaces graphiques. Cette {term}`bibliothèque` a été développée originellement pour les besoins du logiciel de traitement d’images GIMP. GTK est maintenant utilisé dans de nombreux projets, dont les environnements de bureau GNOME, Xfce, Lxde et ROX.  
[Source](https://fr.wikipedia.org/wiki/GTK_(bo%C3%AEte_%C3%A0_outils))  
[Site officiel](https://www.gtk.org)

hidapi
: Une {term}`bibliothèque` multiplateforme faisant partie de libusb ciblant les périphériques HID et Bluetooth-HID.  
[Code source](https://github.com/libusb/hidapi)

Iced
: Une {term}`bibliothèque` graphique (GUI) multiplateforme pour Rust, axée sur la simplicité et la sûreté du typage.  
[Site officiel](https://iced.rs)

InboxSDK
: Une {term}`bibliothèque` {term}`JavaScript` de haut niveau utilisée par les développeurs pour créer des applications basées sur des extensions de navigateur, directement intégrées dans l’interface utilisateur de Gmail.  
[Code source](https://github.com/InboxSDK/InboxSDK)

Introspection
: La capacité d'un programme à examiner son propre état.  
[Source](https://fr.wikipedia.org/wiki/R%C3%A9flexion_(informatique))

iOS
: Un système d’exploitation mobile créé et développé par la société américaine Apple exclusivement pour ses produits. Il gère de nombreux appareils tels que l’iPhone, l’iPod touch et fonctionnait sur les iPad jusqu’en 2019. Il s’agit du deuxième système d’exploitation mobile le plus installé au monde, après {term}`Android`. Basé sur le noyau XNU comme Darwin ou macOS, il constitue la base de trois autres systèmes d’exploitation : iPadOS, tvOS, watchOS. Il s’agit d’un logiciel propriétaire, bien que certaines parties soient en {term}`open source` sous la licence Apple Public Source License et d’autres licences.  
[Source](https://fr.wikipedia.org/wiki/IOS)  
[Site officiel](https://www.apple.com/fr/os/ios/)

iptables
: Un {term}`Logiciel Libre` de l’espace utilisateur Linux grâce auquel l’administrateur système peut configurer les chaînes et règles dans le pare-feu en espace noyau.  
[Source](https://fr.wikipedia.org/wiki/Iptables)

JavaScript
: Langage de script multi-paradigme, standardisé par l’ECMA (norme ECMAScript). Initialement conçu pour l’interactivité dans les navigateurs web, il est désormais omniprésent côté serveur (Node.js) et dans l’automatisation de tâches. Il forme, avec HTML et CSS, le socle technologique du développement web moderne.  
[Source](https://fr.wikipedia.org/wiki/JavaScript)

Kernel
: Noyau de système d’exploitation. Une des parties fondamentales de certains systèmes d’exploitation. Il gère les ressources de l’ordinateur et permet aux différents composants — matériels et logiciels — de communiquer entre eux.  
[Source](https://fr.wikipedia.org/wiki/Noyau_de_syst%C3%A8me_d'exploitation)

Kivy
: Une {term}`bibliothèque` {term}`Libre <Logiciel Libre>` et {term}`open source` pour {term}`Python`, utile pour créer des applications tactiles pourvues d’une interface utilisateur naturelle. Cette {term}`bibliothèque` fonctionne sur {term}`Android`, {term}`iOS`, GNU/{term}`Linux`, {term}`OS X <Apple macOS>` et {term}`Windows <Microsoft Windows>`. Elle est distribuée gratuitement et sous licence MIT.  
[Source](https://fr.wikipedia.org/wiki/Kivy)  
[Site officiel](https://kivy.org)

Linux
: Un système d’exploitation {term}`Libre <Logiciel Libre>` de type UNIX, basé sur le noyau Linux créé en 1991 par Linus Torvalds.  
[Source](https://fr.wikipedia.org/wiki/Noyau_Linux)

MariaDB
: Un système de gestion de base de données édité sous licence GPL. Il s’agit d’un dérivé communautaire de {term}`MySQL` : la gouvernance du projet est assurée par la fondation MariaDB, et sa maintenance par la société MariaDB plc, successeur de Monty Program AB. Cette gouvernance confère au logiciel l’assurance de rester {term}`Libre <Logiciel Libre>`.  
[Source](https://fr.wikipedia.org/wiki/MariaDB)  
[Site officiel](https://mariadb.org)

Markdown
: Un langage de balisage léger créé en 2004 par John Gruber, avec l’aide d’Aaron Swartz, avec l’objectif d’offrir une syntaxe, facile à lire et à écrire, en l’état, sans formatage. Devenu le standard de facto pour la rédaction de documentation technique (fichiers README, commentaires de code, forums), il est facilement convertible en HTML ou en PDF.  
[Source](https://fr.wikipedia.org/wiki/Markdown)

Mercurial
: Un {term}`Logiciel Libre` de gestion de versions décentralisé disponible sur la plupart des systèmes Unix et {term}`Microsoft Windows` écrit en {term}`Python` et {term}`Rust`.  
[Source](https://fr.wikipedia.org/wiki/Mercurial)  
[Site officiel](https://www.mercurial-scm.org)

Microsoft Exchange
: Un groupware (logiciel de groupe de travail) pour serveur de messagerie électronique créé par Microsoft, pour concurrencer Lotus Domino d’IBM. Il est très utilisé dans les entreprises, 52 % du marché des plates-formes de messagerie et de collaboration d’entreprise en 2008. C’est un produit de la gamme des serveurs Microsoft, conçu pour la messagerie électronique, mais aussi pour la gestion d’agenda, de contacts et de tâches, qui assure le stockage des informations et permet des accès à partir de clients mobiles (Outlook Mobile Access, Exchange Active Server Sync) et de clients web (navigateurs tels que Internet Explorer, Mozilla Firefox, Safari).  
[Source](https://fr.wikipedia.org/wiki/Microsoft_Exchange_Server)

Microsoft Windows
: Une gamme de systèmes d’exploitation propriétaires développés par la société américaine Microsoft. Elle se décline en plusieurs produits : pour ordinateurs personnels, pour serveurs et pour systèmes {term}`embarqués <Embarqué>`.  
[Source](https://fr.wikipedia.org/wiki/Microsoft_Windows)  
[Site officiel](https://www.microsoft.com/fr-fr/windows)

Mido
: Objets MIDI pour {term}`Python`. Une {term}`bibliothèque` pour travailler avec des ports, messages et fichiers MIDI 1.0.
[Documentation](https://mido.readthedocs.io)  
[Distribution](https://pypi.org/project/mido/)  
[Code source](https://github.com/mido)  
*(L’auteur de ces pages est co-mainteneur du projet depuis 2023 aux côtés de [Radovan Bast](https://github.com/bast) et de son créateur, [Ole Martin Bjørndalen](https://github.com/olemb).)*

MySQL
: Un système de gestion de bases de données relationnelles (SGBDR). Il est distribué sous une double licence GPL et propriétaire. Il fait partie des logiciels de gestion de base de données les plus utilisés au monde, autant par le grand public que par des professionnels, en concurrence avec Oracle, {term}`PostgreSQL` et Microsoft SQL Server.  
[Source](https://fr.wikipedia.org/wiki/MySQL)  
[Site officiel](https://www.mysql.com)

Nuitka
: Un compilateur {term}`Python` optimisant, écrit en {term}`Python`, qui crée des exécutables natifs fonctionnant sans installateur séparé. Les fichiers de données peuvent être inclus directement dans le binaire ou placés à côté. Entièrement compatible avec {term}`Python` 3 (versions 3.4 à 3.14) et {term}`Python` 2 (2.6, 2.7), il fonctionne sur {term}`Windows <Microsoft Windows>`, {term}`macOS <Apple macOS>`, {term}`Linux` et plus — essentiellement partout où {term}`Python` est lui-même compatible avec votre système.  
[Source](https://en.wikipedia.org/wiki/Nuitka)
[Site officiel](https://nuitka.net)

Oracle VirtualBox
: Un {term}`Logiciel Libre` de virtualisation créé par la société Innotek rachetée par Sun Microsystems et aujourd’hui publié par Oracle.  
[Source](https://fr.wikipedia.org/wiki/Oracle_VM_VirtualBox)  
[Site officiel](https://www.virtualbox.org)

PostgreSQL
: Un système de gestion de base de données relationnelle et objet (SGBDRO). C’est un outil {term}`Libre <Logiciel Libre>` disponible selon les termes d’une licence de type BSD mettant l’accent sur l’extensibilité et la conformité avec SQL. Il prend en charge les transactions avec les propriétés ACID et offre des fonctionnalités avancées telles que les vues automatiquement mises à jour, les vues matérialisées, les déclencheurs, les clés étrangères et les procédures stockées.  
[Source](https://fr.wikipedia.org/wiki/PostgreSQL)  
[Site officiel](https://www.postgresql.org/)

PowerShell
: Un langage de script et une interface en ligne de commande développés par Microsoft pour l’administration système. Contrairement aux shells traditionnels qui traitent du texte, PowerShell est fondé sur la programmation orientée objet et manipule des objets .NET, ce qui en fait un outil puissant pour l’automatisation et la gestion des environnements Windows et désormais multiplateformes avec PowerShell Core.  
[Source](https://fr.wikipedia.org/wiki/Windows_PowerShell)

Proxmox
: Une plateforme de virtualisation {term}`Libre <Logiciel Libre>` basée sur l’hyperviseur Linux KVM qui offre aussi des conteneurs avec LXC.  
[Source](https://fr.wikipedia.org/wiki/Proxmox_Virtual_Environnement)  
[Site officiel](https://www.proxmox.com)

Pygame
: Une {term}`bibliothèque` {term}`libre <Logiciel Libre>` multiplate-forme qui facilite le développement de jeux vidéo temps réel avec le langage de programmation {term}`Python`.  
[Source](https://fr.wikipedia.org/wiki/Pygame)  
[Site officiel](https://www.pygame.org)

PyGObject
: Une bibliothèque {term}`Python` permettant la création d'interfaces graphiques utilisant la {term}`bibliothèque` GTK 3 via l’{term}`Introspection` {term}`GObject`.  
[Source](https://fr.wikipedia.org/wiki/PyGTK)

PyInstaller
: Un outil qui empaquette une application {term}`Python` et toutes ses dépendances en un seul paquet exécutable. L’utilisateur peut lancer l’application sans avoir besoin d’installer un interpréteur {term}`Python` ni aucun module externe. PyInstaller prend en charge {term}`Python` 3.8 et versions ultérieures, et empaquette correctement de nombreuses {term}`bibliothèques <Bibliothèque>` majeures telles que NumPy, Matplotlib, PyQt, wxPython, etc. Il est testé et fonctionnel sur {term}`Windows <Microsoft Windows>`, {term}`macOS <Apple macOS>` et {term}`Linux`.  
[Site officiel](https://pyinstaller.org)  

PySide
: Un binding qui permet de lier le langage {term}`Python` avec la {term}`bibliothèque` {term}`Qt`, disponible à l’origine en C++. Il constitue une alternative aux interfaces Tkinter.  
PySide se distingue de PyQt, le binding historique, par le fait qu’il est disponible sous licence LGPL, c’est d’ailleurs ce qui a déclenché son développement.  
PySide est un projet lancé et soutenu jusque fin 2011 par Nokia.  
À partir de la version 1.0.8, PySide peut prendre en charge {term}`Python` 3.  
[Source](https://fr.wikipedia.org/wiki/PySide)

Python
: Un langage de programmation interprété, multiparadigme et multiplateformes. Il favorise la programmation impérative structurée, fonctionnelle et orientée objet. Il est doté d’un typage dynamique fort, d’une gestion automatique de la mémoire par ramasse-miettes et d’un système de gestion d’exceptions.  
[Source](https://fr.wikipedia.org/wiki/Python_(langage))  
[Site officiel](https://www.python.org)

QEMU
: Un {term}`Logiciel Libre` de machine virtuelle, pouvant émuler un processeur et, plus généralement, une architecture différente si besoin. Il permet d’exécuter un ou plusieurs systèmes d’exploitation via les hyperviseurs KVM et Xen, ou seulement des binaires, dans l’environnement d’un système d’exploitation déjà installé sur la machine.  
[Source](https://fr.wikipedia.org/wiki/QEMU)

Qt
: Une API orientée objet et développée en C++, conjointement par The Qt Company et Qt Project. Qt offre des composants d’interface graphique (widgets), d’accès aux données, de connexions réseaux, de gestion des fils d’exécution, d’analyse XML, etc. ; par certains aspects, elle ressemble à un framework lorsqu’on l’utilise pour concevoir des interfaces graphiques ou que l’on conçoit l’architecture de son application en utilisant les mécanismes des signaux et slots par exemple.  
[Source](https://fr.wikipedia.org/wiki/Qt)  
[Site officiel](https://www.qt.io)

Reverse-engineering
: Voir {term}`Rétro-ingénierie`.

Rétro-ingénierie
: Processus d’analyse d’un système (matériel ou logiciel) pour en comprendre le fonctionnement interne, souvent dans un but d’interopérabilité, de maintenance ou de création de pilotes {term}`Libres <Logiciel Libre>`. Dans ma pratique, cela est éthique et vise à libérer la longévité du matériel tout en élargissant ma culture technique et en affinant mes intuitions.

Rust
: Un langage de programmation compilé multi-paradigme qui met l’accent sur la performance, la sûreté des types et la concurrence. Il garantit la sûreté des accès en mémoire, ce qui signifie que toutes les références pointent vers une mémoire valide, sans nécessiter l’utilisation de techniques de gestion de la mémoire automatisée telles que le ramasse-miettes.  
[Source](https://fr.wikipedia.org/wiki/Rust_(langage))

Security by Design
: Philosophie de conception de systèmes où la sécurité n’est pas une couche ajoutée a posteriori, mais une contrainte fondamentale intégrée dès l’architecture initiale (privilège minimum, défense en profondeur).

Sphinx
: Un générateur de documentation {term}`Libre <Logiciel Libre>`.  
[Source](https://fr.wikipedia.org/wiki/Sphinx_(g%C3%A9n%C3%A9rateur_de_documentation))  
[Site officiel](https://www.sphinx-doc.org)

SQLite
: Une {term}`bibliothèque` écrite en langage {term}`C` qui propose un moteur de base de données relationnelle accessible par le langage SQL. SQLite implémente en grande partie le standard SQL-92 et des propriétés ACID.  
[Source](https://fr.wikipedia.org/wiki/SQLite)  
[Site officiel](https://sqlite.org)

Telnet
: Un {term}`protocole` utilisé sur tout réseau TCP/IP, permettant de communiquer avec un serveur distant en échangeant des lignes de texte et en recevant des réponses également sous forme de texte.  
Créé en 1969, telnet est un moyen de communication très généraliste et bi-directionnel. Il appartient à la couche application du modèle OSI et du modèle ARPA. Il est normalisé par l’IETF (RFC 15, 854 et 855).  
Il était notamment utilisé pour administrer des serveurs Unix distant ou de l’équipement réseau, avant de tomber en désuétude par défaut de sécurisation (le texte étant échangé en clair) et l’adoption de SSH.  
[Source](https://fr.wikipedia.org/wiki/Telnet)

Thunderbolt
: Un format de connexion informatique conçu par Intel, dont les travaux ont débuté en 2007, sous le nom de code Light Peak. Cette connexion devait utiliser à terme la fibre optique, bien que ses premières implémentations utilisent des fils de cuivre standards. Cette interface permet l’utilisation des {term}`protocoles <Protocole>` DisplayPort et PCI Express dans la même interface. Le connecteur Mini DisplayPort, qui était notamment déjà présent sur les ordinateurs d’Apple, a été choisi comme interface standard pour Thunderbolt. La version 3 du Thunderbolt bascule sur le connecteur USB de type C, et permet donc en plus l’utilisation du {term}`protocole` USB standard sur la même interface. Cette version entérine l’utilisation du cuivre, car l’utilisation du câble comme alimentation électrique est aussi un élément important de cette interface.  
Les premiers ordinateurs qui l’utilisent sont, par ordre chronologique, les MacBook Pro, les iMac, les MacBook ainsi que les Mac mini du fabricant Apple. Ils utilisent les processeurs Intel Core i5 ou Core i7 fonctionnant sur les microarchitectures Sandy-Bridge, Ivy Bridge, Haswell et Skylake.  
Les connecteurs Thunderbolt 1 et 2 sont entièrement compatibles avec la norme Mini DisplayPort afin de pouvoir connecter des moniteurs externes.  
[Source](https://fr.wikipedia.org/wiki/Thunderbolt_(interface))  
[Thunderbolt Technology Community](https://www.thunderbolttechnology.net)

tokio
: Un environnement d’exécution (*runtime*) asynchrone pour le langage de programmation {term}`Rust`. Il fournit les blocs de constructions nécessaires à l’écriture d’applications réseau hautes performances et concurrentes. Offrant une grande flexibilité, il permet de cibler une large gamme de systèmes : des serveurs massifs multicœurs jusqu’aux petits appareils {term}`embarqués <Embarqué>` aux ressources limitées.
[Site officiel](https://tokio.rs)  
[Documentation](https://docs.rs/tokio)

Twisted
: Un moteur réseau piloté par événements, écrit en {term}`Python`. Fondé sur le modèle de réacteur (*Reactor Pattern*), il permet de gérer des milliers de connexions simultanées et de construire des applications réseau complexes (serveurs TCP/UDP, clients, {term}`protocoles <Protocole>` personnalisés) sans bloquer l’exécution. Sous licence {term}`open source` MIT, il est l’un des outils les plus anciens et les plus robustes de l’écosystème {term}`Python`.  
[Source](https://fr.wikipedia.org/wiki/Twisted)  
[Site officiel](https://twisted.org/)

Vyatta
: Une filiale de la société de télécommunications américaine AT&T qui fournit des routeurs virtuels logiciels, des pare-feu virtuels et des produits VPN pour réseaux Internet Protocol. Le système est une distribution Linux spécialisée basée sur Debian avec des applications réseau telles que Quagga, OpenVPN, et bien d’autres. Ancêtre de VyOS et base de Ubiquiti EdgeOS.  
[Source](https://fr.wikipedia.org/wiki/Vyatta)

Web
: Un système hypertexte public fonctionnant sur Internet. Le Web permet de consulter, à l’aide d’un navigateur, des pages regroupées en sites. Web signifie littéralement « toile (d’araignée) », image représentant les hyperliens qui lient les pages web entre elles.  
Le Web est une des applications d’Internet, qui est distincte d’autres applications comme les réseaux sociaux, le courrier électronique et la visioconférence. Inventé en 1989-1990 au CERN par Tim Berners-Lee épaulé de Robert Cailliau, le Web popularise Internet. Depuis, il est fréquemment confondu avec ce dernier.  
[Source](https://fr.wikipedia.org/wiki/World_Wide_Web)

webapp2
: Était un framework web léger en {term}`Python`, compatible avec webapp de {term}`Google App Engine`. Il pouvait également être utilisé en dehors de {term}`Google App Engine` indépendamment du SDK. Cependant, sa base de code {term}`Python` 2 n’a jamais été migrée vers {term}`Python` 3, ce qui a conduit à son obsolescence.  
[Site officiel](https://webapp2.readthedocs.io)  
[Code source](https://github.com/GoogleCloudPlatform/webapp2) *Archivé depuis le 30 novembre 2023*

WebSocket
: Un standard du {term}`Web` désignant un {term}`protocole` réseau de la couche application et une interface de programmation du World Wide Web visant à créer des canaux de communication full-duplex par-dessus une connexion TCP pour les navigateurs web. Le {term}`protocole` a été normalisé par l’IETF dans la RFC 6455 en 2011 et l’interface de programmation par le W3C.  
[Source](https://fr.wikipedia.org/wiki/WebSocket)  
[RFC](https://www.rfc-editor.org/info/rfc6455/)

Wi-Fi
: Un ensemble de {term}`protocoles <Protocole>` de communication sans fil régi par les normes du groupe IEEE 802.11. Un réseau Wi-Fi permet de relier par ondes radio plusieurs appareils informatiques au sein d’un réseau informatique afin de permettre la transmission de données entre eux.  
[Source](https://fr.wikipedia.org/wiki/Wi-Fi)

Wireshark
: Un analyseur de paquets {term}`Libre <Logiciel Libre>` et gratuit. Il est utilisé dans le dépannage et l’analyse de réseaux informatiques, le développement de {term}`protocoles <Protocole>`, l’éducation et la rétro-ingénierie.  
[Source](https://fr.wikipedia.org/wiki/Wireshark)

Xcode
: Xcode est un environnement de développement pour macOS, ainsi que pour iOS, watchOS, tvOS et visionOS.  
[Source](https://fr.wikipedia.org/wiki/Xcode)  
[Site officiel](https://developer.apple.com/xcode/)

zbus
: Une {term}`bibliothèque` écrite en {term}`Rust` 100 % natif, développée par Zeeshan Ali Khan (zeenix), qui fournit une API pour interagir avec D-Bus, le système IPC largement utilisé sur {term}`Linux`. Elle gère automatiquement l’établissement de la connexion, ainsi que la création, l’envoi et la réception des différents types de messages D-Bus (appels de méthodes, signaux, etc.).  
[Documentation](https://docs.rs/zbus)  
[Livre](https://z-galaxy.github.io/zbus)  
[Distribution](https://crates.io/crates/zbus)  
[Source code](https://github.com/z-galaxy/zbus)
:::

## Audiovisuel & Spectacle Vivant

:::{glossary}
Alternance
: La formation par alternance aussi appelée formation duale ou formation en apprentissage, désigne un système de formation qui intègre une expérience de travail où la personne concernée, l’alternant qui peut être élève, étudiant ou apprenti, se forme alternativement en entreprise privée ou publique et dans un établissement d’enseignement comme, en France, un lycée professionnel, un centre de formation d’apprentis, un établissement public local d’enseignement et de formation professionnelle agricole, une maison familiale rurale, une école d’ingénieur ou une université. En Suisse, les établissements d’enseignement qui se calquent sur le modèle de la formation duale s’appellent écoles professionnelles.  
L’étudiant alternant suit une formation dispensée par un établissement d’enseignement et par une entreprise d’accueil où il a un statut particulier, salarié ou stagiaire, indemnisé ou non, ou apprenti. La fréquence de l’alternance est très variable d’une formation à l’autre. Dans certaines formations en médecine, la fréquence est très élevée : le matin, ils sont à l’hôpital, l’après-midi, ils suivent les cours en amphithéâtre. Certaines formations d’ingénieurs pratiquent une alternance pouvant aller jusqu’à une périodicité de plusieurs mois.  
[Source](https://fr.wikipedia.org/wiki/Formation_par_alternance)

Ardour
: Une station audio-numérique {term}`Libre <Logiciel Libre>` souvent présentée comme une alternative {term}`Libre <Logiciel Libre>` au logiciel Pro Tools.  
Elle est disponible sur {term}`Linux`, {term}`macOS <Apple macOS>`, {term}`Windows <Microsoft Windows>` et Solaris.  
Son principal auteur est Paul Davis, qui est également l’auteur du serveur audio JACK.  
[Source](https://fr.wikipedia.org/wiki/Ardour)  
[Site officiel](https://ardour.org)  
[Code source](https://git.ardour.org)
*(L’auteur de ces pages a [contribué](https://github.com/Ardour/ardour/commits?author=rdoursenaud) à la traduction française.)*

Asset
: Éléments graphiques ou multimédias unitaires (icônes, textures, modèles 3D, boutons d’interface, illustrations, sons) conçus pour être intégrés et réutilisés dans un projet plus vaste (site web, application, jeu vidéo, film). La création d’assets optimisés et modulaires est une étape clé dans les pipelines de production utilisant {term}`Krita`, {term}`Inkscape`, {term}`Blender` ou encore {term}`Ardour`.

Authoring
: Processus de création d’un DVD ou Blu-ray vidéo à fins d’utilisation dans une platine de salon. La production complète d’un DVD/Blu-ray vidéo comprend plusieurs étapes. Compressions de la vidéo en MPEG-2 () et de l’audio en Dolby Digital (AC3) ou en PCM (WAV), graphismes et animation des interfaces de navigation, intégration et programmation des éléments, inscription sur DVD et ou cartouche DLT. Les logiciels d’auteuring DVD doivent être conformes aux spécifications définies par le DVD Forum group en 1995. Ces spécifications sont complexes en raison du grand nombre de compagnies impliquées dans ce processus.  
L’auteuring DVD est un processus séparé de la compression des vidéos en MPEG-2, mais quelques systèmes professionnels possèdent ces deux fonctionnalités. Soit une carte d’encodage MPEG-2 ou un logiciel d’encodage intégré. La solution matérielle donne à qualité égale des résultats plus rapides, ou à temps de calcul égal un encodage de meilleure qualité.  
Il y a plusieurs applications pour programmer les DVD vidéo contrairement au standard DVD audio, où il y en a peu.  
[Source](https://fr.wikipedia.org/wiki/Auteuring_DVD)
*(L’auteur de ces pages a probablement réalisé un des premiers authoring envoyé au pressage en utilisant majoritairement des {term}`Logiciels Libres <Logiciel Libre>`. Et ce à deux reprises en 2005 (DVD-R) et 2010 (DLT). En détournant, par ailleurs, les techniques issues du « fansub » pour générer les sous-titres, {term}`Blender` pour le générique de fin dont le défilement a été précisémment calculé pour éviter le scintillement, et autres acrobaties réservées aux professionnels…)*

Art-Net
: {term}`Protocole` de transport du signal **DMX** sur des réseaux Ethernet (IP). Permet de déporter et de router des signaux d’éclairage sur de longues distances via l’infrastructure réseau standard.

Blender
: Un {term}`Logiciel Libre` de modélisation, d’animation par ordinateur et de rendu en 3D, créé en 1994. Il est actuellement développé par la Fondation Blender.  
Depuis 2019, le logiciel Blender est de plus en plus reconnu par les entreprises du secteur de l’animation 3D, comme Epic Games, Ubisoft et Nvidia.  
Il propose des fonctions avancées de modélisation (dont la sculpture 3D, le texturage et dépliage UV, etc), d’animation 3D (rigging, blend shapes), et de rendu (sur processeur graphique comme sur processeur). Il gère aussi le montage vidéo non linéaire, la composition, la création nodale de matériaux, ainsi que diverses simulations physiques telles que les particules, les corps rigides, les corps souples et les fluides. Ses capacités sont par ailleurs très extensibles, grâce à un système de greffons.  
[Source](https://fr.wikipedia.org/wiki/Blender)  
[Site officiel](https://www.blender.org/)

Compositing
: Technique de post-production consistant à assembler plusieurs sources d’images (rendus 3D, prises de vues réelles, éléments graphiques 2D) en une seule image finale cohérente. Cela inclut la gestion des incrustations (fond vert), des effets de lumière, des ombres et des corrections colorimétriques. Dans un environnement {term}`Libre <Logiciel Libre>`, des logiciels comme {term}`Blender` (avec son éditeur de nœuds) permettent de réaliser des compositings complexes sans recourir à des solutions propriétaires coûteuses.

Cubase
: Cubase est une famille de séquenceurs musicaux conçus par la société allemande Steinberg Media Technologies.  
Ce logiciel a succédé à la série des séquenceurs « Pro » commencée sur C64 pour prendre fin avec PRO-24 III sur Atari.  
Les premières versions de Cubase sont apparues sur Atari puis {term}`Mac <Apple macOS>` et {term}`Windows <Microsoft Windows>`.  
[Source](https://fr.wikipedia.org/wiki/Cubase)  
[Site officiel](https://www.steinberg.net/cubase/)  
*(L’auteur de ces lignes a commencé avec Steinberg **Cubase 2.0** sur un **Atari 1040 STe** puis un **Falcon 030** qu’il possèdes encore !)*

Frescobaldi
: Un logiciel de création de partitions musicales pour {term}`LilyPond`. Frescobaldi est un {term}`Logiciel Libre`, disponible gratuitement sous licence GNU GPL. Il est conçu pour fonctionner sur tous les principaux systèmes d’exploitation. Il est nommé d’après Girolamo Frescobaldi (1583-1643), un compositeur italien de la fin de la Renaissance et du début du Baroque.  
[Source](https://fr.wikipedia.org/wiki/Frescobaldi_(logiciel))  
[Site officiel](https://frescobaldi.org)  
[Code source](https://github.com/frescobaldi/frescobaldi)  
*(L’auteur de ces pages a [contribué](https://github.com/frescobaldi/frescobaldi/commits?author=rdoursenaud) la traduction française.)*

HiQnet
: Un {term}`protocole` développé par Harman Pro pour la communication et le pilotage d’équipements audio professionnels. Conçu par le groupe *System Development & Integration* (SDIG) de Harman Pro en 2004, il a été annoncé en janvier 2005. Le {term}`protocole` et son port ont été enregistrés auprès de l’IANA en février 2004 par Bruce Vander Werf.  
[Source](https://wiki.wireshark.org/HiQnet)  
*(Rédigée par l’auteur de ces pages à l’occasion du développement du dissecteur.)*

Inkscape
: Un logiciel de dessin vectoriel. Diffusé sous licence GNU GPL version 3, c’est un {term}`Logiciel Libre`. Il est disponible sous {term}`macOS <Apple macOS>`, {term}`Linux` et {term}`Microsoft Windows`.  
Les images vectorielles sont constituées par des courbes qui reposent sur des formules mathématiques. Inkscape est ainsi particulièrement adapté au travail professionnel sur les logos et les affiches. Ses fonctionnalités sont assez proches des logiciels propriétaires Adobe Illustrator et CorelDraw.  
Inkscape fait partie des {term}`Logiciels Libres <Logiciel Libre>` préconisés par l’État français dans le cadre de la modernisation globale de ses systèmes d’information.  
[Source](https://fr.wikipedia.org/wiki/Inkscape)  
[Site officiel](https://inkscape.org)

Krita
: Un logiciel de peinture numérique et d’animation 2D. Disponible sous {term}`MacOS <Apple macOS>`, {term}`Linux` et {term}`Microsoft Windows`, c’est un {term}`Logiciel Libre` et gratuit diffusé sous licence GNU.  
Contrairement à des logiciels comme GIMP, Affinity Photo ou Photoshop, il n’est pas conçu pour la retouche de photos. Il est très apprécié par les artistes et les peintres numériques.  
Il fait partie de la famille KDE. Projet à but non-lucratif, son développement est soutenu depuis 2012 par la Fondation Krita.  
[Source](https://fr.wikipedia.org/wiki/Krita)  
[Site officiel](https://krita.org)

LilyPond
: Un {term}`Logiciel Libre` de notation musicale créé en 1996 par Han-Wen Nienhuys et Jan Nieuwenhuizen alors qu’ils étaient encore lycéens à Eindhoven (Pays-Bas). Développé par une communauté internationale dans le cadre du projet GNU, ce logiciel offre un langage de description de la musique, qu’il compile ensuite sous forme de partition écrite. Selon ses auteurs, cette approche classique permet ainsi de libérer les musiciens de toute préoccupation typographique pour offrir un rendu de haute qualité esthétique.  
[Source](https://fr.wikipedia.org/wiki/LilyPond)  
[Site officiel](https://lilypond.org)

LoopMIDI
: Cordon MIDI virtuel de bouclage (*loopback*) pour {term}`Windows <Microsoft Windows>` 7 jusqu’à {term}`Windows <Microsoft Windows>` 10, 32 et 64 bit, écrit par Tobias Erichsen et s’appuyant sur son pilote noyau personnalisé virtualMIDI.  
Distribué gratuitement pour un usage personnel non-commercial. Pour un usage commercial ou redistribution, un accord écrit du développeur est requis.
[Site officiel](https://www.tobias-erichsen.de/software/loopmidi.html)

Motion Design
: Discipline artistique et technique consistant à animer des éléments graphiques (typographie, logos, illustrations) pour créer du mouvement et du rythme, souvent utilisée dans les génériques, les publicités ou les interfaces dynamiques. Contrairement à l’animation de personnages traditionnelle, le motion design se concentre sur la mise en mouvement de l’information visuelle. Il fait souvent appel à des outils comme {term}`Blender` (pour la 3D et le {term}`compositing`) ou {term}`Krita` (pour l’animation 2D image par image). Historiquement les outils de référence étaient Macromédia Flash, Director et Shockwave.

Nuendo
: Une station audionumérique évoluée de la société allemande Steinberg Media Technologies.  
Il tire ses fonctions essentielles du séquenceur musical {term}`Cubase`, de Steinberg également, lui offrant ainsi une ergonomie et une panoplie d’outils pour la création musicale, mais va beaucoup plus loin que {term}`Cubase` en apportant de nombreuses fonctions supplémentaires. Il s’agit d’une station audio-numérique professionnelle adaptée pour la production sonore au sens large, dépassant donc le simple domaine musical (Cinéma, audiovisuel, jeux-vidéo, réalité virtuelle).
[Source](https://fr.wikipedia.org/wiki/Nuendo)  
[Site officiel](https://www.steinberg.net/nuendo)

Scribus
: Un logiciel de publication assistée par ordinateur (PAO), distribué sous licence {term}`Libre <Logiciel Libre>` GNU GPL. Basé sur le framework multiplateforme {term}`Qt`, il fonctionne nativement sur les systèmes UNIX, {term}`Linux`, {term}`Mac OS X <Apple macOS>`, {term}`Windows <Microsoft Windows>` et OS/2. Il fournit un large éventail de fonctionnalités de mise en page, comparable aux principales applications professionnelles, telles que QuarkXPress, Adobe InDesign ou Affinity Publisher.
Il permet de créer des présentations animées et interactives, des formulaires PDF, des dépliants, des plaquettes, des livres et des magazines, et tout type de document destiné à être imprimé ou à être visualisé sous forme numérique.  
En France, le logiciel est intégré à la liste des {term}`Logiciels Libres <Logiciel Libre>` préconisés par l’État dans le cadre de la modernisation globale de ses systèmes d’information ; de même, au Canada, aux logiciels et ressources numériques libres pour l’enseignement supérieur.  
[Source](https://fr.wikipedia.org/wiki/Scribus)  
[Site officiel](https://www.scribus.net)

Studio One
: Un logiciel station de travail audio numérique de PreSonus. Voir {term}`Studio Pro`.

Studio Pro
: (Anciennement Studio One Pro) Une station de travail audio-numérique (DAW) utilisée pour créer, enregistrer, mixer et masteriser de la musique et d’autres contenus audio, avec des fonctionnalités également disponibles pour la vidéo. Initialement développé comme successeur du moteur audio KRISTAL, il a été acquis par PreSonus et publié pour la première fois sous le nom de Studio One en 2009 pour {term}`macOS <Apple macOS>` et {term}`Microsoft Windows`. PreSonus et Studio One ont ensuite été rachetés par Fender en 2021, ce qui a conduit au renommage du produit en Fender Studio Pro en 2026.
[Source](https://en.wikipedia.org/wiki/Studio_Pro)  
[Site officiel](https://fender.com/products/fender-studio-pro)
:::

## Concepts & Organisation

:::{glossary}
Cloud
: Le cloud computing, en français l’informatique en nuage (ou encore l’infonuagique au Canada), est la pratique consistant à utiliser des serveurs informatiques à distance, hébergés dans des centres de données connectés à Internet pour stocker, gérer et traiter des données, plutôt qu’un serveur local ou un ordinateur personnel. Les principaux services proposés en cloud computing sont le SaaS (software as a Service), le PaaS (platform as a Service) et le IaaS (infrastructure as a service) ou le MBaaS (mobile backend as a service). On distingue généralement trois types de cloud : le cloud public — accessible par Internet —, le cloud d’entreprise ou privé — accessible uniquement sur un réseau privé —, le cloud intermédiaire ou hybride — qui est une combinaison entre le cloud public et le cloud privé.
[Source](https://fr.wikipedia.org/wiki/Cloud_computing)

Coopérative
: Entreprise collective dont les membres (sociétaires) sont à la fois associés et utilisateurs. Les décisions sont prises démocratiquement (une personne = une voix) et les bénéfices sont répartis équitablement ou réinvestis. Voir **refuge.coop**.

Interopérabilité
: L’interopérabilité est la capacité que possède un produit ou un système, dont les interfaces sont intégralement conçues à fonctionner avec d’autres produits ou systèmes existants ou futurs et ce sans restriction d’accès ou de mise en œuvre.  
Il convient de distinguer « interopérabilité » et « compatibilité ». Pour être simple, on peut dire que la compatibilité est une notion verticale qui fait qu’un outil peut fonctionner dans un environnement donné en respectant toutes les caractéristiques et l’interopérabilité est une notion transversale qui permet à divers outils de pouvoir communiquer - quand on sait pourquoi, et comment, ils peuvent fonctionner ensemble.  
Autrement dit, on ne peut parler d’interopérabilité d’un produit ou d’un système que si on connaît intégralement toutes ses interfaces.  
[Source](https://fr.wikipedia.org/wiki/Interop%C3%A9rabilit%C3%A9)

Live
: En concert.

Logiciel Libre
: Logiciel respectant les quatre libertés fondamentales : utiliser, étudier, modifier et redistribuer le code source. Favorise la collaboration et la transparence.  
[Source](https://fr.wikipedia.org/wiki/Mouvement_du_logiciel_libre)

Mention
: Distinction attribuée par le jury lors de l’obtention d’un diplôme français (comme le Baccalauréat ou le BTS), basée sur la moyenne générale des notes obtenues aux examens. Contrairement aux distinctions universitaires internationales utilisant le latin (Cum Laude, etc.), le système éducatif français utilise des qualificatifs : Assez Bien (12-14), Bien (14-16) et Très Bien (>16). Ils témoignent d’un niveau d’excellence technique et théorique supérieur à la simple validation du diplôme.  
[Source](https://fr.wikipedia.org/wiki/Mention_honorifique)

Open Source
: Terme désignant une méthode de développement où le code source est accessible, popularisée par l’OSI. Bien que techniquement proche du {term}`Logiciel Libre`, le mouvement Open Source met l’accent sur les avantages pragmatiques (qualité, collaboration, coût) en occultant souvent la dimension éthique et les libertés fondamentales de l’utilisateur. Cette nuance permet parfois l’usage de licences restrictives (« source disponible ») qui ne garantissent pas les mêmes droits que le {term}`Logiciel Libre`.  
[Source](https://fr.wikipedia.org/wiki/Open_source)  
[Site officiel](https://opensource.org)

Print
: Terme désignant l’ensemble des supports destinés à l’impression physique (affiches, flyers, brochures, jaquettes de CD/DVD). Dans un flux de travail {term}`Libre <Logiciel Libre>`, cela implique l’utilisation de logiciels comme {term}`Scribus` pour la mise en page et {term}`Inkscape` pour le vectoriel, avec une gestion rigoureuse des espaces colorimétriques (passage de RVB à CMJN) et des résolutions adaptées à l’impression offset ou numérique.

Protocole
: On nomme protocole les conventions qui facilitent une communication ou des interactions sans faire directement partie du sujet de la communication elle-même. Ce terme est utilisé dans plusieurs domaines :
  - Arts :
    - L’Art protocolaire (ou art des protocoles) est une pratique de l’art contemporain où l’œuvre est définie par un ensemble d’instructions ou de règles établies par l’artiste ;
    - Le protocole peut également désigner, dans les arts de la performance ou la musique expérimentale, la partition d’un événement (event score).
  - Informatique/ électronique :
    - un protocole informatique est un ensemble de règles qui régissent les échanges de données ou le comportement collectif de processus ou d’ordinateurs en réseaux ou d’objets connectés ;
    - un protocole de communication est un ensemble de contraintes permettant d’établir une communication entre deux entités : Internet Protocol, suite des protocoles Internet, protocole réseau par exemple ;
  - Sciences : protocole d’expérimentation ;  
  
  [Source](https://fr.wikipedia.org/wiki/Protocole)

Souveraineté Numérique
: Capacité d’une entité (individu, entreprise, territoire) à maîtriser ses outils numériques, ses données et ses infrastructures, en réduisant la dépendance envers des fournisseurs externes ou des juridictions étrangères. Privilégie les solutions locales, open-source et autonomes.
:::

:::{note}
Ce glossaire est vivant. Les définitions sont adaptées au contexte de mes projets et de la coopérative **refuge.coop**. N’hésitez pas à proposer des enrichissements.
:::
