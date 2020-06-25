<template>
  <div>
    <v-app-bar
      app
      color="primary"
      light
      clipped-left
    >
      <div class="d-flex align-right">
        <v-img
          alt="Vuetify Logo"
          class="shrink mr-2"
          contain
          src="https://cdn.vuetifyjs.com/images/logos/vuetify-logo-dark.png"
          transition="scale-transition"
          width="40"
        />
      </div>

      <v-toolbar-title class="white--text display-1">
        OfCourse
      </v-toolbar-title>

      <v-spacer></v-spacer>

        <v-list
          dense
          nav
          dark
          color="colorful1"
          class="py-0"
        >
          <v-list-item v-bind:two-line="$vuetify.breakpoint.width>500" >
            <v-list-item-avatar :class="{'mx-auto':($vuetify.breakpoint.width<=500)}">
              <img src="../../../public/Nona1.png">
            </v-list-item-avatar>

            <v-list-item-content v-if="$vuetify.breakpoint.width>500">
              <v-list-item-title>{{username}}</v-list-item-title>
              <v-list-item-subtitle>我们首先应该善良，其次要诚实，再其次是永远不要相互遗忘。</v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>
        </v-list>
    </v-app-bar>
  </div>
</template>

<script>
export default {
  name: 'appBar',
  data: () => ({
    username: ''
  }),
  props: {
    name: {
      type: String,
      required: true
    }
  },
  mounted () {
    this.username = this.$store.getters.username
  }
}
</script>
