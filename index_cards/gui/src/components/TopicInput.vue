<script lang="ts">
import { ref, defineComponent } from "vue";
import APIInterface from "../api";

export default defineComponent({
  setup() {
    const inputRef = ref<HTMLInputElement | null>();
    const errorMessage = ref("");

    let topicName = "";
    let topicId: null | number = null;

    return {
      inputRef,
      topicName,
      topicId,
      errorMessage,
    };
  },
  mounted() {
    this.inputRef?.focus();
  },
  methods: {
    submit() {
      this.errorMessage = "";
      let trimmedInput = this.topicName.trim();
      if (trimmedInput === "") {
        this.errorMessage = "The topic name cannot be empty";
        return;
      }
      if (!/^[\x00-\x7F]*$/.test(trimmedInput)) {
        this.errorMessage = "The topic name cannot include special characters.";
        return;
      }
      this.topicName = trimmedInput;
      if (this.inputRef) {
        this.inputRef.value = "";
      }
      console.log(this.topicName);
      this.topicName = "";
      APIInterface.getTopics();
    },
  },
});
</script>

<template>
  <label for="input">Topic Name:</label>
  <input
    id="input"
    @keyup.enter="submit"
    v-model="topicName"
    type="text"
    ref="inputRef"
  />
  <button @click="submit">Submit</button>
  <p class="error-message" v-if="errorMessage">{{ errorMessage }}</p>
</template>
