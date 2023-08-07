# Djungeon
> A player generated Choose Your Own Adventure game made with Django, Django Rest Framework and Vue.js

## Post-Mortem
Note: Please ignore the lack of git history, this project was recently migrated out of a larger monorepo so the commit history was lost.

I built Djungeon over a few days as a portfolio project to demonstrate my ability mainly with Django and Vue.js. I decided against doing the conventional blog example, mostly just because I wanted to do something more unique but also because I think it helps prove that I do know what I'm doing to an extent (I couldn't find a Django-Vue CYOA game to copy the code from).

A bit more details on what it actually is, a player creates a "room" which contains a title (eg "The Corridor of Choice"), a prompt ("You find yourself at a junction, do you...") and two choices ("Turn left" and "Turn right"). Each one of these choices will connect to a random room created by another player, gradually building a more complex, sprawling game.

On reflection, it doesn't really work as a game. A good room in a CYOA game will be informed by the room that linked to it, whereas Djungeon just joins everything up randomly. I did take a shot at building a better version, but came into a conflict of interest; my better version ended up far simpler, so was less worthwhile as a portfolio project. This version may not work as a product, but because of some of the weird things I had to do to make it work, it ends up being very nice as a portfolio project.

It's nothing massively complex, as I say it was only built over a few days, so the code should be reasonably easy to digest.

## Setup
### Django
In djungeon_django, run `pipenv install` and `pipenv shell`. Then, run migrations and start the server with `./manage.py runserver 8000`. You must use port 8000 for the vue front-end to work. However, django alone will also work with its own in-built frontend

### Vue
In djungeon_vue, run npm install and then `npm run serve`. Similar to the above, it must run on port 8080 to connect to Django