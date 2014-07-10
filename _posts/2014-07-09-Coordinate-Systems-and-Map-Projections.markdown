---
layout: post
title:  "Coordinate Systems and Map Projections"
date:   2014-07-09 18:57:52
categories: GIS
comments: false
post_view: 2014-07-09-Coordinate-Systems-and-Map-Projections.png
publish: false
---

A coordinate system is used to describe positions on the earth. A projection is a way of representing a 3d Sphere on a 2d plane. Basic? Yes, but only for experts in Geographical Information Systems (GIS). For us, a few tips could help before diving.

<h1> Coordinate systems </h1>

Coordinates of your GPS are not the only geographic coordinate system. As a matter of fact, locating points on a perfect sphere without shift is very simple. Locating points on the earth is more difficult, at least for two reasons. First, the earth is not a perfect sphere but an imperfect ellipsoid. Second, the sea level is not a good estimator of the earth surface reference.

Today, the 1984 revision of the Word Geodetic System (WGS84) is the reference in cartography and it is used by GPS. But because of the Earth geometrical imperfections, other datums can give more accurate positions. Be sure that a lot of coordinates systems have been created.

Defining a geographic coordinate system is not a simple task. It asks to define the shape and other parameters. For an ellipsoid for instance, the semi-major axis, the semi-minor axis, the inverse flattening and so on.

To sort out coordinates systems, the [EPSG][epsg] reference has been created. It is a collection of definitions of coordinate reference systems that are recognized by most of geographic libraries.


{% include posts/2014-07-09-Coordinate-Systems-and-Map-Projections.html %}
Animation by [mbostock][gistproj] 


[gistproj]:http://bl.ocks.org/mbostock/3711652
[epsg]: http://www.epsg.org/
