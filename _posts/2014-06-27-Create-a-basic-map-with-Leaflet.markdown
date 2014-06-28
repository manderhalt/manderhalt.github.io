---
layout: post
title:  "Create a basic map with Leaflet"
date:   2014-06-27 23:08:52
categories: Leaflet
---
This post explains in a nutshell how to create maps with [Leaflet][leaflet-site]

{% include map.html %}

First, include the `.css` and the `.js` in the `<head>` section of your `.html` page,

{% highlight html %}
<head>
    <meta charset="utf-8">
    ...
    <link rel="stylesheet" href="http://cdn.leafletjs.com/leaflet-0.7.3/leaflet.css" />
    <script src="http://cdn.leafletjs.com/leaflet-0.7.3/leaflet.js"></script>
</head>

{% endhighlight %}

and create a `div`element.


{% highlight html %}

<div id="map"> </div>

{% endhighlight %}

With the following lines, create the map and add it to the `div` element that has been previously created.

{% highlight JavaScript %}

<script type="text/javascript">
    var map = L.map('map').setView([47, 0.9], 6);
    L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
    {
        maxZoom: 18,
      }).addTo(map);
</script>

{% endhighlight %}

[leaflet-site]: http://leafletjs.com
