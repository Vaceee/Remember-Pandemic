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
export default {
  name: 'post',
  components: {
    ptitle, storey, writebox
  },
  data: () => ({
    storeys: [
      {
        stu_name: '璃梦',
        id: '12223',
        content: '我们开始故事接龙怎么样啊？',
        reply: 0,
        replies: 2,
        replied: true,
        time: '2019-12-2',
        likes: 2,
        liked: true,
        image: nona
      },
      {
        stu_name: '赵轲欣',
        id: '12234',
        content: '挺好的。我记得小的时候曾经这么干过……当然，写得都挺傻的',
        reply: 1,
        replies: 1,
        replied: true,
        time: '2019-12-2',
        likes: 1,
        liked: true,
        image: ming
      },
      {
        stu_name: '璃梦',
        id: '12255',
        content: '真是让人怀念的童年时代啊……',
        reply: 2,
        replies: 0,
        replied: false,
        time: '2019-12-2',
        likes: 2,
        liked: false,
        image: nona,
        more: 3,
        extendref: ''
      },
      {
        stu_name: '懒得想名字的步',
        id: '12256',
        content: '+1，还以为只有我自己呢',
        reply: 3,
        replies: 0,
        replied: false,
        time: '2019-12-2',
        likes: 0,
        liked: false,
        image: aggi
      },
      {
        stu_name: '璃梦',
        id: '12257',
        content: '不知道什么时候起，就好像是美梦重新来过……',
        reply: 2,
        replies: 0,
        replied: false,
        time: '2019-12-2',
        likes: 2,
        liked: false,
        image: nona,
        more: 2,
        extendref: ''
      },
      {
        stu_name: '璃梦',
        id: '12245',
        content: `那我先来吧。第一句……
        从前，有一个漂亮的女孩住在蓝色的森林里……
        话说我们当年接龙的故事还都是猫呢。真是怀念啊，那还是我上小学的时候……那样的日子。`,
        reply: 0,
        replies: 0,
        replied: false,
        time: '2019-12-2',
        likes: 1,
        liked: true,
        image: nona
      },
      {
        stu_name: '赵轲欣',
        id: '12258',
        content: `她的名字叫小茉。有一天，出门的时候，她发现一个光芒闪耀的球体在林间漂浮。她加快脚步跟了上去……
        果然我也老了啊，这些想象力现在都开转不动了。`,
        reply: 0,
        replies: 0,
        replied: false,
        time: '2019-12-2',
        likes: 1,
        liked: true,
        image: ming
      },
      {
        stu_name: '懒得想名字的步',
        id: '12259',
        content: '我觉得挺好啊，大片开头',
        reply: 1,
        replies: 0,
        replied: false,
        time: '2019-12-2',
        likes: 1,
        liked: false,
        image: aggi,
        more: 1,
        extendref: ''
      }
    ],
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
        limit: 10,
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
