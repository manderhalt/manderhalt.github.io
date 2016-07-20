d3.json("js/world.topo.json", function(error,world) {
    if (error) return console.error(error);
    console.log(world);
    var geom = topojson.feature(world, world.objects.countries).features;
    var width = parseInt(d3.select('header').style('width'), 10);
    var height = parseInt(d3.select('header').style('height'), 10);
    var svg = d3.select(".entete").append("svg")
        .attr("width", width)
        .attr("height", height)
        .attr('class','headermap')

    var projection = d3.geo.mercator()
        .scale(200)
        .center([0,45])
        .translate([width / 2, height / 2]);

    var path = d3.geo.path()
        .pointRadius(2)
        .projection(projection);

    var g = svg.append("g")

    g.selectAll(".subunit")
    .data(geom)
    .enter().append("path")
    .attr("class", "subunit")
    .attr("d", path)
    .style("fill-opacity",0)
    .style("stroke-opacity", 0)
    .transition()
    .duration(3000)
    .style("fill-opacity",function(d){
        return 0.05+Math.random()*0.15
    })
    .style("stroke-opacity",0.4)

    g.selectAll(".subunit")
        .on('mouseover',function(d) {
            d3.select(this)
            .style("fill-opacity",0.4)
        })
        .on('mouseout',function(d){
            d3.select(this)
            .transition()
            .duration(1000)
            .style("fill-opacity",function(){
                return 0.05+Math.random()*0.15
            })
        })

    g.selectAll(".subunit")


});
