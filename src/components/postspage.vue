<template>
  <v-app>
    <div class="cont">
    <appbar></appbar>
    <sidedrawer></sidedrawer>
    <postlist></postlist>
  </div>
  </v-app>
</template>

<script>
import appbar from './general/appbar'
import sidedrawer from './general/sidedrawer'
import postlist from './posts/postlist'
export default {
  name: 'postspage',

  components: {
    appbar, sidedrawer, postlist
  },

  data: () => ({
  })
}
</script>

<style scoped>
.cont{
  background-color:#f4f5f7;
  height: 100%;
}
</style>
