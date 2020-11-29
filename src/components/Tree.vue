<template>
  <div>
    <body>
      <!-- <tree id="tree" :data="tree" :duration="1" @change="showBranch"></tree> -->
      {{ drawTree(this.treeData) }}
    </body>
  </div>
</template>

<script>
// import {tree} from 'vued3tree'
import data from '../../data/all-data'
// import data from '../../data/pet-data'
import * as d3 from 'd3';

export default {
  props: ['on'],
  components: {
    // tree
  },
  data() {
    return {
      treeData: data,
    }
  }, 
  methods: {
    showBranch(element) {
      console.log(element)
      element.data.children = element.data._children
    }, 
    drawTree(treeData) {
      // clear previous tree
       d3.select('svg').remove();
      // ************** Generate the tree diagram	 *****************
      root = treeData;
      var margin = {top: 20, right: 20, bottom: 20, left: 200},
        width = 1440,
        height = 30 * root.children.length;
        
      var i = 0,
        duration = 10,
        root;

      var tree = d3.layout.tree()
        .size([height, width]);
        // .size([10*height, width])
        // .separation(function separation(a, b) { return a.parent == b.parent ? 2 : 1; });

      var diagonal = d3.svg.diagonal()
        .projection(function(d) { return [d.y, d.x]; });

      var svg = d3.select("body").append("svg")
        .attr("width", width + margin.right + margin.left)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");
        // .attr("transform", "translate(" + (margin.left + width/2) + "," + margin.top + ")");

      
      root.x0 = height / 2;
      root.y0 = 0;
      update(root);

      d3.select(self.frameElement).style("height", "500px");

      function update(source) {

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
          .on("click", click);

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
      }

      // Toggle children on click.
      function click(d) {
        if ((d._children != null && d._children.length == 0) || (d.children != null && d.children.length == 0)) {
          alert('no subcategories under ' + d.name)
          return;
        }
        if (d.children) {
        d._children = d.children;
        d.children = null;
        } else {
        d.children = d._children;
        d._children = null;
        }
        update(d);
      }
      
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
div#container {
  height: 400px;
  width: 400px;
  border:2px solid #000;
  overflow: scroll;
 }
svg#sky {
  height: 100px;
  width: 1100px;
  border:1px dotted #ccc;
  background-color: #ccc;
}
</style>