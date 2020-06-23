<template>
  <v-app>
    <div class="cont">
    <appbar></appbar>
    <sidedrawer></sidedrawer>
    <classset></classset>
    </div>
  </v-app>
</template>

<script>
import appbar from './general/appbar'
import sidedrawer from './general/sidedrawer'
import classset from './classes/classset'
export default {
  name: 'classsetpage',

  components: {
    appbar, sidedrawer, classset
  },

  data: () => ({
  })
}
</script>

<style scoped>
.cont{
  background-color:#a5acd6;
  height: 100%;
}
</style>
