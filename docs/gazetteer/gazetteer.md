---
headerVersion: 2023.11.25
tags: [background]
hide: [toc, navigation]
name: Map of Taelgar
title: Map of Taelgar
---
# Map of Taelgar

<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"
integrity="sha256-20nQCchB9co0qIjJZRGuk2/Z9VM+kNiyxNV1lvTlZBo=" crossorigin="" ></script>


<div id="world-of-taelgar" class="ext-map-container"></div>

<script type="text/javascript">
    document.addEventListener("DOMContentLoaded", function () {

            var map = L.map('world-of-taelgar', {
                crs: L.CRS.Simple,
                minZoom: -2,
                maxZoom: 2
            });

            
            // this bounds must be in the form [y,x], [y,x]
            // it will typically be, in the yaml, 
            // bounds:
            //  - [0,0]
            //  - [100,100]

            var bounds = [[[0, 0], [5156.7, 6636.233]]];

            // this has to be the path, i.e. what was working for me was /assets/world-map-01-02.png
            var image = L.imageOverlay('/taelgarverse1720/assets/taelgar-world-map.png', bounds).addTo(map);
            map.setView( [3333, 2000], -1);
        })
</script>


