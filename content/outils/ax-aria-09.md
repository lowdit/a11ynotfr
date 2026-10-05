---

title: "listitem en dehors d’un conteneur list (AX_ARIA_09)"
a11ynot_id: AX_ARIA_09
category: outils
gistID: 428bac8391a7f1a56145
original_url: "http://a11ynot.com/nots/AX_ARIA_09.html"
layout: a11ynot
type: a11ynot
tags:
  - axe
  - ainspector
  - devtools
tag_labels:
  - aXe
  - AInspector Sidebar
  - Accessibility Developer Tools
---

<h2 aria-describedby="428bac8391a7f1a56145">Début de l'exemple</h2>
<div class="rendered-not">
<!-- Bad: the listitem role must be owned by an element with role list -->
<div> 
    <span role="listitem">Rainbow Trout</span> 
    <span role="listitem">Brook Trout</span>
    <span role="listitem">Lake Trout</span>
</div>
</div> <!-- rendered-not -->

<h2 aria-describedby="428bac8391a7f1a56145">Fin de l'exemple</h2>

<h3 aria-describedby="428bac8391a7f1a56145">Code de cet exemple</h3>
<script src="https://gist.github.com/428bac8391a7f1a56145.js"></script>
