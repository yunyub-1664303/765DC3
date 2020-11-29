<template>
  <div class="chart-wrapper">
    <chart :options="chartOptionsBar"></chart>
  </div>
</template>

<script>
import 'echarts/lib/component/title';
export default {
  name:'BarChart',
  props: ['currentRoot'],
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
          text: this.getTitle(),
          x: 'center',
          textStyle: {
            fontSize: 24
          }
        }
      }
    }
  },
  methods: {
    getTitle() {
      console.log("in chart: " + JSON.stringify(this.currentRoot))
      return 'How Finely Divided Are Subcategories Under ' + this.currentRoot.name;
    }
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