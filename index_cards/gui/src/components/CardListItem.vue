<script lang="ts">
import { defineComponent, ref } from "vue";
import { APIInterface, APIError } from "../api";

export default defineComponent({
  props: ["cardId", "initQuestion", "initAnswer"],
  data() {
    const question = ref(this.initQuestion);
    const answer = ref(this.initAnswer);

    const questionError = ref(false);

    let oldQuestion = this.initQuestion;
    let oldAnswer = this.initAnswer;

    return {
      question,
      answer,
      questionError,
      oldQuestion,
      oldAnswer,
    };
  },
  methods: {
    async _handleError(error: Error | APIError) {
      if (error instanceof APIError) {
        let errorJson = await error.response.json();
        console.log(errorJson);
      } else if (error instanceof Error) {
        alert("Connection to server failed: " + error.message);
      }
    },
    updateCard() {
      if (this.oldQuestion == this.question && this.oldAnswer == this.answer) {
        return;
      }
      this.questionError = this.question === "";
      if (this.questionError) return;

      APIInterface.putCard(this.cardId, this.question, this.answer)
        .then((card) => {
          this.oldQuestion = card.question;
          this.oldAnswer = card.answer;
        })
        .catch((error) => this._handleError(error));
    },
  },
});
</script>

<template>
  <div class="card">
    <div class="label-textarea">
      <label for="question-text-area">Question:</label>
      <textarea
        id="question-text-area"
        rows="4"
        cols="50"
        v-model="question"
        @focusout="updateCard"
        >{{ question }}</textarea
      >
      <div v-if="questionError" class="error-message">
        Question cannot be blank
      </div>
    </div>
    <div class="label-textarea">
      <label for="answer-text-area">Answer:</label>
      <textarea
        id="answer-text-area"
        rows="4"
        cols="50"
        v-model="answer"
        @focusout="updateCard"
        >{{ answer }}</textarea
      >
    </div>
    <button @click="$emit('deleteCard', cardId)">Del</button>
  </div>
</template>

<style scoped>
textarea {
  height: 4em;
  width: 400px;
  overflow-y: scroll;
  margin: 1em;
  resize: none;
}
.card {
  display: flex;
  align-items: center;
}

.label-textarea {
  align-items: flex-start;
}
</style>
