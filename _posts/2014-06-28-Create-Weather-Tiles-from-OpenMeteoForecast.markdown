---
layout: post
title:  "Create Weather Tiles from OpenMeteoForecast"
date:   2014-06-28 15:30:00
categories: Leaflet
comments: true
post_view: 2014-06-28-Create-Weather-Tiles-from-OpenMeteoForecast.png
publish: false
---

[OpenMeteoForecast][OpenMeteoForecast-Site] is a project ruled by the [OpenMeteoFundation][OpenMeteoFundation-Site]. It provides open numerical weather forecasts over Europe with the WRF-ARW model on a 12 km grid.

The model runs 4 times a day for the next 72 hours with hourly predictions. Data can be accessed through [OPeNDAP server][OPeNDAP-server-Site] or by downloading [NetCDF files][NetCDF-files-Site] directly from the server.

Spatial gridded data arrays are beautiful but they can be easily enhanced by creating tile layers on a map powered by ![Leaflet](/images/logos/leaflet.png){: style="height:25px;margin-bottom:-5px"}. That's what we are going to do!

<script src="http://cdn.leafletjs.com/leaflet-0.7.3/leaflet.js"></script>
<script type="text/javascript" src="data.json"></script>
<div id="map"> </div>
<script type="text/javascript">
    var map = L.map('map').setView([47, 3], 3);
    L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            maxZoom: 18
            }).addTo(map);    L.tileLayer('http://localhost:8080/src/2014-06-28-Create-Weather-Tiles-from-OpenMeteoForecast/tile/{z}/{x}/{y}.png',{tms: true,opacity: 0.8}).addTo(map);
</script>


Load data from the [OPeNDAP server][OPeNDAP-server-Site]
===========================================================

The [OpenMeteoForecast][OpenMeteoForecast-Site] [OPeNDAP server][OPeNDAP-server-Site] provides a list of all available simulations.

Two solutions for us:
1. Download directly a `.nc` file
2. Parse a `.nc` file to get only the data we need with the server API.

Each `.nc` file weights 280 Mo. So the second one seems to be the best one!

First, import the following useful python packages. If they are not already installed, use [pip][pip-Site] or another package manager.

{% highlight python %}
import re
from bs4 import BeautifulSoup
from urllib2 import urlopen

{% endhighlight %}

Then, parse the content of the server webpage to get all available simulations files names. In order to do this, I use [BeautifulSoup][BeautifulSoup-Site] and some regular expressions to filter html results.

{% highlight python linenos=table %}

reg_grid = re.compile('eu12-pp')
reg_ext = re.compile('$nc')
reg_date = re.compile('[20]\d\d\d\d\d\d\d\d\d')
response = urlopen('http://dap.ometfn.net/')
html = response.read()
# Parse the html page of the server to find available files
soup = BeautifulSoup(html)
files = [l.get('href') for l in soup.find_all('a') if l.get('href')]
# Filter noisy names with regular expressions
files2 = [l for l in files if reg_grid.search(l) and l.endswith('.nc')]
print "And the winner is: ", (files2[0])

{% endhighlight %}

When I wrote this post, the file `http://dap.omd.li/eu12-pp_2014062806_72.nc` was available, but files are deleted every day on the server for storage space reasons. Use the previous chunck to get an available file name!










[BeautifulSoup-Site]: http://www.crummy.com/software/BeautifulSoup/
[pip-Site]: https://pip.pypa.io/en/latest/installing.html
[OpenMeteoFundation-Site]: http://openmeteofoundation.org/
[OpenMeteoForecast-Site]:https://openmeteoforecast.org/wiki/Main_Page
[OPeNDAP-server-Site]: http://www.opendap.org/
[NetCDF-files-Site]: http://dap.ometfn.net/
[Leaflet-Site]: http://leafletjs.com/
