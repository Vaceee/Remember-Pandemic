<template>
  <router-link class="link" :to="`/post/${id}`">
  <div>
    <v-hover>
    <template v-slot={hover}>
    <v-card :elevation="hover?10:4" class="ma-3 mx-auto">
      <v-container fluid class="pa-0">
        <v-row class="px-0">
          <v-col cols="7" class="py-0 pr-0">
            <v-card class="subtitle-1 px-3 py-1 heada accent--text font-weight-bold"
             flat tile>
              {{title}}
            </v-card>
          </v-col>
          <v-col class="py-0 pl-0">
            <v-card class="body-2 pa-2 foota author-time-container" flat tile>
              <v-icon dense>mdi-account-circle</v-icon>{{name+' '}}
              <v-icon dense>mdi-clock</v-icon>{{time}}
            </v-card>
          </v-col>
        </v-row>
        <v-row class="px-0">
          <v-col cols="10" class="py-0">
            <v-card class="body-2 px-3 pt-0" flat tile>
              {{content}}
            </v-card>
          </v-col>
          <v-col class="py-0 pl-5">
            <span class="right"><v-btn color="colorful2" class="ml-3" @click="writepost">删除</v-btn></span>
          </v-col>
        </v-row>
        <v-row class="px-0">
          <v-col class="py-1 mr-2">
            <v-card class="body-2 pa-2 foota" flat tile>
              {{'回复数：'+rep_cnt+' '}}
              {{'点击量：'+click_cnt}}
            </v-card>
          </v-col>
        </v-row>
        <v-row class="px-0">
          <v-col class="py-1 mr-2">
            <v-card class="foota" flat tile>
              <v-chip small class="ml-2" text-color="white"
               v-for="tag in tags" :key="tag" :color="tag.tagcolor">
                <v-avatar left tile><v-icon>mdi-tag-outline</v-icon></v-avatar>{{tag.tagname}}
              </v-chip>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-card>
    </template>
    </v-hover>
  </div>
  </router-link>
</template>

<script>
export default {
  name: 'postitem',
  data: () => ({
  }),
  props: {
    id: {
      type: String,
      required: true
    },
    title: {
      type: String,
      required: true
    },
    content: {
      type: String,
      required: true
    },
    name: {
      type: String,
      required: true
    },
    time: {
      type: String,
      required: true
    },
    rep_cnt: {
      type: String,
      required: true
    },
    click_cnt: {
      type: String,
      required: true
    },
    tags: {
      type: Array,
      required: false
    }
  }
}
</script>

<style scoped>
.heada{
  line-height: 45px;
}
.foota{
  text-align: right;
  white-space: pre;
}
.link{
  text-decoration: none;
}
.author-time-container {
  margin-left: 1em;
}
.ml-3{
  height: 5px;
}
</style>
