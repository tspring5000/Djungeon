<template>
    <div class="play" :key="anim">
        <h3 class="header">{{ room.name }}</h3>
        <h2 :class="[room.type_class]">{{ room.prompt }}</h2>

        <div class="flex">
            <template v-if="room.is_ending">
                <router-link class="btn-link" to="/">
                    <button class="btn shadow-box"><h3>Try Again</h3></button>
                </router-link>
            </template>

            <template v-else>
                <a class="btn-link"><button class="btn shadow-box" @click="getRoom(room.choice_1?.room)">
                <h3>{{ room.choice_1?.text }}</h3>
                </button></a>
                <a class="btn-link"><button class="btn shadow-box" @click="getRoom(room.choice_2?.room)">
                <h3>{{ room.choice_2?.text }}</h3>
                </button></a>
            </template>
        </div>
    </div>

</template>

<script>
import axois from "axios"

export default {
    name: 'PlayView',
    data() {
        return {
            room: {},
            anim: 0,
        }
    },
    components: {
    },
    mounted() {
        this.getRoom(this.$route.params.room_slug)
    },
    methods: {
        getRoom(room_slug){
            axois.get(`/api/v1/rooms/${room_slug}/`).then(response => {
                this.room = response.data
            })
            .catch(error => {
                console.log(error)
            })
            this.anim += 1;
        },
    }
}
</script>