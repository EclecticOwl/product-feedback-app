<template>
    <div class="log-in">
        <h1>Log In</h1>
        <form @submit.prevent="submitForm">
            <p>Are you sure you wish to sign out?</p>
            <button type="submit">Sign Out</button>
        </form>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'SignOut',
    methods: {
        submitForm() {
            const token = localStorage.getItem('token')
        axios
          .post('/auth/token/logout/', token)
          .then( () => {
              this.$store.commit('removeToken')
              localStorage.removeItem('token')
              this.$router.push('/')
              this.$forceUpdate
            })
            .catch(err => {
              console.log(err)
            })
        }
    }
}

</script>