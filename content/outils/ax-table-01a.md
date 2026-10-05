---

title: "En-têtes de tableau manquants ou incohérents (AX_TABLE_01a)"
a11ynot_id: AX_TABLE_01a
category: outils
gistID: 42a9cd1ae7125e0b1e75
original_url: "http://a11ynot.com/nots/AX_TABLE_01a.html"
layout: a11ynot
type: a11ynot
tags:
  - ainspector
  - axe
tag_labels:
  - AInspector Sidebar
  - aXe
---

<h2 aria-describedby="42a9cd1ae7125e0b1e75">Début de l'exemple</h2>
<div class="rendered-not">
<!-- Bad: Table has incomplete header row -->
<table> 
  <tr>
    <th>Header</th>
    <th>Header</th>
    <td>Cell</td>
  </tr>
  <tr>
    <td>Cell</td>
    <td>Cell</td>
    <td>Cell</td>
  </tr>
</table>

<!-- Good: Table has incomplete header column -->
<table> 
  <tr>
    <td>Cell</td>
    <td>Cell</td>
    <td>Cell</td>
  </tr>
  <tr>
    <th>Header</th>
    <td>Cell</td>
    <td>Cell</td>
  </tr>
</table>

<!-- Bad: Table has no headers -->
<table> 
  <tr>
    <td>Cell</td>
    <td>Cell</td>
    <td>Cell</td>
  </tr>
  <tr>
    <td>Cell</td>
    <td>Cell</td>
    <td>Cell</td>
  </tr>
</table>
</div> <!-- rendered-not -->

<h2 aria-describedby="42a9cd1ae7125e0b1e75">Fin de l'exemple</h2>

<h3 aria-describedby="42a9cd1ae7125e0b1e75">Code de cet exemple</h3>
<script src="https://gist.github.com/42a9cd1ae7125e0b1e75.js"></script>
