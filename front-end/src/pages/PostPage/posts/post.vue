<template>
  <v-content id="post-list">
    <v-container class="py-0">
      <v-sheet class="postsheet" color="transparent" :width="'100%'">
      <ptitle
        :title="post.title"
        :content="post.content"
        :name="post.usr_name"
        :time="post.time"
      />
      </v-sheet>
      <v-sheet class="contsheet" color="transparent" :width="($vuetify.breakpoint.smAndUp)? '70%' :'100%'">
      <storey
        v-for="storey in storeys"
        :key="storey.id"
        :id="storey.id"
        :content="storey.content"
        :name="storey.usr_name"
        :reply="storey.reply"
        :time="storey.time"
        :likes="storey.like_cnt"
        :image="storey.image"
        :replies="storey.reply.reply_cnt"
        :extendref="storey.extendref"
      />
      </v-sheet>
    <writebox></writebox>
    <page-bar></page-bar>
    <br>
    </v-container>
  </v-content>
</template>

<script>
import ptitle from './title'
import storey from './storey'
import nona from '../../../../public/Nona1.png'
import ming from '../../../../public/Ming.png'
import aggi from '../../../../public/Aggi.png'
import writebox from './writebox'
import pageBar from './pagebar'
export default {
  name: 'post',
  components: {
    ptitle, storey, writebox, pageBar
  },
  data: () => ({
    storeys: [],
    post: {}
  }),
  mounted () {
    this.$axios.get('/posts/fetch-one', {
      params: {
        post_id: this.$route.params.postId
      }
    }).then(response => {
      var data = response.data
      this.post = data.post
    }).catch(e => {
      alert(e)
    })

    this.$axios.get('/replies/fetch', {
      params: {
        page: 1,
        limit: 12,
        post_id: this.$route.params.postId,
        reply_id: -1
      }
    }).then(response => {
      var data = response.data
      this.storeys = data.replies
    }).catch(e => {
      alert(e)
    })
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
.contsheet{
  margin: 0px auto;
  color:#c4cf9a;
}
</style>
