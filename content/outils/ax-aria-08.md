---

title: "Radiogroup sans éléments role radio associés (AX_ARIA_08)"
a11ynot_id: AX_ARIA_08
category: outils
gistID: e24ea75ba197acb94d6a
original_url: "http://a11ynot.com/nots/AX_ARIA_08.html"
layout: a11ynot
type: a11ynot
tags:
  - axe
  - devtools
tag_labels:
  - aXe
  - Accessibility Developer Tools
---

<h2 aria-describedby="e24ea75ba197acb94d6a">Début de l'exemple</h2>
<div class="rendered-not">
<!-- Bad: the radiogroup role must own elements with role radio -->
<ul role="radiogroup" aria-labelledby="foo"> 
    <li id="radio1" tabindex="-1">Rainbow Trout</li> 
    <li id="radio2" tabindex="-1">Brook Trout</li>
    <li id="radio3" tabindex="0">Lake Trout</li>
</ul>
</div> <!-- rendered-not -->

<h2 aria-describedby="e24ea75ba197acb94d6a">Fin de l'exemple</h2>

<h3 aria-describedby="e24ea75ba197acb94d6a">Code de cet exemple</h3>
<script src="https://gist.github.com/e24ea75ba197acb94d6a.js"></script>
