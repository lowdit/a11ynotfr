---

title: "Propriété aria-owns inutile quand la hiérarchie DOM suffit (AX_ARIA_06)"
a11ynot_id: AX_ARIA_06
category: outils
gistID: aaf96aa84b339234be4c
original_url: "http://a11ynot.com/nots/AX_ARIA_06.html"
layout: a11ynot
type: a11ynot
tags:
  - devtools
tag_labels:
  - Accessibility Developer Tools
---

<h2 aria-describedby="aaf96aa84b339234be4c">Début de l'exemple</h2>
<div class="rendered-not">
<!-- Bad: the ownership is implicit in the DOM structure (each radio is a descendant of the radiogroup) -->
<ul role="radiogroup" aria-labelledby="foo" aria-owns="radio1 radio2 radio3"> 
    <li id="radio1" tabindex="-1" role="radio" aria-checked="false">Rainbow Trout</li> 
    <li id="radio2" tabindex="-1" role="radio" aria-checked="false">Brook Trout</li>
    <li id="radio3" tabindex="0" role="radio" aria-checked="true">Lake Trout</li>
</ul>
</div> <!-- rendered-not -->

<h2 aria-describedby="aaf96aa84b339234be4c">Fin de l'exemple</h2>

<h3 aria-describedby="aaf96aa84b339234be4c">Code de cet exemple</h3>
<script src="https://gist.github.com/aaf96aa84b339234be4c.js"></script>
