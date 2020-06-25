<template>
  <div>
    <v-row>
      <v-col cols="2"></v-col>
      <v-col cols="5">
        <navi-card
          to="/section/1"
          color="pink"
          icon="mdi-virus"
          title="疫情通告"
          :small="small"
        />
      </v-col>
      <v-col cols="5">
        <navi-card
          to="/section/2"
          color="orange"
          icon="mdi-book"
          title="疫情日记"
          :small="small"
        />
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="2"></v-col>
      <v-col cols="5">
        <navi-card
          to="/section/3"
          color="purple"
          icon="mdi-city"
          title="抗疫行动"
          :small="small"
        />
      </v-col>
      <v-col cols="5">
        <navi-card
          :to="{name: ClassesPage.name}"
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
