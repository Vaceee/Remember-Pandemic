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
          name: '魔药学',
          id: '1',
          teacher: '苏丝',
          time: '周四5-8节',
          hotposts: [
            { title: '谁能买到波多莫草吗？', color: 'red' },
            { title: '变色药水的配方公式，速进', color: 'indigo' },
            { title: '关于我为什么被苏丝关了禁闭', color: 'lime' }
          ]
        },
        {
          name: '魔法史',
          id: '2',
          teacher: '艾特伟',
          hotposts: [
            { title: '关于仙界大战的小组课后作业', color: 'orange' }
          ]
        },
        {
          name: '变形术',
          id: '3',
          teacher: '斐戎',
          time: '周一3-4节 周三5-6节',
          hotposts: [
            { title: '莉迪亚真的是人间宝藏', color: 'teal' },
            { title: '关于那只黑白鸟的50个小秘密', color: 'pink' }
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
