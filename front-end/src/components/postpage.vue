<template>
  <v-app>
    <div class="cont">
    <appbar></appbar>
    <sidedrawer></sidedrawer>
    <post></post>
    </div>
  </v-app>
</template>

<script>
import appbar from './general/appbar'
import sidedrawer from './general/sidedrawer'
import post from './posts/post'
export default {
  name: 'post-page',

  components: {
    appbar, sidedrawer, post
  },

  data: () => ({
  })
}
</script>

<style scoped>
.cont{
  background-color:#f9fafd;
  height: 100%;
}
</style>
