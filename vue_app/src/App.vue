<template>
  <nav>
    <ul>
      <li>
        <router-link to="/">Home</router-link> 
      </li>
      <li>
        <router-link to="/sign-up">Sign Up</router-link> 
      </li>
      <li v-if="!isAnon">
        <router-link to="/log-in">Log In</router-link> 
      </li>
      <li v-if="isAnon">
        <router-link to="/sign-out">Sign Out</router-link>
      </li>
      <li>
        <router-link to="/product-list">Product List</router-link>
      </li>
    </ul>
  </nav>
  <router-view/>
  <p></p>
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
  },
  computed: {
    isAnon() {
      return this.$store.state.isAuthenticated
    }
  }
}
</script>

<style>
ul {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 1em;
  list-style-type: none;
}
a {
  text-decoration: none;
}
</style>