---

title: "aria-labelledby qui ne pointe vers aucun id (AX_ARIA_02)"
a11ynot_id: AX_ARIA_02
category: outils
gistID: f6897b666765ca1850d9
original_url: "http://a11ynot.com/nots/AX_ARIA_02.html"
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

<h2 aria-describedby="f6897b666765ca1850d9">Début de l'exemple</h2>
<div class="rendered-not">
<!-- Bad: typo in aria-labelledby value -->
<div id="my-label">Label for text input</div>
<input type="text" aria-labelledby="the-label"></input>
</div> <!-- rendered-not -->

<h2 aria-describedby="f6897b666765ca1850d9">Fin de l'exemple</h2>

<h3 aria-describedby="f6897b666765ca1850d9">Code de cet exemple</h3>
<script src="https://gist.github.com/f6897b666765ca1850d9.js"></script>
