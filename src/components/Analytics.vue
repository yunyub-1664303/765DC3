<template>
  <div class="chart-wrapper">
    <div style="display: table-row; width: 100%">
        <chart :options="this.chartOptionsBar" style="display: table-cell; position: relative; left: 300px; overflow: scroll;"></chart>
        <chart :options="this.option2" style="display: table-cell; position: relative; left: 400px;"></chart>
    </div>
    <Tree @updatedRoot="updateChart"/>
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
          data: this.updateFineAxis(allData)[0],
          name: "category name",
          nameLocation: "center",
          nameTextStyle: {
            padding: [10, 0, 0, 0],
            fontSize: 16
          }
        },
        yAxis: {
          type: 'value',
          name: 'fineness: subProductCount / (numChildren + 1)',
          nameTextStyle: {
            padding: [0, 0, 0, 200],
            fontSize: 14
          }
        },
        series: [
          {
            type: 'bar',
            data: this.updateFineAxis(allData)[1]
          }
        ],
        title: {
          text: 'Fineness of Subcategories Under root',
          x: 'center',
          textStyle: {
            fontSize: 20
          }
        },
        color: ["#034f84"],
      },
      option2: {
        xAxis: {
          data: this.updateAxis(allData)[0],
          name: "average number of products in each subcategory",
          nameLocation: "center",
          nameTextStyle: {
            padding: [10, 0, 0, 0],
            fontSize: 12
          }
        },
        yAxis: {
          type: 'value',
          name: 'height: # of children levels',
          nameTextStyle: {
            padding: [0, 0, 0, 50],
            fontSize: 14
          }
        },
        series: [
          {
            type: 'bar',
            data: this.updateAxis(allData)[1]
          }
        ],
        title: {
          text: 'Height vs Fineness Under root',
          x: 'center',
          textStyle: {
            fontSize: 20
          }
        },
        color: ["#034f84"],
      }
    }
  },
  methods: {
    updateChart(selected) {
      this.chartOptionsBar.title.text = 'Fineness of Subcategories Under  ' + selected.name;
      var axis = this.updateFineAxis(selected);
      this.chartOptionsBar.xAxis.data = axis[0]
      this.chartOptionsBar.series = {type: 'bar', data: axis[1]};
      this.chartOptionsBar.color = ["#034f84"];

      this.option2.title.text = 'Height vs Fineness Under ' + selected.name;
      axis = this.updateAxis(selected);
      this.option2.xAxis.data = axis[0]
      this.option2.series = {type: 'bar', data: axis[1]};
      this.option2.color = ["#034f84"];
    },
    updateAxis(selected) {
      var aux = [];
      var xAxisName = [];
      var xAxis = [];
      var yAxis = [];
      for (var i = 0; i < selected.children.length; i++) {
        var curr = selected.children[i];
        aux.push({name: curr.name, fineness: curr.subcnt / (curr._children.length + 1), height: curr.height});
      }
      aux.sort(function(a, b) {return a.fineness - b.fineness;});
      for (i = 0; i < aux.length; i++) {
        xAxisName.push(aux[i].name);
        xAxis.push(aux[i].fineness);
        yAxis.push(aux[i].height);
        console.log(xAxisName[i] + ": " + yAxis[i])
      }
      return [xAxis, yAxis];
    },
    updateFineAxis(selected) {
      var aux = [];
      var xAxis = [];
      var yAxis = [];
      for (var i = 0; i < selected.children.length; i++) {
        var curr = selected.children[i];
        aux.push({name: curr.name, fineness: curr.subcnt / (curr._children.length + 1)});
      }
      aux.sort(function(a, b) {return a.fineness - b.fineness;});
      for (i = 0; i < aux.length; i++) {
        xAxis.push(aux[i].name);
        yAxis.push(aux[i].fineness);
        console.log(xAxis[i] + ": " + yAxis[i]);
      }
      return [xAxis, yAxis];
    }
  },
}
</script>

<style scoped>
/* .chart-wrapper {
  width: 100%;
  height: 700px;
}
.echarts {
  width: 100%;
  height: 100%;
} */

</style>