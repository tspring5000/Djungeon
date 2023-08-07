<template>
  <div class="create">
    <h3 class="header">Create a new room</h3>
    <br>

    <p class="errortxt" v-for="(value, key) in errors">{{ key }} : {{ value }}</p>

    <p>{{ errors.values }}</p>

    <form @submit.prevent="submit" spellcheck="false" method="POST">
      <div class="flex flex-col">
        <div class="form-item">
          <label>Room Name</label><br>
          <textarea
            v-model="form.room.name" class="shadow-box" required
            cols="25" rows="1" maxlength="25"
            placeholder="The Corridor of Choice"
          ></textarea>
        </div>

        <div class="form-item">
          <label>Room Prompt</label><br>
          <textarea
            v-model="form.room.prompt" class="shadow-box" required
            cols="25" rows="10" maxlength="250"
            placeholder="You find yourself at a junction, do you..."
          ></textarea>
        </div>

        <div class="form-item">
          <label>Choice 1</label><br>
          <textarea
            v-model="form.choice_1.text" class="shadow-box" required
            cols="25" rows="1" maxlength="25"
            placeholder="Turn Left"
          ></textarea>
        </div>

        <div class="form-item">
          <label>Choice 2</label><br>
          <textarea
            v-model="form.choice_2.text" class="shadow-box" required
            cols="25" rows="1" maxlength="25"
            placeholder="Turn Right"
          ></textarea>
        </div>

        <div>
          <button class="btn shadow-box"><h3>PROCEED</h3></button>
        </div>
      </div>
    </form>
  </div>
</template>

<script>
import router from "@/router"
import axois from "axios"

export default {
  name: 'CreateView',
  data() {
    return {
      form: {
        room: {
          name: "",
          prompt: "",
        },
        choice_1: {
          text: "",
        },
        choice_2: {
          text: "",
        },
      },
      errors: {},
    }
  },
  components: {
  },
  mounted() {
  },
  methods: {
    async submit(){
      axois.post("/api/v1/create-room/", this.form).then(response => {
        router.push(response.data)
      })
      .catch(error => {
        this.errors = error.response.data
      })
    },
  }
}
</script>
