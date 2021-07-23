<template>
<div class="home-bg">
  <v-content>
    <v-card flat color="transparent">
      <v-row v-if="$vuetify.breakpoint.smAndUp">
        <v-col class="py-0 bgr0r">
          <v-row class="mx-auto vertical">
            <nav-block />
          </v-row>
        </v-col>
        <v-col cols="5" class="bodyy">
          <info-block />
        </v-col>
      </v-row>

      <div v-else>
        <v-col>
          <v-row class="mx-auto">
            <nav-block small/>
          </v-row>
          <v-row>
            <div class="bodyy mx-auto">
              <info-block />
            </div>
          </v-row>
        </v-col>
      </div>
    </v-card>
  </v-content>
</div>
</template>

<script>
import ClassesPage from '../ClassesPage'
import navBlock from './navBlock'
import infoBlock from './infoBlock'
export default {
  name: 'homeNav',
  components: {
    navBlock,
    infoBlock
  },
  data: () => ({
    ClassesPage
  })
}
</script>

<style scoped>
.vertical{
  margin-top: 15%;
}
.home-bg{
  background: url("../../../public/wizard-city.jpg");
  height: 100%;
  width: 100%;
  background-size: cover;
  position: fixed;
}
</style>
