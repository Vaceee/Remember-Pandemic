<template>
  <div>
    <v-card elevation="10" height="100%" width="33%" class="containcard" tile>
      <v-container>
        <v-row no-gutters>
          <v-col>
            <v-img src="../../assets/logo.png" class="mx-6 mb-3" height="100" width="100">
            </v-img>
            <v-form
              ref="form"
              lazy-validation
              class="px-6 pb-6"
            >
              <v-card-title class="d-flex headline px-0 pt-2" color="primary"><!--justify-center-->
                <span>用户注册</span>
              </v-card-title>
              <v-text-field
                v-model="usrNo"
                :counter="7"
                label="账号"
                required
                clearable
                autocomplete="false"
              ></v-text-field>
              <v-text-field
                v-model="usrPassword"
                label="密码"
                required
                type="password"
                clearable
                autocomplete="false"
                @keyup.enter="try_login"
              ></v-text-field>
              <v-text-field
                v-model="usrName"
                label="用户名"
                required
                clearable
                autocomplete="false"
              ></v-text-field>
              <div class="checkboxlist">
              <input type="checkbox" class="checkbox" v-model="usrSex" value="M">男
              <input type="checkbox" class="checkbox" v-model="usrSex" value="F">女
              </div>

              <div class="buttons">
                <router-link class="link" to="/login">
                <v-btn
                  color="primary"
                  class="mr-4"
                >登陆</v-btn>
                </router-link>
                <v-btn
                  color="accent"
                  class="mr-4"
                  @click="register"
                >注册</v-btn>
              </div>
            </v-form>

          </v-col>
        </v-row>
      </v-container>
    </v-card>
  </div>
</template>

<script>
import hash from 'sha.js'
export default {
  name: 'RegisterForm',
  data () {
    return {
      usrNo: '',
      usrPassword: '',
      usrName: '',
      usrSex: []
    }
  },
  computed: {
    passwdHash () {
      return hash('sha256').update(this.usrPassword).digest('hex')
    }
  },
  methods: {
    register () {
      if (!this.usrNo.length || !this.usrPassword.length) {
        this.login_alert('账号或密码不能为空')
      } else {
        this.$axios.post('/register', {
          usr_no: this.usrNo,
          usr_password: this.passwdHash,
          usr_name: this.usrName,
          usr_gender: this.usrSex[0]
        }).then(res => {
          if (res.status === 200) {
            const data = res.data
            if (data.status === 'REGISTER_SUCCESS') {
              alert('注册成功！')
              this.$router.push('login')
            } else if (data.status === 'NO_REPEAT') {
              alert('账号已被注册！')
            } else if (data.status === 'REGISTER_FAIL') {
              alert('出错了！')
            } else {
              alert('Unknown error occured')
            }
          } else {
            alert('Connection failed.\nPlease check your network condition.')
          }
        }).catch(e => {
          alert(e)
        })
      }
    }
  }
}
</script>

<style scoped>
  .buttons {
    justify-content: center;
    margin-top: 15px;
  }
  .containcard {
    position: fixed;
    top:0;
    right:5%;
    transform: translate(20%,0);
    z-index: 10;
  }
  .alert-container {
    padding-right: 1em;
  }
</style>
