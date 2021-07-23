<template>
  <v-app>
    <div class="cont">
    <app-bar/>
    <side-drawer/>
    <router-view/>
    </div>
  </v-app>
</template>

<script>
import appBar from '../../components/general/appBar'
import sideDrawer from '../../components/general/sideDrawer'
export default {
  name: 'HomePage',
  components: {
    appBar,
    sideDrawer
  }
}
</script>

<style scoped>
.cont{
  background-color:#f9fafd;
  height: 100%;
}
</style>
