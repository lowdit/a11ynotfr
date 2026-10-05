---

title: "Faute de frappe dans aria-labelledby (aria-labeledby) (AX_ARIA_11)"
a11ynot_id: AX_ARIA_11
category: outils
gistID: 792c0ce0c42c82529c39
original_url: "http://a11ynot.com/nots/AX_ARIA_11.html"
layout: a11ynot
type: a11ynot
tags:
  - ainspector
  - axe
  - devtools
tag_labels:
  - AInspector Sidebar
  - aXe
  - Accessibility Developer Tools
---

<h2 aria-describedby="792c0ce0c42c82529c39">Début de l'exemple</h2>
<div class="rendered-not">
<!-- Bad: Labeled using incorrectly spelled aria-labeledby -->
<div id="address_label">Enter your address</div>
<input aria-labeledby="address_label">
</div> <!-- rendered-not -->

<h2 aria-describedby="792c0ce0c42c82529c39">Fin de l'exemple</h2>

<h3 aria-describedby="792c0ce0c42c82529c39">Code de cet exemple</h3>
<script src="https://gist.github.com/792c0ce0c42c82529c39.js"></script>
