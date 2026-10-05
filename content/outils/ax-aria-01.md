---

title: "Rôles ARIA interdits, abstraits ou vides (AX_ARIA_01)"
a11ynot_id: AX_ARIA_01
category: outils
gistID: 4b6cd17c1e4a3ad175e6
original_url: "http://a11ynot.com/nots/AX_ARIA_01.html"
layout: a11ynot
type: a11ynot
tags:
  - ainspector
  - axe
tag_labels:
  - AInspector Sidebar
  - aXe
---

<h2 aria-describedby="4b6cd17c1e4a3ad175e6">Début de l'exemple</h2>
<div class="rendered-not">
<div role="datepicker"></div> <!-- Bad: "datepicker" is not an ARIA role -->
<div role="range"></div>      <!-- Bad: "range" is an _abstract_ ARIA role -->
<div role=""></div>           <!-- Bad: An empty ARIA role is not allowed -->
</div> <!-- rendered-not -->

<h2 aria-describedby="4b6cd17c1e4a3ad175e6">Fin de l'exemple</h2>

<h3 aria-describedby="4b6cd17c1e4a3ad175e6">Code de cet exemple</h3>
<script src="https://gist.github.com/4b6cd17c1e4a3ad175e6.js"></script>
