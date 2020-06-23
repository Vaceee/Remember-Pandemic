<template>
  <v-app>
    <div class="cont">
    <appbar></appbar>
    <sidedrawer></sidedrawer>
    <writebox></writebox>
    </div>
  </v-app>
</template>

<script>
import appbar from './general/appbar'
import sidedrawer from './general/sidedrawer'
import writebox from './write/writebox'
export default {
  name: 'post-page',
  components: {
    appbar, sidedrawer, writebox
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
