<template>
  <div>
    <div>
      <tree id="tree" :data="tree" layoutType="circular"></tree>
    </div>
  </div>
</template>

<script>
import {tree} from 'vued3tree'

export default {
  components: {
    tree
  },
  data() {
    return {
      tree: {
        name: "father",
        children:[{
          name: "son1",
          children:[ {name: "grandson"}, {name: "grandson2"}], 
          cnt: 50
        },{
          name: "son2",
          children:[ {name: "grandson3"}, {name: "grandson4"}], 
          cnt: 50,
        }],
        cnt: 100
      }
    }
  }, 
}
</script>

<style scoped>
/* .node circle {
  fill: #fff;
  stroke: steelblue;
  stroke-width: 3px;
}

.node text { font: 12px sans-serif; }

.link {
  fill: none;
  stroke: #ccc;
  stroke-width: 2px;
} */
#tree {
  max-width: 500px;
  max-height: 500px;
  margin: auto;
}
</style>