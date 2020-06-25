<template>
  <div>
    <div v-if="($vuetify.breakpoint.smAndUp)">
      <div @mouseenter="hover=true" @mouseleave="hover=false">
        <v-navigation-drawer
          app
          clipped
          expand-on-hover
          color="colorful2"
          elevation="2"
          permanent
          :class="{aaa:hover}"
        >
          <v-list
            dense
            nav
            class="py-0 grey--text"
          >
            <v-list-item
              v-for="item in items"
              :key="item.title"
              @click="redirect(item)"
            >
              <v-list-item-icon>
                <v-icon>{{item.icon}}</v-icon>
              </v-list-item-icon>
              <v-list-item-content>
                <v-list-item-title class="subtitle-1">{{item.title}}</v-list-item-title>
              </v-list-item-content>
            </v-list-item>
          </v-list>
        </v-navigation-drawer>
        </div>
        <v-overlay
          :value="hover"
          z-index="3"
        >
        </v-overlay>
      </div>
    <div v-else>
      <v-btn
        fab
        v-for="(item,i) in items"
        :key="item.title"
        color="colorful2 accent-2"
        class="btn"
        :class="'btn'+(i+1)"
      >
        <v-icon>{{item.icon}}</v-icon>
      </v-btn>
    </div>
  </div>
</template>

<script>
export default {
  name: 'sideDrawer',
  data: () => ({
    items: [
      {
        icon: 'mdi-home',
        title: '主页'

      },
      {
        icon: 'mdi-file-document',
        title: '贴子'
      },
      {
        icon: 'mdi-tag',
        title: '标签'
      },
      {
        icon: 'mdi-file-search',
        title: '搜索'
      },
      {
        icon: 'mdi-logout',
        title: '退出'
      }
    ],
    hover: false
  }),
  methods: {
    redirect (item) {
      if (item.title === '退出') {
        this.$axios.get('/logout')
        this.$store.commit('logout')
        this.$router.go(0)
      } else if (item.title === '主页') {
        this.$router.push('/home')
      }
    }
  }
}
</script>

<style scoped>
.aaa{
  box-shadow: 0px 2px 4px -1px rgba(0, 0, 0, 0.2),
    0px 4px 5px 0px rgba(0, 0, 0, 0.14),
    0px 1px 10px 0px rgba(0, 0, 0, 0.12);
  color:rgb(228, 223, 249);
}
.btn{
  position: fixed;
  left: -16px;
  z-index: 4;
}
.btn1{
  bottom: 160px;
}
.btn2{
  bottom: 88px;
}
.btn3{
  bottom: 16px;
}
</style>
