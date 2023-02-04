<script lang="ts">
import { defineComponent } from "vue";
import { APIInterface } from "../api";

export default defineComponent({
  props: ["topicId", "topicName"],
  methods: {
    async practiseTopic() {
      const practiseSession = await APIInterface.postPractiseSession(
        this.topicId
      );
      this.$router.push({
        name: "Practise",
        params: {
          practiseSessionId: practiseSession.id,
        },
      });
    },
    editTopic() {
      this.$router.push({
        name: "Edit Topic",
        params: {
          topicId: this.topicId,
        },
      });
    },
  },
});
</script>

<template>
  <div class="topic-list-item">
    <h4>{{ topicName }}</h4>
    <button @click="practiseTopic">Practise</button>
    <button @click="editTopic">Edit</button>
    <button @click="$emit('deleteTopic', topicId)">Delete</button>
  </div>
</template>

<style scoped>
.topic-list-item {
  display: flex;
}

.card-div {
  text-align: center;
}
</style>
