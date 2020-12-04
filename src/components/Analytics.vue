<template>
  <div style="display: table-row; width: 100%">
    <chart :options="this.fvscat" @click="this.click" style="display: table-cell; position: relative; left: 100px;"></chart>
    <chart :options="this.hvsf" @click="this.click" style="display: table-cell; position: relative; left: 200px;"></chart>
    <Tree @updatedRoot="updateChart" v-bind:search="this.search"/>
  </div>
</template>

<script>
import Tree from './Tree.vue';
import 'echarts/lib/component/tooltip';
import 'echarts/lib/component/title';
import allData from '../../data/all-data';

export default {
  name:'BarChart',
  components: { Tree,
     },
  props: ['search'],
  data () {
    return {
      // bar: getBar(),
      fvscat: {
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
        series: {
          type: 'bar',
          data: this.updateFineAxis(allData)[1]
        },
        title: {
          text: 'Fineness of Subcategories Under root',
          x: 'center',
          textStyle: {
            fontSize: 20
          }
        },
        color: ["#034f84"],
        tooltip: {
          trigger: 'axis',
        },
      },
      hvsf: {
        xAxis: {
          data: this.updateAxis(allData)[0],
          name: "category name (sorted by increasing fineness)",
          nameLocation: "center",
          nameTextStyle: {
            padding: [10, 0, 0, 0],
            fontSize: 16
          },
        },
        yAxis: {
          type: 'value',
          name: 'height: # of children levels (including self)',
          nameTextStyle: {
            padding: [0, 0, 0, 50],
            fontSize: 14
          }
        },
        series: {
          type: 'bar',
          data: this.updateAxis(allData)[1]
        },
        title: {
          text: 'Height vs Fineness Under root',
          x: 'center',
          textStyle: {
            fontSize: 20
          }
        },
        color: ["#034f84"],
        
        tooltip: {
          trigger: 'axis',
        },
      },
    }
  },
  methods: {
    click (bar) {
      var index = bar.dataIndex;
      if (this.fvscat.series.data[index].itemStyle.color === '#fc0000') {
        // remove highlights
        this.fvscat.series.data[index].itemStyle.color = '#034f84';
        this.hvsf.series.data[index].itemStyle.color = '#034f84';
      } else {
        // remove previous highlights
        for (var i = 0; i < this.fvscat.series.data.length; i++) {
          this.fvscat.series.data[i].itemStyle.color = '#034f84';
          this.hvsf.series.data[i].itemStyle.color = '#034f84';
        }
        // highlight the clicked one
        this.fvscat.series.data[index].itemStyle.color = '#fc0000';
        // highlight the corresponding one
        this.hvsf.series.data[index].itemStyle.color = '#fc0000';
      }
      
    },
    updateChart(selected) {
      this.fvscat.title.text = 'Fineness of Subcategories Under ' + selected.name;
      var axis = this.updateFineAxis(selected);
      this.fvscat.xAxis.data = axis[0]
      this.fvscat.series = {type: 'bar', data: axis[1]};
      this.fvscat.color = ["#034f84"];

      this.hvsf.title.text = 'Height vs Fineness Under ' + selected.name;
      axis = this.updateAxis(selected);
      this.hvsf.xAxis.data = axis[0]
      this.hvsf.series = {type: 'bar', data: axis[1]};
      this.hvsf.color = ["#034f84"];
    },
    updateAxis(selected) {
      var aux = [];
      var xAxisName = [];
      // var xAxis = [];
      var yAxis = [];
      for (var i = 0; i < selected.children.length; i++) {
        var curr = selected.children[i];
        aux.push({name: curr.name, fineness: curr.subcnt / (curr._children.length + 1), height: curr.height});
      }
      aux.sort(function(a, b) {return a.fineness - b.fineness;});
      for (i = 0; i < aux.length; i++) {
        xAxisName.push(aux[i].name);
        // xAxis.push(aux[i].fineness);
        yAxis.push({value: aux[i].height + 1, itemStyle: {color: "#034f84"}});
        // console.log(xAxisName[i] + ": " + yAxis[i])
      }
      return [xAxisName, yAxis];
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
        yAxis.push({value: aux[i].fineness, itemStyle: {color: "#034f84"}});
        // console.log(xAxis[i] + ": " + yAxis[i]);
      }
      return [xAxis, yAxis];
    }
  },
}
</script>

<style >
.center {
  display: block;
  margin-left: auto;
  margin-right: auto;
  width: 17%;
}

</style>