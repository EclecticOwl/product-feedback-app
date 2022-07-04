<template>
    <div class="log-in">
        <h1>Log In</h1>
        <form @submit.prevent="submitForm">
            <input type="email" name="username" v-model="username">
            <input type="password" name="password" v-model="password">
            <button type="submit">Sign In</button>
        </form>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    name: "LogIn",
    data() {
        return {
            username: '',
            password: '',
        }
    },
    methods: {
        submitForm() {
            const formData = {
                username:  this.username,
                password: this.password,
            }

            axios
                .post('/auth/token/login/', formData)
                .then( response => {
                    const token = response.data.auth_token
                    this.$store.commit('setToken', token)
                    axios.defaults.headers.common['Authorization'] = 'Token ' + token
                    localStorage.setItem('token', token)
                    this.$router.push('/')
                })
                .catch(err => {
                    console.log(err)
                })
        }
    }
}
</script>