<script lang="ts">
import { defineComponent, ref } from "vue";
import { APIInterface } from "../api";
import HomeButton from "../components/HomeButton.vue";
import SessionCardListItem from "../components/SessionCardListItem.vue";
import { CardSessionCardPairs, CardSessionCardPair } from "../models";

export default defineComponent({
  props: ["practiseSessionId"],
  components: {
    HomeButton,
    SessionCardListItem,
  },
  data() {
    const displayedCards = ref<CardSessionCardPairs>();

    return { displayedCards };
  },
  methods: {
    async getCards() {
      const topicId = (
        await APIInterface.getPractiseSession(this.practiseSessionId)
      ).topicId;

      const cards = await APIInterface.getTopicCards(topicId);
      const sessionCards = (
        await APIInterface.getSessionCardsPractiseSession(
          this.practiseSessionId
        )
      ).filter((sessionCard) => sessionCard.correct !== null);

      this.displayedCards = sessionCards
        .map((sessionCard) => {
          const card = cards.find((card) => sessionCard.cardId === card.id);
          const pair: CardSessionCardPair = {
            question: card ? card.question : "",
            answer: card ? card.answer : "",
            userAnswer: sessionCard.userAnswer,
            correct: sessionCard.correct,
          };
          return pair;
        })
        .filter((pair) => pair.question !== undefined);
    },
  },
  mounted() {
    this.getCards();
  },
});
</script>

<template>
  <HomeButton />
  <router-link to="/practisesessions">Back</router-link>
  <h1>Review Session</h1>
  <table>
    <thead>
      <th>Question</th>
      <th>Correct Answer</th>
      <th>Your Answer</th>
    </thead>
    <tbody>
      <SessionCardListItem
        v-for="card in displayedCards"
        :question="card.question"
        :answer="card.answer"
        :user-answer="card.userAnswer"
        :correct="card.correct"
      />
    </tbody>
  </table>
</template>
