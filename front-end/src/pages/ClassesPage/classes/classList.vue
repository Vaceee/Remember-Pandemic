<template>
  <v-content id="class-list">
    <v-container>
      <vuedraggable v-model="claases" ghost-class="a" chosen-class="a" drag-class="a">
        <class-item
          v-for="claas in claases"
          :key="claas.id"
          :id="claas.id"
          :name="claas.name"
          :teacher="claas.teacher"
          :time="claas.time"
          :hotposts="claas.hotposts"
        />
      </vuedraggable>
    </v-container>
  </v-content>
</template>

<script>
import classItem from './classItem'
import vuedraggable from 'vuedraggable'

export default {
  name: 'classList',
  components: {
    classItem, vuedraggable
  },
  props: ['secId', 'drag'],
  data () {
    return {
      claases: [
        {
          name: '线上学习',
          id: '4',
          teacher: '',
          time: '教学',
          hotposts: [
            { title: '对于线上网课，你有哪些技巧分享？', color: 'red' },
            { title: '期末的论文和大作业太多了吧', color: 'indigo' }
          ]
        },
        {
          name: '时间管理',
          id: '5',
          time: '提升',
          hotposts: [
            { title: '大家在家都如何保持自主性呢', color: 'orange' }
          ]
        },
        {
          name: '校园生活',
          id: '6',
          teacher: '',
          time: '生活',
          hotposts: [
            { title: '想念西苑大排档的烤鱼了', color: 'green' },
            { title: '还来不及和老师同学认真告别，就匆匆毕业了', color: 'purple' }
          ]
        },
        {
          name: '畅所欲言',
          id: '7',
          teacher: '',
          time: '沟通',
          hotposts: [
            { title: '疫情期间，你还会跟室友经常交流吗？', color: 'teal' },
            { title: '异地恋的同学是怎样度过疫情的？', color: 'pink' }
          ]
        },
        {
          name: '兴趣交流',
          id: '8',
          teacher: '',
          time: '社交',
          hotposts: [
            { title: '分享我在疫情期间的新爱好', color: 'teal' },
            { title: '有对数据挖掘感兴趣的同学吗', color: 'pink' }
          ]
        }

      ]
    }
  }
}
</script>

<style scoped>
.a{
  opacity:1;
  background-color:#d9f6ff;
}
</style>
