<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  props: ["topicId", "topicName"],
});
</script>

<template>
  <div class="topic-list-item">
    <h4>{{ topicName }}</h4>
    <button @click="$emit('deleteTopic', topicId)">Delete</button>
    <button @click="$emit('editTopic', topicId)">Edit</button>
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
