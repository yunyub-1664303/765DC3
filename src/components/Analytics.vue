<template>
  <div class="chart-wrapper">
    <chart :options="this.chartOptionsBar"></chart>
    <Tree @updatedRoot="updateTitle"/>
  </div>
</template>

<script>
import Tree from './Tree.vue';
import 'echarts/lib/component/title';
import allData from '../../data/all-data';
export default {
  name:'BarChart',
  components: { Tree },
  data () {
    return {
      chartOptionsBar: {
        xAxis: {
          data: ['Q1', 'Q2', 'Q3', 'Q4']
        },
        yAxis: {
          type: 'value'
        },
        series: [
          {
            type: 'bar',
            data: [63, 75, 24, 92]
          }
        ],
        title: {
          text: 'How Finely Divided Are Subcategories Under root',
          x: 'center',
          textStyle: {
            fontSize: 24
          }
        }
      },
      currentRoot: {name: allData.name, children: allData.children},
    }
  },
  methods: {
    updateTitle(selected) {
      console.log("in chart: " + selected.name)
      this.currentRoot = selected;
      this.chartOptionsBar.title.text = 'How Finely Divided Are Subcategories Under ' + this.currentRoot.name;
    },
  },
}
</script>

<style scoped>
.chart-wrapper {
  width: 100%;
  height: 700px;
}
.echarts {
  width: 100%;
  height: 100%;
}

</style>