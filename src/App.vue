<template>
  <div id="app">
    <h1>
      Amazon Categories Tree
    </h1>
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
