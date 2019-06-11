<template>
    <div>
    <span class = "display1" v-once>Enter a number from 1 to 4999 to convert from the Roman number system to Arabic and vice versa. </span>
        <ul>
            <li v-for="err in errors" class="red--text">
                {{err}}
            </li>
        </ul>
    <div>
        
        <v-textarea
          solo
          name="input"
          label="Input value"
          v-model="input"
          @input="handleData"
        />
    </div>
        <v-textarea
          solo
          name="output"
          label="Input value"
            v-model="output"
        />
    </div>



</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            input: "",
            output: "",
            entrypoint: "http://localhost:8000/",
            errors: [],
            interval: null,
            sendingRequestDelay: 600,
        }
    },
    methods: {
        handleData(){
            clearInterval(this.interval);
            this.interval = setInterval(() => {
                this.send();
                clearInterval(this.interval);
            }, this.sendingRequestDelay);
        },
        send(){
            const payload = {
                "value": this.input
            }
            this.errors = [];
            axios({
                method: 'post',
                url: this.entrypoint,
                data: payload,
                headers: {
                    "Content-Type": "application/json",
                }
            })
            .then((response) => {
                this.output = response.data.data;
            })
            .catch((err) => {
                this.errors = err.response.data.errors;
            })
        }
    }
    
}
</script>

<style>
body{background: rgba(94, 185, 238, 0.151)}

#display1 {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #0479ee1c;
  margin-top: 60px;
}

</style>
