<template>
  <router-link class="link" :to="to">
    <v-card :color="color" class="pa-4 my-4" v-if="small">
      <v-icon x-large color="white">{{ icon }}</v-icon><br>
      <v-card-title class="white--text headline">{{ title }}</v-card-title>
    </v-card>
    <v-card :color="color" class="pa-4 mx-12 my-4" v-else>
      <v-icon x-large color="white">{{ icon }}</v-icon><br>
      <v-card-title class="white--text headline">{{ title }}</v-card-title>
    </v-card>
  </router-link>
</template>

<script>
export default {
  name: 'naviCard',
  props: {
    to: {
      type: [String, Object],
      required: true
    },
    color: {
      type: String,
      required: true
    },
    icon: {
      type: String,
      required: true
    },
    title: {
      type: String,
      required: true
    },
    small: {
      type: Boolean,
      required: false
    }
  }
}
</script>

<style scoped>
.link {
  text-decoration: none;
}
</style>
