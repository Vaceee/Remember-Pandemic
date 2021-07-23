<template>
  <v-content id="post-list">
    <v-container class="pa-0">
      <v-row class="pa-0">
      <v-col class="pa-0" width="70%">
    <div :class="($vuetify.breakpoint.smAndUp)?'bodya':'bodyb'">
      <span class="pl-3">全部贴子：</span>
    <postitem
      v-for="post in posts"
      :key="post.id"
      :title="post.title"
      :content="post.content"
      :name="post.stu_name"
      :time="post.last_time"
      :tags="post.tags"
    />
    </div>
    </v-col>
    <v-col>

      <div :class="($vuetify.breakpoint.smAndUp)?'tagheada':'tagheadb'">
    <tagheada
      :tags="section.selectedtags" :name="section.sec_name" :hottags="section.hottags"
    ></tagheada>
    </div>
    <div :class="($vuetify.breakpoint.smAndUp)?'topa':'topb'">
      <span class="white--text pl-2">热门贴子：</span>
    <postitem
      v-for="hotpost in hotposts"
      :key="hotpost.id"
      :title="hotpost.title"
      :content="hotpost.content"
      :name="hotpost.stu_name"
      :time="hotpost.last_time"
      :tags="hotpost.tags"
    />
    </div>
    </v-col>
    </v-row>
    </v-container>
  </v-content>
</template>

<script>
import tagheada from './tag-heada'
import postitem from './postitem'

export default {
  name: 'postlist',
  components: {
    postitem, tagheada
  },
  props: ['secId'],
  data () {
    return {
      section: {
        sec_name: '闲谈',
        selectedtags: [
          { tagname: '我不会打tag', tagcolor: 'amber' },
          { tagname: '无聊闲聊', tagcolor: 'blue-grey' }
        ],
        hottags: [
          { tagname: '4m3', tagcolor: 'red', hotness: 7 }
        ]
      },
      hotposts: [
        {
          stu_name: 'Bi Lingfan',
          PosterId: '12223',
          title: 'Fish!',
          Post_Time: 823,
          last_time: '2019-12-2',
          content: 'There are lots of fish swimming in our new Aipen pool! I guess these are colorful koi\'s.',
          tags: [{ tagname: 'travel', tagcolor: 'indigo' },
            { tagname: 'beautiful things', tagcolor: 'cyan' }]
        }
      ],
      posts: [
        {
          stu_name: 'Bi Lingfan',
          PosterId: '12223',
          title: 'Fish!',
          Post_Time: 823,
          last_time: '2019-12-2',
          content: 'There are lots of fish swimming in our new Aipen pool! I guess these are colorful koi\'s.',
          tags: [{ tagname: 'travel', tagcolor: 'indigo' },
            { tagname: 'beautiful things', tagcolor: 'cyan' }]
        },
        {
          stu_name: '管理员',
          PosterId: '12323',
          title: '关于颜色',
          Post_Time: 823,
          last_time: '2019-12-4',
          content: '在所有的色彩中，毫无疑问，蓝色是UI设计中最重要的颜色，也是使用范围最广的色彩。蓝色是冷色系中唯一的原色……',
          tags: [{ tagname: '管理员发布', tagcolor: 'orange' }]
        },
        {
          stu_name: 'Xaire',
          PosterId: '12323',
          title: '关于浏览器中的默认字体',
          Post_Time: 823,
          last_time: ' 2019-05-24',
          content: '行高：1.5（font:12px/1.5 Arial;）行高：1.5（font:12px/1.5 Arial;）……'
        },
        {
          stu_name: 'ソン·チエンフアン',
          PosterId: '12323',
          title: 'DDDDD',
          Post_Time: 823,
          last_time: '2019-11-19',
          content: '多推就是弟弟吗？什么奇怪的理论',
          tags: [{ tagname: 'ACGN', tagcolor: 'pink' }, { tagname: '不打多个标签不舒服', tagcolor: 'light-green' }]
        }
      ]
    }
  },
  mounted () {
    this.$ajax.get('/posts/fetch', {
      params: {
        page: 1,
        limit: 10,
        sec_id: this.secId
      }
    }).then(response => {
      var data = response.data
      this.posts = data.posts
    }).catch(e => {
      alert(e)// 不知道怎么办，它不让用console啊
    })
  }
}
</script>

<style scoped>
.tagheada{
  width: 70%;
  font-size: 2.5rem;
}
.tagheadb{
  padding-left:16px;
  font-size: 2rem;
}
.topa, .topb{
  margin-bottom: 0.5rem;
  font-size: 1.3rem;
  background-color: #8e8fdd;
  padding: 0.8em 0 0.3em;
  border-radius: 0.3em;
}
.topa{
  width: 70%;
  /*margin-left: auto;
  margin-right: auto;*/
}
.topb{
  padding-left:16px;
}
.bodya{
  width: 70%;
  /*margin:auto;*/
  margin-top: 2.2rem;
  font-size: 1.2rem;
}
</style>
