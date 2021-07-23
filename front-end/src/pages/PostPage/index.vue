<template>
  <v-app>
    <div class="cont">
    <appBar></appBar>
    <sideDrawer></sideDrawer>
    <post></post>
    </div>
  </v-app>
</template>

<script>
import appBar from '../../components/general/appBar'
import sideDrawer from '../../components/general/sideDrawer'
import post from './posts/post'
export default {
  name: 'PostPage',
  components: {
    appBar, sideDrawer, post
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
