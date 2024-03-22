---
headerVersion: 2023.11.25
tags: [place, status/needswork]
displayDefaults: {ruledBy: 'Ruled by: <name> <((since )startDate())>'}
name: Sembara
typeOf: realm
whereabouts: Western Green Sea Region
title: Sembara
---
# Sembara
<div class="grid cards ext-narrow-margin ext-one-column" markdown>
-    :octicons-location-24:{ .lg .middle } A realm in the [Western Green Sea Region](<../../western-green-sea/western-green-sea-region.md>)  
</div>


<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"
integrity="sha256-20nQCchB9co0qIjJZRGuk2/Z9VM+kNiyxNV1lvTlZBo=" crossorigin="" ></script>


<div id="region-map-sembara" class="ext-map-container"></div>

<script type="text/javascript">
    document.addEventListener("DOMContentLoaded", function () {

            var map = L.map('region-map-sembara', {
                crs: L.CRS.Simple,
                minZoom: -1,
                maxZoom: 3
            });

            
            // this bounds must be in the form [y,x], [y,x]
            // it will typically be, in the yaml, 
            // bounds:
            //  - [0,0]
            //  - [100,100]

            var bounds = [[[0, 0], [2468, 2308]]];

            // this has to be the path, i.e. what was working for me was /assets/world-map-01-02.png
            var image = L.imageOverlay('/taelgarverse1720/assets/sembara-regions.png', bounds).addTo(map);
            map.setView( [1200, 1200], 0);
        })
</script>







