<template>
     <div class="home-container">
        <p>You can check out a link to the products to review <a @click.prevent="this.$router.push('/product')">here</a>.</p>
        <p>Or you can see a random product <a @click.prevent="randomProduct">here</a>.</p>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'HomeView',
    methods: {
        randomProduct() {
            axios.get('/api/randproduct/')
            .then(rep => {
                this.$router.push('/product/' + rep.data.id + '/')
                })
            .catch(err => {console.log(err)})
        }
    }

}
</script>

<style lang="sass">
.home-container
    margin-top: 5em
    display: flex
    flex-direction: column
    justify-content: center
    align-items: center
    gap: 2em
    a
        text-decoration: underline
        color: blue
</style>