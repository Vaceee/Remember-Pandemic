<template>
  <v-content id="post-list">
    <v-container class="pa-0">
      <div :class="($vuetify.breakpoint.smAndUp)?'mainaaa':'mainbbb'">
        <span class="tagheada">{{section.sec_name}}</span>
        <span class="right"><v-btn color="primary" class="ml-3" @click="writepost">发表帖子</v-btn></span>
        </div>
      <div :class="($vuetify.breakpoint.smAndUp)?'aaa':'bbb'">
        <tagheada
          :tags="section.selectedtags" :name="section.sec_name" :hottags="section.hottags"
        ></tagheada>
        <div class="bodyy">
          <span class="pl-2">热门帖子：</span>
          <post-item
            v-for="hotpost in hotposts"
            :key="hotpost.id"
            :id="hotpost.id"
            :title="hotpost.title"
            :content="hotpost.content"
            :name="hotpost.stu_name"
            :time="hotpost.last_time"
            :tags="hotpost.tags"
            :rep_cnt="hotpost.rep_cnt"
            :click_cnt="hotpost.click_cnt"
          />
        </div>
      </div>
      <div :class="($vuetify.breakpoint.smAndUp)?'mainaaa':'mainbbb'">
        <div class="bodyy">
          <span class="pl-2">全部贴子：</span>
          <post-item
            v-for="post in posts"
            :key="post.id"
            :id="post.id"
            :title="post.title"
            :content="post.content"
            :name="post.usr_name"
            :time="post.last_time"
            :rep_cnt="post.rep_cnt"
            :click_cnt="post.click_cnt"
            :tags="post.tags"
          />
        </div>
      </div>
      <page-bar></page-bar>
    </v-container>
  </v-content>
</template>

<script>
import tagheada from './tag-heada'
import postItem from './postItem'
import pageBar from './pagebar'

export default {
  name: 'postList',
  components: {
    postItem,
    tagheada,
    pageBar
  },
  props: ['secId'],
  data () {
    return {
      section: {
        sec_name: '',
        selectedtags: [
          { tagname: '干货必读', tagcolor: 'pink' }
        ],
        hottags: [
          { tagname: '世界疫情', tagcolor: 'orange', hotness: 9 },
          { tagname: '科普辟谣', tagcolor: 'blue', hotness: 7 }
        ]
      },
      hotposts: [
        {
          stu_name: 'Floyd',
          id: '5',
          title: '美国确诊人数已突破200万',
          // content: '抗议',
          Post_Time: '2020-6-12',
          last_time: '2020-6-12',
          tags: [{ tagname: '世界疫情', tagcolor: 'purple' }],
          section: { secname: '疫情通告', seccolor: 'pink' },
          rep_cnt: 8,
          click_cnt: 133
        },
        {
          stu_name: '知乎',
          id: '6',
          title: '未来记载新冠病毒的配图',
          // content: '你会选择哪一张图片？',
          Post_Time: '2020-6-26',
          last_time: '2020-6-26',
          tags: [{ tagname: '新冠病毒', tagcolor: 'indigo' },
            { tagname: '历史', tagcolor: 'cyan' }],
          section: { secname: '疫情日记', seccolor: 'orange' },
          rep_cnt: 12,
          click_cnt: 96
        }
      ],
      posts: []
    }
  },
  methods: {
    writepost () {
      this.$router.push(`/writepost/${this.$route.params.secId}`)
    }
  },
  mounted () {
    this.$axios.get('/posts/fetch', {
      params: {
        page: 1,
        limit: 10,
        bas_id: this.$route.params.secId
      }
    }).then(response => {
      var data = response.data
      this.posts = data.posts
    }).catch(e => {
      alert(e)
    })
    this.$axios.get('/sections/fetch')
      .then(response => {
        var sections = response.data.sections
        for (let sec of sections) {
          sec = Object(sec)
          // alert(sec.id) // 已解决
          if (Number(sec.id) === Number(this.$route.params.secId)) {
            this.section.sec_name = sec.name
          }
        }
      }).catch(e => {
        alert(e)
      })
  }
}
</script>

<style scoped>
.tagheada, .tagheadb{
  color:#5a5ba1;
  line-height: 5rem;
}
.tagheada{
  /*width: 70%;*/
  padding-left: 0.5rem;
  font-size: 2.5rem;
}
.tagheadb{
  padding-left: 0.5rem;
  font-size: 2rem;
}
.bodyy{
  font-size: 1.2rem;
}
.aaa{
  margin-top: -56px;
  margin-left: 62%;
  width: 26%;
  position: fixed;
}
.mainaaa{
  width: 70%;
}
.right{
  float:right;
  color:#5a5ba1;
  line-height: 5rem;
  padding-left: 0.5rem;
  font-size: 2.5rem;
}
</style>
