<template>
  <v-content>
    <div class="cont1">
    <v-card class="mx-auto mt-4" v-if="($vuetify.breakpoint.smAndUp)">
      <v-toolbar dense elevation="2">
      <v-btn-toggle
        color="primary"
        dense
        group
      >
        <v-btn :value="1" text @click="bold">
          <v-icon>mdi-format-bold</v-icon>
        </v-btn>

        <v-btn :value="2" text @click="italic">
          <v-icon>mdi-format-italic</v-icon>
        </v-btn>

        <v-btn :value="3" text @click="quote">
          <v-icon>mdi-format-quote-close</v-icon>
        </v-btn>

        <v-btn :value="4" text @click="code">
          <v-icon>mdi-code-tags</v-icon>
        </v-btn>
      </v-btn-toggle>

      <v-divider vertical></v-divider>

      <v-btn-toggle
        class="px-3"
        color="primary"
        dense
        group
      >
        <v-btn v-for="i in 6" :key= "i" class="pa-0" @click="heading(i)" ripple>
          <v-icon>{{'mdi-format-header-'+i}}</v-icon>
        </v-btn>
      </v-btn-toggle>

      <v-divider vertical></v-divider>

      <v-btn-toggle
        color="primary"
        dense
        group
      >
        <v-btn :value="1" text @click="link">
          <v-icon>mdi-link-variant</v-icon>
        </v-btn>

        <v-btn :value="2" text @click="ulist">
          <v-icon>mdi-format-list-bulleted</v-icon>
        </v-btn>

        <v-btn :value="3" text @click="olist">
          <v-icon>mdi-format-list-numbered</v-icon>
        </v-btn>

        <v-btn :value="4" text @click="image">
          <v-icon>mdi-image</v-icon>
        </v-btn>
      </v-btn-toggle>

      <v-divider vertical></v-divider>
      <v-btn-toggle
        color="primary"
        dense
        group
      >
        <v-btn :value="1" text>
          <v-icon>mdi-upload</v-icon>
        </v-btn>

        <v-btn :value="2" text @click="sub">
          <v-icon>mdi-format-subscript</v-icon>
        </v-btn>

        <v-btn :value="3" text @click="sup">
          <v-icon>mdi-format-superscript</v-icon>
        </v-btn>

        <v-btn :value="4" text @click="table">
          <v-icon>mdi-table</v-icon>
        </v-btn>
        <v-btn :value="5" text @click="returnc">
          <v-icon>mdi-keyboard-return</v-icon>
        </v-btn>
      </v-btn-toggle>
        <v-btn color="primary" tile class="ml-3">发表</v-btn>
      </v-toolbar>
      <v-textarea v-model="userText" placeholder="欢迎使用OfCourse! markdown文本编辑器" auto-grow></v-textarea>
    </v-card>

    <v-card class="mx-auto mt-4" v-else>
      <v-toolbar dense elevation="2">
      <v-btn-toggle
        color="primary"
        dense
        group
      >
        <v-btn :value="1" text @click="bold">
          <v-icon>mdi-format-bold</v-icon>
        </v-btn>

        <v-btn :value="2" text @click="italic">
          <v-icon>mdi-format-italic</v-icon>
        </v-btn>

        <v-btn :value="3" text @click="quote">
          <v-icon>mdi-format-quote-close</v-icon>
        </v-btn>

        <v-btn :value="4" text @click="code">
          <v-icon>mdi-code-tags</v-icon>
        </v-btn>
      </v-btn-toggle>
        <v-btn color="primary" tile class="ml-3">提交</v-btn>
      </v-toolbar>

      <v-toolbar dense elevation="1">
      <v-btn-toggle
        class="px-3"
        color="primary"
        dense
        group
      >
        <v-btn v-for="i in 6" :key= "i" class="pa-0" @click="heading(i)" ripple>
          <v-icon>{{'mdi-format-header-'+i}}</v-icon>
        </v-btn>
      </v-btn-toggle>

      <v-btn-toggle
        color="primary"
        dense
        group
      >
        <v-btn :value="1" text @click="link">
          <v-icon>mdi-link-variant</v-icon>
        </v-btn>

        <v-btn :value="2" text @click="ulist">
          <v-icon>mdi-format-list-bulleted</v-icon>
        </v-btn>

        <v-btn :value="3" text @click="olist">
          <v-icon>mdi-format-list-numbered</v-icon>
        </v-btn>

        <v-btn :value="4" text @click="image">
          <v-icon>mdi-image</v-icon>
        </v-btn>
      </v-btn-toggle>

      </v-toolbar>
      <v-toolbar dense elevation="1">

      <v-btn-toggle
        color="primary"
        dense
        group
      >
        <v-btn :value="1" text>
          <v-icon>mdi-upload</v-icon>
        </v-btn>

        <v-btn :value="2" text @click="sub">
          <v-icon>mdi-format-subscript</v-icon>
        </v-btn>

        <v-btn :value="3" text @click="sup">
          <v-icon>mdi-format-superscript</v-icon>
        </v-btn>

        <v-btn :value="4" text @click="table">
          <v-icon>mdi-table</v-icon>
        </v-btn>
        <v-btn :value="5" text @click="returnc">
          <v-icon>mdi-keyboard-return</v-icon>
        </v-btn>
      </v-btn-toggle>
      </v-toolbar>
      <v-textarea v-model="userText" placeholder="欢迎使用OfCourse! markdown文本编辑器" auto-grow></v-textarea>
    </v-card>
    <div v-html="compileMarkDown(userText)" class="pt-2"></div>
    </div>
  </v-content>
</template>

<script>
var showdown = require('showdown')
var converter = new showdown.Converter()
converter.setOption('tables', true)
export default {
  name: 'writebox',
  data: () => ({
  }),
  methods: {
    compileMarkDown (value) {
      return converter.makeHtml(value)
    },
    bold () {
      this.userText += '**粗体内容**'
    },
    italic () {
      this.userText += '*斜体内容*'
    },
    quote () {
      this.userText += '> 引用内容'
    },
    code () {
      this.userText += '`代码内容`'
    },
    link () {
      this.userText += '[链接标题](链接地址)'
    },
    ulist () {
      this.userText +=
`* 第一项
* 第二项
* 第三项`
    },
    olist () {
      this.userText +=
`1. 第一项
2. 第二项
3. 第三项`
    },
    image () {
      this.userText += '![图片alt](图片地址)'
    },
    sub () {
      this.userText += '<sub>下标内容</sub>'
    },
    sup () {
      this.userText += '<sup>上标内容</sup>'
    },
    table () {
      this.userText +=
`|  表头   | 表头  |
|  ----  | ----  |
| 单元格  | 单元格 |
| 单元格  | 单元格 |`
    },
    returnc () {
      this.userText += `

`
    },
    heading (n) {
      for (let i = 0; i < n; i++) this.userText += '#'
      this.userText += n + '级标题'
    }
  },
  props: {
    userText: String
  }
}
</script>

<style scoped>
.texta{
  width: 80%;
  align-self: center;
}
.cont1{
  width:80%;
  margin: 0 auto;
}
</style>
