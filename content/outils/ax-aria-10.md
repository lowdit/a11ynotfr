---

title: "Attribut ARIA non pris en charge par le rôle (aria-required sur radio) (AX_ARIA_10)"
a11ynot_id: AX_ARIA_10
category: outils
gistID: 4bc567244032d0a5448c
original_url: "http://a11ynot.com/nots/AX_ARIA_10.html"
layout: a11ynot
type: a11ynot
tags:
  - axe
  - devtools
tag_labels:
  - aXe
  - Accessibility Developer Tools
---

<h2 aria-describedby="4bc567244032d0a5448c">Début de l'exemple</h2>
<div class="rendered-not">
<!-- Bad: the radio role does not support the aria-required property -->
<ul role="radiogroup" aria-labelledby="foo"> 
    <li aria-required="true" tabindex="-1" role="radio" aria-checked="false">Rainbow Trout</li> 
    <li aria-required="true" tabindex="-1" role="radio" aria-checked="false">Brook Trout</li>
    <li aria-required="true" tabindex="0" role="radio" aria-checked="true">Lake Trout</li>
</ul>
</div> <!-- rendered-not -->

<h2 aria-describedby="4bc567244032d0a5448c">Fin de l'exemple</h2>

<h3 aria-describedby="4bc567244032d0a5448c">Code de cet exemple</h3>
<script src="https://gist.github.com/4bc567244032d0a5448c.js"></script>
