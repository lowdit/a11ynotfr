---

title: "Contraste insuffisant du texte (AX_COLOR_01)"
a11ynot_id: AX_COLOR_01
category: outils
gistID: 097599b455099e246b84
original_url: "http://a11ynot.com/nots/AX_COLOR_01.html"
layout: a11ynot
type: a11ynot
tags:
  - axe
tag_labels:
  - aXe
---

<h2 aria-describedby="097599b455099e246b84">Début de l'exemple</h2>
<div class="rendered-not">
<!-- Bad: small text with a contrast ratio of less than 4.5:1 -->
<p style="color: gray">  <!-- Contrast ratio 3.95:1 -->
Warning: this product should not be used by any minor without adult supervision.

<!-- Bad: large text with a contrast ratio of less than 3.0:1 -->
<h1 style="color: #BBB">Very subtle heading</h1>  <!-- Contrast ratio 1.92:1 -->
</div> <!-- rendered-not -->

<h2 aria-describedby="097599b455099e246b84">Fin de l'exemple</h2>

<h3 aria-describedby="097599b455099e246b84">Code de cet exemple</h3>
<script src="https://gist.github.com/097599b455099e246b84.js"></script>
