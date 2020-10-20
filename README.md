# Plot covid-19 France

Ce dépot contient du code permettant de visualiser les données en rapport avec
l'épidémie de COVID-19 en France. On se concentre pour l'instant sur la reprise
de l'épidémie quelques mois après la sortie du confinement (à partir d'août
2020, donc).

## Comment visualiser les figures?

- Pour visualiser les figures sans le code (avec Voilà), c'est par là-bas http://tiny.cc/plot-covid19-fr

- Pour visualiser les figures sans le code (avec Voilà et Binder), cliquez sur
ce bouton : [![Binder
Voila](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/paugier/plot-covid19-fr/branch/default?urlpath=%2Fvoila%2Frender%2Fplot_covid19.ipynb)

- Pour visualiser le code et les figures et potentiellement modifier le code
(avec Jupyter Notebook), cliquez sur ce bouton :
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/paugier/plot-covid19-fr/branch/default?filepath=plot_covid19.ipynb)

- Il y a aussi une instance sur Heroku gratuit
(https://plot-covid19-fr.herokuapp.com/) mais ça rame dès que plusieurs
utilisateurs sont connectés!

- Pour l'instant le plus efficace est encore de récupérer le code et de lancer
l'application localement (voir plus bas).

## A propos des données utilisées

### Données Système d’Informations de DEPistage (SI-DEP)

https://www.data.gouv.fr/fr/datasets/donnees-relatives-aux-resultats-des-tests-virologiques-covid-19/

- Départements :
https://www.data.gouv.fr/fr/datasets/r/406c6a23-e283-4300-9484-54e78c8ae675
(`sp-pos-quot-dep-*-19h15.csv`)

- France :
https://www.data.gouv.fr/fr/datasets/r/dd0de5d9-b5a5-4503-930a-7b08dc0adc7c
(`sp-pos-quot-fra-*-19h15.csv`)

### Données hospitalières

https://www.data.gouv.fr/fr/datasets/donnees-hospitalieres-relatives-a-lepidemie-de-covid-19/

- Variations à hospital :
https://www.data.gouv.fr/fr/datasets/r/6fadff46-9efd-4c53-942a-54aca783c30c
(`donnees-hospitalieres-nouveaux-covid19-*-19h00.csv`)

## Thanks

Le projet est hébergé sur [foss.heptapod.net](ttps://foss.heptapod.net). Merci
à [Octobus](https://octobus.net/) et [Clever
Cloud](https://www.clever-cloud.com)!

## Lancer l'application localement (plus rapide)

L'application tourne sur Python 3.8. Pour récupérer les sources, le plus simple
est de cloner le dépot avec Mercurial avec la commande `hg clone
https://foss.heptapod.net/graphics/plot-covid19-fr`. Pour mettre à jour, il
faudra juste faire depuis le répertoire du dépôt `hg pull -u`. Pour les
utilisateurs de Git qui ne voudraient pas découvrir le zen de Mercurial,
utiliser le dépôt miroir https://github.com/paugier/plot-covid19-fr.

Ensuite pour installer et lancer :

```
cd plot-covid19-fr
python3.8 -m pip install -r requirements.txt
voila plot_covid19.ipynb
```
