<template>
    <el-card class="box-card">
      <el-form  label-position="labelPosition" label-width="100px" class="main">
          <el-form-item label="订阅链接" prop="desc">
              <el-input type="textarea" v-model="linkInput" rows="5" placeholder="请粘贴订阅链接，仅支持Clash订阅，多个订阅链接请用逗号隔开"></el-input>
          </el-form-item>
          <el-form-item label="更新间隔" prop="time">
              <el-input v-model="time" style="width: 100px" placeholder="秒"></el-input>
          </el-form-item>
          <el-form-item label="新订阅链接" prop="desc">
              <el-input type="textarea" v-model="linkOutput" rows="5"></el-input>
          </el-form-item>
          <el-form-item>
              <el-button  type="primary" @click="submitForm('ruleForm')">生成</el-button>
              <el-button @click="copyForm('ruleForm')">复制</el-button>
          </el-form-item>
      </el-form>
    </el-card>
</template>

<script>
export default {
    data() {
        return {
            linkInput:'',
            linkOutput:'',
            time:'',
        };
    },
    methods: {
        submitForm() {
            let result = ""
                if (this.linkInput !== "") {
                    result += "/sub?url=" + this.linkInput;
                        if (/^[1-9][0-9]*$/.test(this.time)) {
                            result += "&interval=" + this.time;
                        }
                        else if (this.time === ""){
                            result += "&interval=1800";
                        }
                        else {
                            this.$message({
                                message: '时间间隔必须为整数',
                                type: 'error'
                            });
                            return false;
                        }

                } else {
                    this.$message({
                        message: '订阅链接不能为空',
                        type: 'error'
                    });
                    return false;
                }
            this.linkOutput = result
        },
        copyForm(formName) {
            navigator.clipboard.writeText(this.linkOutput);
            this.$message({
                message: '复制成功',
                type: 'success'
            })
        }
    }
}
</script>

<style scoped>
.box-card{
    width: 1000px;
    height: 600px;
    margin: 100px auto auto;
}

.main{
    margin-top: 60px;
}

</style>
