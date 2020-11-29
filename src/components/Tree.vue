<template>
  <div>
    {{ drawTree(this.treeData) }}
  </div>
</template>

<script>
// import {tree} from 'vued3tree'
import data from '../../data/all-data'
// import data from '../../data/pet-data'
import * as d3 from 'd3';

export default {
  components: { },
  data() {
    return {
      selected: {"name": data.name, "height": data.height, "subcnt": data.subcnt},
      treeData: data,
      width: 1440,
      height: 30 * data.children.length
    }
  }, 
  methods: {
    drawTree(treeData) {
      
      
      this.update(treeData);

      d3.select(self.frameElement).style("height", "500px");
      console.log("in tree: " + this.selected.name)
      
    },
    // Toggle children on click.
    click(d) {
      if (d.children) {
        d._children = d.children;
        d.children = null;
      } else {
        d.children = d._children;
        d._children = null;
      }
      this.update(d);
      this.selected = {"name": d.name, "children": d.children, "height": d.height, "subcnt": d.subcnt};
      this.$emit('updatedRoot', this.selected)
    },
    drawLegend(svg) {
      // Add color annotations
      var circles = ['unselected', 'selected', 'no subcategories'];
      var itemWidth = 100;
      var itemHeight = 18;

      var legend = svg.selectAll(".legend")
        .data(circles)
        .enter()
        .append("g")
        .attr("transform", function(d,index) { return "translate(" + (1000 + index * itemWidth) + "," + itemHeight + ")"; })
        .attr("class","legend");

      legend.append('rect')
        .attr("width",15)
        .attr("height",15)
        .attr("fill", function(d) { 
          if (d === 'selected') {
            return "#034f84";
          } else if (d === "no subcategories") {
            return "#b2b2b2";
          }
          return "lightsteelblue"; 
        });
        
      legend.append('text')
        .attr("x", 20)
        .attr("y",12)
        .text(function(d) { return d; });
    },
    update(source) {
      // clear previous tree
      d3.select('svg').remove();
      // ************** Generate the tree diagram	 *****************
      var root = this.treeData;
      var margin = {top: 20, right: 20, bottom: 20, left: 200};
        // width = 1440,
        // height = 30 * root.children.length;
        

      var svg = d3.select("body").append("svg")
        .attr("width", this.width + margin.right + margin.left)
        .attr("height", this.height + margin.top + margin.bottom)
        .append("g")
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")")
        // .attr("transform", "translate(" + (margin.left + width/2) + "," + margin.top + ")");

      
      root.x0 = this.height / 2;
      root.y0 = 0;
        var i = 0,
        duration = 10;

      var tree = d3.layout.tree()
        .size([this.height, this.width]);

      var diagonal = d3.svg.diagonal()
        .projection(function(d) { return [d.y, d.x]; });
        // Compute the new tree layout.
        var nodes = tree.nodes(root).reverse(),
          links = tree.links(nodes);

        // Normalize for fixed-depth.
        nodes.forEach(function(d) { d.y = d.depth * 180; });

        // Update the nodes…
        var node = svg.selectAll("g.node")
          .data(nodes, function(d) { return d.id || (d.id = ++i); });

        // Enter any new nodes at the parent's previous position.
        var nodeEnter = node.enter().append("g")
          .attr("class", "node")
          .attr("transform", function() { return "translate(" + source.y0 + "," + source.x0 + ")"; })
          .on("click", this.click);

        nodeEnter.append("circle")
          .attr("r", 1e-6)
          .style("fill", function(d) { return d._children ? "lightsteelblue" : "#fff"; });

        nodeEnter.append("text")
          .attr("x", function(d) { return d.children || d._children ? -13 : 13; })
          .attr("dy", ".35em")
          .attr("text-anchor", function(d) { return d.children || d._children ? "end" : "start"; })
          .text(function(d) { return d.name; })
          .style("fill-opacity", 1e-6);

        // Transition nodes to their new position.
        var nodeUpdate = node.transition()
          .duration(duration)
          .attr("transform", function(d) { return "translate(" + d.y + "," + d.x + ")"; });

        nodeUpdate.select("circle")
          .attr("r", 10)
          .style("fill", function(d) { 
            if ((d._children == null && d.children.length == 0) || (d.children == null && d._children.length == 0)) {
              return "#b2b2b2";
            }
            return d._children ? "lightsteelblue" : "#034f84"; 
          });

        nodeUpdate.select("text")
          .style("fill-opacity", 1);

        // Transition exiting nodes to the parent's new position.
        var nodeExit = node.exit().transition()
          .duration(duration)
          .attr("transform", function() { return "translate(" + source.y + "," + source.x + ")"; })
          .remove();

        nodeExit.select("circle")
          .attr("r", 1e-6);

        nodeExit.select("text")
          .style("fill-opacity", 1e-6);

        // Update the links…
        var link = svg.selectAll("path.link")
          .data(links, function(d) { return d.target.id; })
          ;

        // Enter any new links at the parent's previous position.
        link.enter().insert("path", "g")
          .attr("class", "link")
          .attr("d", function() {
          var o = {x: source.x0, y: source.y0};
          return diagonal({source: o, target: o});
          })
          .attr("fill", "none")
          .attr("stroke", "#555")
          .attr("stroke-opacity", 0.4)
          .attr("stroke-width", 1.5);

        // Transition links to their new position.
        link.transition()
          .duration(duration)
          .attr("d", diagonal);

        // Transition exiting nodes to the parent's new position.
        link.exit().transition()
          .duration(duration)
          .attr("d", function() {
          var o = {x: source.x, y: source.y};
          return diagonal({source: o, target: o});
          })
          .remove();

        // Stash the old positions for transition.
        nodes.forEach(function(d) {
        d.x0 = d.x;
        d.y0 = d.y;
        });
        
        this.drawLegend(svg);
      }
  },
}
</script>

<style scoped>
/* .node circle {
  cursor: pointer;
  fill: #fff;
  stroke: steelblue;
  stroke-width: 1.5px;
}

.node text {
  font-size: 11px;
}

path.link {
  fill: none;
  stroke: #ccc;
  stroke-width: 1.5px;
} */

.node {
		cursor: pointer;
	}

.node circle {
  fill: #fff;
  stroke: steelblue;
  stroke-width: 3px;
}

.node text {
  font: 12px sans-serif;
}

.link {
  fill: none;
  stroke: #ccc;
  stroke-width: 2px;
}
/* svg#sky {
  height: 100px;
  width: 1100px;
  border:1px dotted #ccc;
  background-color: #ccc;
} */
</style>