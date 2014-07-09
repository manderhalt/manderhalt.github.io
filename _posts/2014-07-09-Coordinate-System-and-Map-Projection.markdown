---
layout: post
title:  "Coordinate Systems and Map Projections"
date:   2014-07-09 18:57:52
categories: GIS
comments: false
---
Coordinate systems and map projections

<div id="chart">
</div>

<script src="http://d3js.org/d3.v3.min.js"></script>
<script src="http://d3js.org/topojson.v1.min.js"></script>
<script>

var width = 960,
    height = 700;

var path = d3.geo.path()
    .projection(null);

var svg = d3.select("div#chart").append("svg")
    .attr("width", width)
    .attr("height", height);

d3.json("europ.json", function(error, europe) {
  if (error) return console.error(error);

  svg.insert("path", ".graticule")
      .datum(topojson.feature(europe, europe.objects.continent_Europe_subunits))
      .attr("class", "land")
      .attr("d", path);
});

d3.select(self.frameElement).style("height", height + "px");

</script>
