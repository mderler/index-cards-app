<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  props: ["topicId", "topicName"],
  methods: {
    practiseTopic() {},
    editTopic() {},
  },
});
</script>

<template>
  <div class="topic-list-item">
    <h4>{{ topicName }}</h4>
    <button @click="practiseTopic">Practise</button>
    <button @click="$emit('editTopic', topicId)">Edit</button>
    <button @click="editTopic">Delete</button>
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
