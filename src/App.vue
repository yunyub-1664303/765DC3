<template>
  <div id="app">
    <h1>
      Amazon Categories Tree
    </h1>
    <BarChart/>
    
  </div>
</template>

<script>

import BarChart from './components/Analytics.vue'

export default {
  name: 'App',
  components: { BarChart }
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
