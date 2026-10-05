---

title: "Même liste « possédée » par deux combobox (AX_ARIA_07)"
a11ynot_id: AX_ARIA_07
category: outils
gistID: 7da5d9473e61d781135e
original_url: "http://a11ynot.com/nots/AX_ARIA_07.html"
layout: a11ynot
type: a11ynot
tags:
  - devtools
tag_labels:
  - Accessibility Developer Tools
---

<h2 aria-describedby="7da5d9473e61d781135e">Début de l'exemple</h2>
<div class="rendered-not">
<!-- Bad: list1 is owned by two comboboxes -->
<input id="combo1" type="text" role="combobox" aria-labelledby="foo" aria-owns="list1"/>

<input id="combo2" type="text" role="combobox" aria-labelledby="foo" aria-owns="list1"/>

<ul id="list1" aria-expanded="true" role="listbox">
    <li role="option" tabindex="-1">Rainbow Trout</li>
    <li role="option" tabindex="-1">Brook Trout</li>
    <li role="option" tabindex="-1">Lake Trout</li>
</ul>
</div> <!-- rendered-not -->

<h2 aria-describedby="7da5d9473e61d781135e">Fin de l'exemple</h2>

<h3 aria-describedby="7da5d9473e61d781135e">Code de cet exemple</h3>
<script src="https://gist.github.com/7da5d9473e61d781135e.js"></script>
