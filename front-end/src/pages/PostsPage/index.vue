<template>
  <v-app>
    <div class="cont">
    <appBar></appBar>
    <sideDrawer></sideDrawer>
    <post-list/>
    </div>
  </v-app>
</template>

<script>
import appBar from '../../components/general/appBar'
import sideDrawer from '../../components/general/sideDrawer'
import postList from './postList'
export default {
  name: 'PostsPage',
  components: {
    appBar, sideDrawer, postList
  }
}
</script>

<style scoped>
.cont{
  background-color:#f4f5f7;
  height: 100%;
}
</style>
