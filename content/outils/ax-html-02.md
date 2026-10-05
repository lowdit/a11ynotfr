---

title: "Identifiant id dupliqué dans la page (AX_HTML_02)"
a11ynot_id: AX_HTML_02
category: outils
gistID: f5910b21c535988894a3
original_url: "http://a11ynot.com/nots/AX_HTML_02.html"
layout: a11ynot
type: a11ynot
tags:
  - axe
  - devtools
tag_labels:
  - aXe
  - Accessibility Developer Tools
---

<h2 aria-describedby="f5910b21c535988894a3">Début de l'exemple</h2>
<div class="rendered-not">
<!-- Bad: the id 'trout' should only occur once in the "page" -->
<input type="radio" id="trout" name="trout" value="rainbow"/>
<input type="radio" id="trout" name="trout" value="brook"/>
<input type="radio" id="trout" name="trout" value="lake"/>
</div> <!-- rendered-not -->

<h2 aria-describedby="f5910b21c535988894a3">Fin de l'exemple</h2>

<h3 aria-describedby="f5910b21c535988894a3">Code de cet exemple</h3>
<script src="https://gist.github.com/f5910b21c535988894a3.js"></script>
