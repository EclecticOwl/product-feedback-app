<template>
    <div class="form-container">
        <form @submit.prevent="submitForm" class="form-main">
            <div>
                <h1>Sign up</h1>
            </div>
            <div class="form-input">
                <label for="username">Username:</label>
                <input type="email" name="username" v-model="username">
            </div>
            <div class="form-input">
                <label for="email">Email:</label>
                <input type="email" name="email" v-model="email">
            </div>
            <div class="form-input">
                <label for="password">Password:</label>
                <input type="password" name="password" v-model="password">
            </div>
            <div class="form-controls">
                <button @click.prevent="goBack">Go Back</button>
                <button type="submit">Sign Up</button>
            </div>

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
                    console.log(response)
                    this.$router.push('/log-in')
                })
                .catch(error => {
                    console.log(error)
                })
        },
        goBack() {
            this.$router.push('/')
        }
    }
}
</script>