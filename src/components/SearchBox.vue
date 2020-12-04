<template>
  <div>
    <Dropdown
      :options="options"
      :disabled="false"
      name="categories"
      :maxItem="100"
      placeholder="Please select an option"
      @selected="update">
    </Dropdown>
  </div>
</template>

<script>
import Dropdown from 'vue-simple-search-dropdown';
import nodes from '../../data/all-nodes.json'
export default {
  components: { Dropdown },
  data() {
    return {
      options: nodes
    }
  }, 
  methods: {
    update(selected) {
      // console.log(selected);
      this.$emit('newSearch', selected);
    }
  }
}
</script>

<style>

</style>