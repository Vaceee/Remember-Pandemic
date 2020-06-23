<template>
  <div>
    <v-row>
      <v-col cols="1"></v-col>
      <v-col cols="5">
        <navi-card
          :to="{
            name: ClassesPage.name
          }"
          color="pink"
          icon="mdi-school"
          title="课堂信息"
          :small="small"
        />
      </v-col>
      <v-col cols="5">
        <navi-card
          :to="{name: PostsPage.name}"
          color="light-blue"
          icon="mdi-city-variant"
          title="校园讨论"
          :small="small"
        />
      </v-col>
    </v-row>
  </div>
</template>

<script>
import ClassesPage from '../ClassesPage'
import PostsPage from '../PostsPage'
import naviCard from './naviCard'
export default {
  name: 'navBlock',
  props: {
    small: Boolean
  },
  components: {
    naviCard
  },
  data: () => ({
    ClassesPage,
    PostsPage
  })
}
</script>
