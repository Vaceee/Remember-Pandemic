<template>
  <v-app>
    <div class="cont">
    <class-list/>
    </div>
  </v-app>
</template>

<script>
import classList from './classes/classList'
export default {
  name: 'ClassesPage',
  components: {
    classList
  }
}
</script>

<style scoped>
.cont{
  background-color:#f1f2f5;
  height: 100%;
}
</style>
