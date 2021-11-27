# Informationen zum Projekt
- Link zum [Testen](https://ccc-jugendgruppe.github.io/fairydustforest/)
 

# Unsere Map
![Screenshot.](https://github.com/CCC-Jugendgruppe/fairydustforest/blob/master/Bilder/Keller.png)
![Screenshot.](https://github.com/CCC-Jugendgruppe/fairydustforest/blob/master/Bilder/neotopia.png)
![Sreenshot.](https://github.com/CCC-Jugendgruppe/fairydustforest/blob/master/Bilder/see.png)

# WorkAdventure Map Starter Kit

This is a starter kit to help you build your own map for [WorkAdventure](https://workadventu.re).


# Einrichten einer Arbeitsumgebung

## Das Projekt klonen

Um das Projekt zu klonen ist ein Git Client erforderlich.


`git clone https://github.com/CCC-Jugendgruppe/fairydustforest.git`

Wenn du mit Git nicht vertraut bist würde sich der Github Desktop Client eignen. 

https://desktop.github.com/


## Tools you will need

In order to build your own map for WorkAdventure, you need:

- the [Tiled editor](https://www.mapeditor.org/) software
- "tiles" (i.e. images) to create your map (this starter kit provides a good default tileset for offices)
- a web-server to serve your map (this starter kit proposes to use Github static pages as a web-server which is both free and performant)

## Getting started

On the [Github repository page](https://github.com/thecodingmachine/workadventure-map-starter-kit),
click the **"Use this template"** button. You will be prompted to enter a repository name for your map.

![](docs/create_repo.png)

Be sure to keep the repository "Public".

In your newly created repository, click on the **Settings tab** and scroll down to the **GitHub Pages** section.
Then select the **gh-pages** branch. 

![](docs/github_pages.png)

Wait a few minutes a Github will deploy a new website with the content of the repository.
The address of the website is visible in the "GitHub Pages" section.

![](docs/website_address.png)

Click on the link. You should be redirected directly to WorkAdventure, on your map!

## Customizing your map

Your map is now up and online. You need to customize it.



### Loading the map in Tiled

The sample map is in the file `map.json`.
You can load this file in [Tiled](https://www.mapeditor.org/).

Now, it's up to you to edit the map and write your own map.

Some resources regarding Tiled:

- [Tiled documentation](https://doc.mapeditor.org/en/stable/manual/introduction/)
- [Tiled video tutorials](https://www.gamefromscratch.com/post/2015/10/14/Tiled-Map-Editor-Tutorial-Series.aspx)

### About WorkAdventu maps

here is an [overview](https://howto.rc3.world/maps.html)

### Pushing the map

When your changes are ready, you need to `git add`, `git commit` and `git push` the changes back to GitHub.
Just wait a few minutes, and your map will be propagated automatically to the GitHub pages web-server.

TODO: describe how to push
