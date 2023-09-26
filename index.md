---
layout: default
title: Passion Project
---
<style>
  p{font-family: sans-serif;}
  hr{background-color: #7e92d6;}
  .color{color:#7e92d6;}
  body {
    padding: 25px;
    background-color: #282b30;
    color: #7e92d6;
    font-size: 16px;
    transition-duration: 0.2s;
  }
  hr{background-color: #7e92d6;}
  .board {
      display: grid;
      grid-template-columns: repeat(3, 100px);
      grid-gap: 2px;
    }
    .cell {
      width: 100px;
      height: 100px;
      border: 1px solid #7e92d6;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 24px;
      cursor: pointer;
    }
</style>


<script>
  
var IsLoggedIn1 = "true";
function myFunction() {
  var element = document.body;
  element.classList.toggle("dark-mode");
  var elem = document.querySelectorAll("#border");
  elem.forEach(function(border) {
    border.classList.toggle("border-dark");
    });
  var bars = document.querySelectorAll("#bar");
  bars.forEach(function(bar) {
    bar.classList.toggle("bar-dark");
    });
  var cellz = document.querySelectorAll("#cells");
  cellz.forEach(function(cells) {
    cells.classList.toggle("cell");
    cells.classList.toggle("cells-dark");
    });
}
</script>


<p style="font-size:36px;font-weight:bold"> Insert Basketball Game Here </p>

<!-- | Period   | Class   |
| -------- | ------- |
| 1        | [AP Calc](https://docs.google.com/document/d/1y261HMZAvWUGejSBIOL2xiuVJkLcg_qR/edit)    |
| 2        | [AP World](https://docs.google.com/document/d/1lURCs6UhD6cJ7ld4NrLNDUb-6VuKnC1r8UTJq3j2KOw/edit)     |
| 3        | [Honors Humanities](https://poway.instructure.com/courses/141205/pages/august-2023)    |
| 4        | [AP Physics](https://poway.instructure.com/courses/141173)   |
| 5        | [AP CSP](https://poway.instructure.com/courses/141645)     | -->
