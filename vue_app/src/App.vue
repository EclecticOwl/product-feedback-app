<template>
  <hamBurger></hamBurger>
  <router-view></router-view>
</template>

<script>
import axios from 'axios'
import HamBurger from './components/HamBurger.vue'
export default {
  name: 'App',
  components: {
    HamBurger,
  },
  beforeCreate() {
    this.$store.commit('initializeStore')
    const token = this.$store.state.token
    if (token) {
      axios.defaults.headers.common['Authorization'] = 'Token ' + token
    } else {
      axios.defaults.headers.common['Authorization'] = ''
    }
  },
}
</script>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
</style>