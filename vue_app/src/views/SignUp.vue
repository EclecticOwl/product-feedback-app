<template>
    <div class="sign-up">
        <h1>Sign up</h1>

        <form @submit.prevent="submitForm">
            <input type="email" name="username" v-model="username">
            <input type="email" name="email" v-model="email">
            <input type="password" name="password" v-model="password">
            <button type="submit">Sign Up</button>

        </form>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: "SignUp",
    data() {
        return {
            username: '',
            password: '',
            email: '',
        }
    },
    methods: {
        submitForm() {
            const formData = {
                username: this.username,
                password: this.password,
                email: this.email,
            }

            axios
                .post('/auth/users/', formData)
                .then(response => {
                    this.$router.push('/log-in')
                    console.log(response)
                })
                .catch(error => {
                    console.log(error)
                })
        }
    }
}
</script>