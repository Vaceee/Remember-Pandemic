<template>
  <div class="greatcont">
    <div v-for="n in reply" :key="n" class="vline" :class="'ml-'+(n-1)*4"></div>
    <v-card elevation="2"  class="storeycard" :class="'ml-'+reply*4">
      <v-container fluid class="pa-0">
        <v-row>
          <v-col class="py-1 px-0" cols="7" :sm=8 :lg=9>
          <span class="avatar">
            <v-avatar size="48">
              <img src="../../../../public/Ming.png" alt="头像"/>
            </v-avatar>
          </span>
          <span class="subtitle-1 font-weight-bold">{{name}}</span>
          </v-col>
          <v-col class="right">
            <span class="iconwrap">
            <v-icon @click="changeLike">{{liked?"mdi-heart":"mdi-heart-outline"}}</v-icon></span>
            <span>{{likes}}</span>
          </v-col>
          <v-col class="right">
            <span class="iconwrap">
            <v-icon>{{replied?"mdi-message":"mdi-message-outline"}}</v-icon></span>
            <span>{{replies}}</span>
          </v-col>
        </v-row>
            <!--v-divider----v-divider-->
        <v-row>
          <v-col cols="12">
            <v-card  class="body-2 px-3 maina" color="transparent" flat tile>
            <div v-html="compileMarkDown(content)" class="pt-2"></div>
            </v-card>
          </v-col>
        </v-row>
        <v-row class="">
          <v-col class="pr-0" cols="7">
            <v-card class="body-2 pl-3" color="transparent" flat tile>
              <a v-if="more" :href="extendref" class="body-2 mylink">
              <v-icon>mdi-menu-swap-outline</v-icon>还有{{more}}条回复，点击查看
              </a>
            </v-card>
          </v-col>
          <v-col class="pl-0" cols="5">
            <v-card class="body-2 pr-6 pl-0 foota right" color="transparent" flat tile>
              <span class="iconwrap">
              <v-icon>mdi-clock-outline</v-icon></span>
              {{time}}
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-card>
  </div>
</template>

<script>
var showdown = require('showdown')
var converter = new showdown.Converter()
converter.setOption('tables', true)
export default {
  name: 'storey',
  data: () => ({
    liked: false
  }),
  methods: {
    compileMarkDown (value) {
      return converter.makeHtml(value)
    },
    changeLike: function () {
      this.$axios.post('/replies/like', {
        method: this.liked ? 'cancle' : 'like',
        rep_id: this.id
      })
      this.liked = !this.liked
      if (this.liked) this.likes++
      else this.likes--
    }
  },
  props: {
    id: {
      type: Number,
      required: true
    },
    name: {
      type: String,
      required: true
    },
    content: {
      type: String,
      required: true
    },
    reply: {
      type: Number,
      required: true
    },
    replied: {
      type: Boolean,
      required: true
    },
    time: {
      type: String,
      required: true
    },
    likes: {
      type: Number,
      required: true
    },
    image: {
      type: String,
      required: true
    },
    replies: {
      type: Number,
      required: true
    },
    more: {
      type: Number,
      required: false
    },
    extendref: {
      type: String,
      required: false
    }
  },
  mounted () {
    if (this.replies > 0) {
      this.replied = true
    }
    if (this.likes > 0) {
      this.liked = true
    }
    if (this.replies > 1) {
      this.more = this.replies - 1
    }
  }
}
</script>

<style scoped>
.storeycard{
  border: thin solid rgba(0, 0, 0, 0.2);
  border-left: transparent;
  border-right: transparent;
}
.avatar{
  padding: 0 1.5em;
}
.iconwrap{
  padding: 0 0.5em;

}
.maina{
  white-space: pre-wrap;
}
.foota{
  padding: 0 2em;
  text-align: right;
}
:focus{
  outline: 0px;
}
.mylink{
  color: inherit;
  text-decoration: none;
}
.greatcont{
  position: relative;
  padding: 8px 0px;
}
.vline{
  border-color: transparent;
  border-left-color: rgba(97, 96, 100, 0.3);
  border-style: solid;
  border-width: 0.1em;
  margin: -1px auto;
  position: absolute;
  top:0;
  bottom:0;
  color:#7faeb9;
  /*height: 49.5%;*/
}
.vline1{
  top:0;
}
.vline2{
  bottom:0;
}
</style>
