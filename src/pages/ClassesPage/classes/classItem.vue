<template>
  <router-link class="link" :to="`/section/${id}`">
  <v-card class="ma-3 classcard" hover :width="($vuetify.breakpoint.smAndUp)?'47%':'95%'" tile>
      <v-container class="pa-0">
        <v-row>
          <v-col class="pb-0 pr-0" :class="($vuetify.breakpoint.smAndUp)?'pl-10':'pl-5'"
           :cols="($vuetify.breakpoint.width<370 ||($vuetify.breakpoint.width>755 && $vuetify.breakpoint.width<900) )?7:
           ($vuetify.breakpoint.width>600 && $vuetify.breakpoint.width<755)?8:6">
            <v-card height="45px" color="transparent" style="line-height : 45px; " flat tile>
              <span class="headline accent--text">
                {{name}}</span>
            </v-card>
          </v-col>
          <v-col class="pb-0 pr-6 pl-0">
            <v-list-item>
              <v-list-item-content>
                <v-list-item-title class="righttext">{{teacher}}</v-list-item-title>
                <v-list-item-subtitle class="righttext"> {{time}}</v-list-item-subtitle>
              </v-list-item-content>
            </v-list-item>
          </v-col>
        </v-row>
        <v-row class="py-0">
          <v-col class="pt-0 pl-2">
          <v-chip v-for="hotpost in hotposts" :key="hotpost" label
            :color="hotpost.color" class="ml-4 mt-1" text-color="white">
            <v-avatar left tile><v-icon>mdi-file-document</v-icon></v-avatar>{{hotpost.title}}
          </v-chip>
          </v-col>
        </v-row>
      </v-container>
  </v-card>
  </router-link>
</template>

<script>
export default {
  name: 'classItem',
  props: {
    name: {
      type: String,
      required: true
    },
    id: {
      type: String,
      required: true
    },
    teacher: {
      type: String,
      required: true
    },
    time: {
      type: String,
      required: false
    },
    hotposts: {
      type: Array,
      required: false
    }
  }
}
</script>

<style scoped>
.classcard{
  float: left;
}
.righttext{
  text-align: right;
  white-space: pre;
}
</style>
