---

title: "État ARIA obligatoire manquant (case à cocher) (AX_ARIA_03)"
a11ynot_id: AX_ARIA_03
category: outils
gistID: 97244f670e69d8e430cc
original_url: "http://a11ynot.com/nots/AX_ARIA_03.html"
layout: a11ynot
type: a11ynot
tags:
  - axe
  - devtools
tag_labels:
  - aXe
  - Accessibility Developer Tools
---

<h2 aria-describedby="97244f670e69d8e430cc">Début de l'exemple</h2>
<div class="rendered-not">
<!-- Bad: the checkbox role requires the aria-checked state -->
<span role="checkbox" aria-labelledby="foo" tabindex="0"></span>
</div> <!-- rendered-not -->

<h2 aria-describedby="97244f670e69d8e430cc">Fin de l'exemple</h2>

<h3 aria-describedby="97244f670e69d8e430cc">Code de cet exemple</h3>
<script src="https://gist.github.com/97244f670e69d8e430cc.js"></script>
