<template>
    <nav>
    <ul>
      <li><router-link to="/">Home</router-link></li>
      <li><router-link to="/sign-up">Sign Up</router-link></li>
      <li v-if="!isAnon"><router-link to="/log-in">Log In</router-link></li>
      <li v-if="isAnon"><router-link to="/sign-out">Sign Out</router-link></li>
      <li><router-link to="/product-list">Product List</router-link></li>
    </ul>
  </nav>
</template>

<script>
export default {
    name: 'NavBar',
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
  gap: 1em;
  list-style-type: none;
}
a {
  text-decoration: none;
}
</style>