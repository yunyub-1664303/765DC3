<template>
  <div>
    <Dropdown
      :options="options"
      :disabled="false"
      name="categories"
      :maxItem="10"
      placeholder="Please select an option"
      @selected="update">
    </Dropdown>
  </div>
</template>

<script>
import Dropdown from 'vue-simple-search-dropdown';
import data from '../../data/all-data'
export default {
  components: { Dropdown },
  data() {
    return {
      options: data.children
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