<template>
  <v-content>
  <div class="bodyy">
    <v-tabs
      fixed-tabs
      background-color="primary"
      dark
      v-model="tab"
      class="tab"
    >
      <v-tab>公告</v-tab>
      <v-tab>@提到我的</v-tab>
      <v-tab>回复我的</v-tab>
      <v-tab-item :key="1">
        <postItem
          v-for="announc in announcs"
          :key="announc.id"
          :title="announc.title"
          :content="announc.content"
          :name="announc.stu_name"
          :time="announc.last_time"
          :tags="announc.tags"
        />
      </v-tab-item>
      <v-tab-item :key="2">
        <postItem
          v-for="at in ats"
          :key="at.id"
          :title="at.title"
          :content="`@${username} ` + at.content"
          :name="at.stu_name"
          :time="at.last_time"
          :tags="at.tags"
        />
      </v-tab-item>
      <v-tab-item :key="3">
        <postItem
          v-for="reply in replies"
          :key="reply.id"
          :title="reply.title"
          :content="reply.content"
          :name="reply.stu_name"
          :time="reply.last_time"
          :tags="reply.tags"
        />
      </v-tab-item>
    </v-tabs>
  </div>
  <div class="bodyy">
    <v-tabs
      fixed-tabs
      background-color="#9970db"
      dark
      v-model="tab"
      class="tab"
    >
      <v-tab>讨论热门</v-tab>
      <v-tab-item :key="1">
        <postItem
          v-for="hottest in hottests"
          :key="hottest.id"
          :title="hottest.title"
          :content="hottest.content"
          :name="hottest.stu_name"
          :time="hottest.last_time"
          :tags="hottest.tags"
          :section="hottest.section"
        />
      </v-tab-item>
    </v-tabs>
  </div>
  </v-content>
</template>

<script>
import ClassesPage from '../ClassesPage'
import postItem from '../../components/general/postItem'
export default {
  name: 'infoBlock',
  components: {
    postItem
  },
  data: () => ({
    ClassesPage,
    username: '',
    announcs: [
      {
        PosterId: '12323',
        title: '欢迎来到记疫',
        Post_Time: 823,
        last_time: '2020-3-4',
        content: '您可以在这里写下有关疫情的一切。'
      },
      {
        PosterId: '12346',
        title: '点击任意一个版块以开始',
        Post_Time: 123,
        last_time: '2020-3-4',
        content: '校园版块为高校学生提供了更多的平台。'
      }
    ],
    ats: [{
      stu_name: '系统管理员',
      PosterId: '12344',
      title: '系统通知',
      Post_Time: 823,
      last_time: '2020-6-26',
      content: '您是第42位加入记疫的用户'
    }],
    replies: [],
    /* replies: [{
      stu_name: 'ソン·チエンフアン',
      PosterId: '12323',
      title: 'DDDDD',
      Post_Time: 823,
      last_time: '2019-11-19',
      content: '多推就是弟弟吗？什么奇怪的理论',
      tags: [{ tagname: 'ACGN', tagcolor: 'pink' }, { tagname: '不打多个标签不舒服', tagcolor: 'light-green' }]
    }], */
    hottests: [{
      stu_name: 'Floyd',
      PosterId: '12344',
      title: '美国确诊人数已突破200万',
      Post_Time: 823,
      last_time: '2020-6-12',
      tags: [{ tagname: '世界疫情', tagcolor: 'purple' }],
      section: { secname: '疫情通告', seccolor: 'pink' }
    },
    {
      stu_name: '知乎',
      PosterId: '12223',
      title: '未来记载新冠病毒的配图',
      Post_Time: 823,
      last_time: '2020-6-26',
      tags: [{ tagname: '新冠病毒', tagcolor: 'indigo' },
        { tagname: '历史', tagcolor: 'cyan' }],
      section: { secname: '疫情日记', seccolor: 'orange' }
    }

    ]
  }),
  mounted () {
    this.username = this.$store.getters.username
  }
}
</script>

<style scoped>
.bodyy{
  font-size: 1.2rem;
  background-color: #f9fafd;
  margin: 10px;
  border-radius: 7px 7px 0 0;
}
.tab{
  border-radius: 6px 6px 0 0;
}
</style>
