<template>
   <div class="main-container">
    <h2>Product List</h2>
    <div class="product-list-container">
        <div v-for="item in array" :key="item.id">
            <p>{{ item.title }}<span> by: {{ item.owner }}</span></p>
        </div>
    </div>
   </div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'ProductList',
    data() {
        return {
            array: null
        }
    },
    created() {
            axios
                .get('/api/products/')
                .then(response =>  {
                    this.array = response.data
                })
                .catch(err => {
                    console.log(err)
                })
    }
}
</script>
<style>
.main-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
}
.product-list-container {
    width: 100%;
    display: grid;
    grid-template-columns: 1fr 1fr;
    justify-items: center;
}

</style>