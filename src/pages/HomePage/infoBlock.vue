<template>
  <div class="bodyy">
    <v-tabs
      fixed-tabs
      background-color="primary"
      dark
      v-model="tab"
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
          :content="at.content"
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

    <v-tabs
      fixed-tabs
      background-color="colorful1"
      dark
      v-model="tab"
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
    announcs: [
      {
        PosterId: '12323',
        title: '魔咒学',
        Post_Time: 823,
        last_time: '2019-12-4',
        content: '下节课每个人带两支羽毛笔'
      },
      {
        PosterId: '12346',
        title: '天文学',
        Post_Time: 123,
        last_time: '2019-12-4',
        content: '记录每天晚上的冬季大三角，将位置变化描在一张图上'
      }
    ],
    ats: [{
      stu_name: '隔壁',
      PosterId: '12344',
      title: '宿舍外面是不是有只猫啊',
      Post_Time: 823,
      last_time: '2019-11-21',
      content: '@璃梦 知道了'
    }],
    replies: [{
      stu_name: 'ソン·チエンフアン',
      PosterId: '12323',
      title: 'DDDDD',
      Post_Time: 823,
      last_time: '2019-11-19',
      content: '多推就是弟弟吗？什么奇怪的理论',
      tags: [{ tagname: 'ACGN', tagcolor: 'pink' }, { tagname: '不打多个标签不舒服', tagcolor: 'light-green' }]
    }],
    hottests: [{
      stu_name: '那三个魂淡',
      PosterId: '12344',
      title: '笑什么笑让你笑了吗',
      Post_Time: 823,
      last_time: '2019-11-20',
      tags: [{ tagname: '哈哈哈哈哈哈哈哈哈', tagcolor: 'purple' }],
      section: { secname: '哈哈哈哈哈哈哈', seccolor: 'yellow' }
    },
    {
      stu_name: 'Bi Lingfan',
      PosterId: '12223',
      title: 'Fish!',
      Post_Time: 823,
      last_time: '2019-12-2',
      tags: [{ tagname: 'travel', tagcolor: 'indigo' },
        { tagname: 'beautiful things', tagcolor: 'cyan' }],
      section: { secname: '生活', seccolor: 'green' }
    }

    ]
  })
}
</script>

<style scoped>
.bodyy{
  font-size: 1.2rem;
  background-color: #f9fafd;
}
</style>
