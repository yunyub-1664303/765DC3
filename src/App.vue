<template>
  <div id="app">
    <h1>
      Amazon Categories Tree
    </h1>
    <SearchBox class="center"/>
    <ChartAndTree/>
    
  </div>
</template>

<script>

import ChartAndTree from './components/Analytics.vue'
import SearchBox from './components/SearchBox.vue'
export default {
  name: 'App',
  components: { ChartAndTree,
  SearchBox }
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
.center {
  display: block;
  margin-left: auto;
  margin-right: auto;
  width: 17%;
}
</style>
