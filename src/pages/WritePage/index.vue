<template>
  <v-app>
    <div class="cont">
    <appBar></appBar>
    <sideDrawer></sideDrawer>
    <writebox></writebox>
    </div>
  </v-app>
</template>

<script>
import appBar from '../../components/general/appBar'
import sideDrawer from '../../components/general/sideDrawer'
import writebox from './writebox'
export default {
  name: 'WritePage',
  components: {
    appBar, sideDrawer, writebox
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
