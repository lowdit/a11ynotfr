---

title: "Champ sans label associé et bouton sans nom (AX_TEXT_01)"
a11ynot_id: AX_TEXT_01
category: outils
gistID: de8704af985f60a4bb4d
original_url: "http://a11ynot.com/nots/AX_TEXT_01.html"
layout: a11ynot
type: a11ynot
tags:
  - ainspector
  - axe
  - devtools
  - wave
tag_labels:
  - AInspector Sidebar
  - aXe
  - Accessibility Developer Tools
  - WAVE
---

<h2 aria-describedby="de8704af985f60a4bb4d">Début de l'exemple</h2>
<div class="rendered-not">
<div>
  Enter your address:
  <input id="address">                <!-- Bad: label not associated with control -->
</div>

<button class="enter_site"></button>  <!-- Bad: button has no text description -->
</div> <!-- rendered-not -->

<h2 aria-describedby="de8704af985f60a4bb4d">Fin de l'exemple</h2>

<h3 aria-describedby="de8704af985f60a4bb4d">Code de cet exemple</h3>
<script src="https://gist.github.com/de8704af985f60a4bb4d.js"></script>
