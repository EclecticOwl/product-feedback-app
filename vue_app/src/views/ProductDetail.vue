<template>
  <div class="main-container">
    <div class="product-sidebar" v-if="product">
       <div class="product-sidebar-header">
            <div>
                <p class="product-title">Product: {{ product.title }}</p>
            </div>
            <div>
                <p class="product-owner">By: {{ product.owner }}</p>
            </div>
       </div>
    </div>
    <div class="product-container">
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'ProductDetail',
    data() {
        return {
            product: null
        }
    },
    created() {
            axios
                .get('/api/products/' + this.$route.params.id )
                .then(response =>  {
                    this.product = response.data
                })
                .catch(err => {
                    console.log(err)
                })
    },
}
</script>