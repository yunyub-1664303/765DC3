<template>
  <div id="app">
    <h1>
      Amazon Categories Tree
    </h1>
    <p>
      Welcome to Amazon Categories Visualizer! <br>
      If you want to explore certein category you have in mind, please type the category name in the search box below and select it from the popped-up options <br>
      Or, feel free to click on the nodes from the tree below the chart to explore what categories we have!
    </p>
    <SearchBox class="center" @newSearch="updateSearch"/>
    <ChartAndTree v-bind:search="this.search"/>
  </div>
</template>

<script>

import ChartAndTree from './components/Analytics.vue'
import SearchBox from './components/SearchBox.vue'
export default {
  name: 'App',
  components: { ChartAndTree,
  SearchBox }, 
  data() {
    return {
      search: ''
    }
  },
  methods: {
    updateSearch(search) {
      this.search = search;
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
