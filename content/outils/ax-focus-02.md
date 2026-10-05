---

title: "Contrôles cliquables non atteignables au clavier (AX_FOCUS_02)"
a11ynot_id: AX_FOCUS_02
category: outils
gistID: 773000cae29e38d9b8a6
original_url: "http://a11ynot.com/nots/AX_FOCUS_02.html"
layout: a11ynot
type: a11ynot
tags:
  - ainspector
tag_labels:
  - AInspector Sidebar
---

<h2 aria-describedby="773000cae29e38d9b8a6">Début de l'exemple</h2>
<div class="rendered-not">
<!-- Bad: span with onclick attribute has no tabindex -->
<span onclick="submitForm();">Submit</span>

<!-- Bad: anchor element without href is not focusable -->
<a onclick="showNextPage();">Next page</a>
</div> <!-- rendered-not -->

<h2 aria-describedby="773000cae29e38d9b8a6">Fin de l'exemple</h2>

<h3 aria-describedby="773000cae29e38d9b8a6">Code de cet exemple</h3>
<script src="https://gist.github.com/773000cae29e38d9b8a6.js"></script>
