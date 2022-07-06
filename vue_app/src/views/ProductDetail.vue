<template>
  <div class="main-container" v-if="product">
    <div class="product-sidebar">
        <div class="product-sidebar-header">
            <div class="product-description">
                <div>
                    <p class="product-title">{{ product.title }}</p>
                </div>
                <div>
                    <p class="product-owner">By: {{ product.owner }}</p>
                </div>
            </div>
        </div>
    </div>
    <div class="feedback-container" v-if="feedback">
        <div class="feedback-header" v-if="feedback_length">
            <p>{{feedback_length}}</p>
            <button @click="showFeedbackForm">Add Comment</button>
        </div>
        <div v-if="showForm">
            <form class="feedback-form" @submit.prevent="submitFeedback">
                <div>
                    <div class="feedback-input">
                        <label for="title">Title:</label>
                        <input v-model="title" type="text" name="title">
                    </div>
                    <div class="feedback-input">
                        <label for="description" name="description">Content:</label>
                        <textarea v-model="content" name="description" cols="16" rows="2"></textarea>
                    </div>
                    <div class="product-category">
                        <select name="category" v-model="category">
                            <option value="enhancement">Enhancement</option>
                            <option value="feature">Feature</option>
                            <option value="ui">UI</option>
                            <option value="ux">UX</option>
                            <option value="bug">Bug</option>
                        </select>
                    </div>
                </div>
                <div class="feedback-controls">
                    <button type="submit">Submit comment</button>
                </div>
            </form>
        </div>
        <div class="feedback-item" v-for="(item, index) in feedback" :key="index">
            <div class="feedback-upvotes">
                <div :id="item.id" @click="upvoter">
                    <svg width="10" height="7" xmlns="http://www.w3.org/2000/svg">
                    <path d="M1 6l4-4 4 4" stroke="#4661E6" stroke-width="2" fill="none" fill-rule="evenodd"/></svg>
                {{item.upvotes}}
                </div>
            </div>
            <div class="feedback-content">
                <p class="feedback-title">{{item.title}}</p>
                <p class="feedback-description">{{item.description}}</p>
                <p class="feedback-category">{{item.category}}</p>
            </div>
        </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'ProductDetail',
    data() {
        return {
            product: null,
            feedback_length: null,
            showForm: false,
            feedback: null,
            title: null, 
            content: null,
            category: null,
        }
    },
    created() {
            this.getData()
    },
    methods: {
        showFeedbackForm() {
            this.showForm = !this.showForm
        },
        submitFeedback() {
            const formData = {
                title:  this.title,
                description: this.content,
                category: this.category,
                product_id:  parseInt(this.$route.params.id)
            }
            console.log(formData)
            const token = localStorage.getItem('token')
            axios
                .post('/api/feedback/', formData , 'Authorization:  Token ' , token)
                .catch(err => {
                    console.log(err)
                })
            this.title = ''
            this.content = ''
            this.description = null
            this.showFeedbackForm()
            this.getData()
        }, 
        getData() {
            axios
                .get('/api/products/' + this.$route.params.id )
                .then(response =>  {
                    this.product = response.data
                    this.feedback = this.product.feedback
                    const len = response.data.feedback.length
                    if (len > 1) {
                        this.feedback_length = len + ' Comments'
                    }else {
                        this.feedback_length = len + ' Comment'
                    }
                })
                .catch(err => {
                    console.log(err)
                })
        },
        upvoter(e) {
            const token = localStorage.getItem('token')
            let number = parseInt(e.target.innerText) + 1
            
            const formData = {
                upvotes: number
            }
            axios
                .put('/api/feedback/' + e.target.id + '/' , formData , ' Authorization: Token ' , token)
                .catch(err => {
                    console.log(err)
                })
        }
        
     },
}
</script>

<style lang="sass">
.feedback-container
    display: flex
    flex-direction: column
    .feedback-header
        background-color: #383E65
        color: white
        margin-bottom: 1.5em
        border-radius: .5em
        display: flex
        align-items: center
        justify-content: space-between
        padding: 1em 2em
        box-shadow: 1px 1px 4px grey
    
    button
        background-color: #9F2DE3
        border: none
        padding: .5em 1em
        border-radius: 1em
        color: white
    button:hover
        cursor: pointer
    
    .feedback-form
        background-color: white
        padding: 1em
        display: flex
        justify-content: space-between
        box-shadow: 1px 1px 4px grey
        margin-bottom: 1em
        border-radius: .5em
    .feedback-input
        display: flex
        justify-content: space-between
        gap: 1em
        align-items: center
        margin-bottom: .25em
    
    input, textarea
        border-radius: 1em
        border: 1px solid #383E65
        box-shadow: 1px 1px 4px grey
        padding: .4em
    .product-category
        display: flex
        justify-content: center
        align-items: center
    .feedback-controls
        display: flex
        justify-content: center
        align-items: center
        button
            height: 40px
    select
        margin-top: .5em
        padding: .5em
        border-radius: .5em 
.feedback-item
    padding: 0 3em
    padding-top: 1em
    background-color: white
    height: 150px
    display: grid
    gap: 4em
    grid-template-columns: 1fr 8fr
    border-radius: 1em
    box-shadow: 1px 1px 4px grey
    margin-bottom: 1em
    .feedback-content
        display: flex
        flex-direction: column
        gap: .5em
    .feedback-category
        font-weight: 900
        border-radius: 1em
        padding: 0 .5em
        font-size: .6em
        width: fit-content
        background-color: #F3F4FE
        color: #8A8EE7
    .feedback-title
        font-weight: bold

    .feedback-upvotes
        display: flex
        justify-content: center
        align-items: center
        div
            display: flex
            gap: .25em
            flex-direction: column
            background-color: #F3F4FE
            padding: .75em
            border-radius: .5em
.product-description
    display: flex
    flex-direction: column
    width: 100%
    justify-content: flex-end
    padding-left: 1em
    .product-owner
        font-size: .5em
</style>