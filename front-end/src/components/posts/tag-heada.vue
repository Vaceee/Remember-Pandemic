<template>
  <div class="pa-4">
    <v-chip class="ml-2" text-color="white"
              v-for="tag in tags" :key="tag" :color="tag.tagcolor"
              close close-icon="mdi-close" @click:close="close">
              <v-avatar left tile><v-icon>mdi-tag</v-icon></v-avatar>{{tag.tagname}}
            </v-chip>
            <v-chip class="ml-2" text-color="white"
              v-for="hottag in hottags" :key="hottag" :color="hottag.tagcolor"
              >
                <v-avatar left tile><v-icon>mdi-fire</v-icon></v-avatar>
                {{hottag.tagname}}
                <v-avatar right :color="hottag.tagcolor+' lighten-3'">{{hottag.hotness}}</v-avatar>
            </v-chip>
  </div>
</template>

<script>
export default {
  name: 'tagheada',
  data: () => ({
  }),
  props: {
    name: {
      type: String,
      required: true
    },
    tags: {
      type: Array,
      required: false
    },
    hottags: {
      type: Array,
      required: false
    }
  }
}
</script>

<style scoped>
:focus{
  outline: 0px;
}
</style>
