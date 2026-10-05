---

title: "Image informative sans alternative ou mal masquée (AX_TEXT_02)"
a11ynot_id: AX_TEXT_02
category: outils
gistID: 7afd836ce46ccdf3131e
original_url: "http://a11ynot.com/nots/AX_TEXT_02.html"
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

<h2 aria-describedby="7afd836ce46ccdf3131e">Début de l'exemple</h2>
<div class="rendered-not">
<!-- Bad: no alternative content provided for informative image -->
<img src="stateDiagram.jpg">

<!-- Bad: presentational image may not be hidden from assistive technology -->
<img src="horizontalLine.jpg">
</div> <!-- rendered-not -->

<h2 aria-describedby="7afd836ce46ccdf3131e">Fin de l'exemple</h2>

<h3 aria-describedby="7afd836ce46ccdf3131e">Code de cet exemple</h3>
<script src="https://gist.github.com/7afd836ce46ccdf3131e.js"></script>
