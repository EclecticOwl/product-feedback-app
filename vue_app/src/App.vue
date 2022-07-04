<template>
  <nav>
    <router-link to="/sign-up">Sign Up</router-link> |
    <router-link to="/log-in">Log In</router-link>
  </nav>
  <router-view/>
</template>

<script>
import axios from 'axios'

export default {
  name: 'App',
  beforeCreate() {
    this.$store.commit('initializeStore')

    const token = this.$store.state.token

    if (token) {
      axios.defaults.headers.common['Authorization'] = 'Token ' + token
    } else {
      axios.defaults.headers.common['Authorization'] = ''
    }
  }
}
</script>