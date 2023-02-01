<script lang="ts">
export default {
  props: ["id", "topicName"],
  created() {
    console.log(this.$props);
  },
};
</script>

<template>
  <h1>Add Cards</h1>
  <h2>{{ topicName }}</h2>
  <div>
    <label for="question-text-area">Question:</label>
    <textarea id="question-text-area" rows="4" cols="50"></textarea>
    <label for="answer-text-area">Answer:</label>
    <textarea id="answer-text-area" rows="4" cols="50"></textarea>
    <button>Submit</button>
    <button>Save</button>
  </div>
</template>

<style scoped>
textarea {
  height: 120px;
  width: 400px;
  overflow-y: scroll;
  margin: 1em;
  resize: none;
}
</style>
