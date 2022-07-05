<template>
  <HamBurger class="mobile-menu"></HamBurger>
  <NavBar class="main-menu"></NavBar>
  <router-view></router-view>
</template>

<script>
import axios from 'axios'
import HamBurger from './components/HamBurger.vue'
import NavBar from './components/NavBar.vue'
export default {
  name: 'App',
  components: {
    HamBurger,
    NavBar,
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

<style lang="sass">
* 
  margin: 0
  padding: 0
  box-sizing: border-box

body
  line-height: 1.5em
  background-color: #f8f8ff


@media (max-width: 701px)
  .main-menu
    display: none
  .form-main
    height: 300px
    width: 300px

@media (min-width: 700px) 
  .mobile-menu 
    display: none
  .form-main
    margin-right: 10em
    height: 300px
    width: 100%
    border-radius: 0 1em 1em 0

.form-main
  background-color: white
  border: 1px solid black
  display: flex
  flex-direction: column
  align-items: center
  justify-content: center
  gap: 2em
  border-radius: 1em

.form-input
  display: flex
  gap: 2em
  input
    padding: 0 .5em
    border-radius: .5em
    border: none
    border-bottom: 1px solid black
    background-color: lavender
  .input-color:focus
    outline: 2px solid purple
.form-controls
  display: flex
  gap: 1em
  button
    width: 75px
    height: 30px
    border-radius: 1em
    border: none

</style>