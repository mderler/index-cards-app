<script lang="ts">
import { defineComponent, ref } from "vue";
import { Card, SessionCard } from "../models";
import { APIInterface } from "../api";

export default defineComponent({
  props: ["practiseSessionId"],
  data() {
    const currendSessionCard = ref<SessionCard>();
    const currendCard = ref<Card>();
    const cards = ref<Card[]>();
    const unansweredSessionCards = ref<SessionCard[]>();

    const userAnswerBox = ref("");
    const submitted = ref(false);

    return {
      currendSessionCard,
      currendCard,
      cards,
      unansweredSessionCards,
      userAnswerBox,
      submitted,
    };
  },
  mounted() {
    this.getCards();
  },
  methods: {
    async getCards() {
      const topicId = (
        await APIInterface.getPractiseSession(this.practiseSessionId)
      ).topicId;

      this.cards = await APIInterface.getTopicCards(topicId);
      this.unansweredSessionCards = (
        await APIInterface.getSessionCardsPractiseSession(
          this.practiseSessionId
        )
      ).filter((sessionCard) => sessionCard.correct === null);

      this.setCard();
    },

    setCard() {
      if (!this.unansweredSessionCards) return;
      if (this.unansweredSessionCards.length === 0) return;

      const index = Math.floor(
        Math.random() * this.unansweredSessionCards.length
      );
      this.currendSessionCard = this.unansweredSessionCards[index];

      this.currendCard = this.cards?.find(
        (card) => card.id === this.currendSessionCard?.cardId
      );

      if (this.currendCard !== undefined) return;
      this.unansweredSessionCards = this.unansweredSessionCards.splice(
        index,
        1
      );
      alert(
        "Card not found, maybe outdated practise session. Skipping for now."
      );
      this.setCard();
    },
    async evaluateCard(correct: boolean) {
      if (!this.currendSessionCard) {
        alert("Card of this session not found.");
        this.setCard();
        return;
      }

      await APIInterface.putSessionCard(this.currendSessionCard?.id, correct);
      const index = this.unansweredSessionCards?.indexOf(
        this.currendSessionCard
      );
      if (index === undefined) return;
      this.unansweredSessionCards?.splice(index, 1);

      this.setCard();
      this.submitted = false;
      this.userAnswerBox = "";
    },
  },
});
</script>

<template>
  <h2 v-if="unansweredSessionCards?.length === 0">Finished</h2>
  <div v-else>
    <label for="question">Question:</label>
    <p id="question">{{ currendCard?.question }}</p>
    <div v-if="!submitted">
      <label for="userAnswerBox">Your Answer:</label>
      <textarea
        id="userAnswerBox"
        v-model="userAnswerBox"
        @keyup.enter="submitted = true"
      ></textarea>
    </div>
    <div v-else>
      <label for="userAnswer">Your Answer:</label>
      <p id="userAnswer">{{ userAnswerBox }}</p>
      <label for="correctAnswer">Correct Answer:</label>
      <p id="correctAnswer">{{ currendCard?.answer }}</p>
    </div>
    <button v-if="!submitted" @click="submitted = true">Submit</button>
    <div v-else>
      <button @click="evaluateCard(true)">Correct</button>
      <button @click="evaluateCard(false)">Incorrect</button>
    </div>
  </div>
</template>
