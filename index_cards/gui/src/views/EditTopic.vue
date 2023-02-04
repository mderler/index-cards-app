<script lang="ts">
import { defineComponent, ref } from "vue";
import { APIInterface, APIError } from "../api";
import { Card } from "../models";
import CardListItem from "../components/CardListItem.vue";
import HomeButton from "../components/HomeButton.vue";

export default defineComponent({
  props: ["topicId"],
  components: {
    CardListItem,
    HomeButton,
  },
  data() {
    const topicName = ref("");
    const cards = ref<Card[]>();

    let oldTopicName = "";

    APIInterface.getTopic(this.topicId)
      .then((topic) => {
        topicName.value = topic.topicName;
        oldTopicName = topic.topicName;
      })
      .catch((error) => alert(error));

    APIInterface.getTopicCards(this.topicId).then(
      (topicCards) => (cards.value = topicCards)
    );

    return {
      topicName,
      oldTopicName,
      cards,
    };
  },
  methods: {
    _handleError(error: Error | APIError) {
      if (error instanceof APIError) {
        let errorJson;
        alert(JSON.stringify(errorJson));
      } else if (error instanceof Error) {
        alert("Connection to server failed: " + error.message);
      }
    },
    submitTopicName() {
      if (this.oldTopicName === this.topicName) {
        return;
      }

      APIInterface.putTopic(this.topicId, this.topicName)
        .then((topic) => {
          this.oldTopicName = topic.topicName;
          return topic;
        })
        .catch((error) => this._handleError(error));
    },
    addCard() {
      APIInterface.postCard(this.topicId)
        .then((card) => this.cards?.push(card))
        .catch((error) => {
          this._handleError(error);
        });
    },
    deleteCard(cardId: number) {
      APIInterface.deleteCard(cardId)
        .then(() => {
          const topic = this.cards?.find((card) => card.id === cardId);
          if (!topic) return;
          const index = this.cards?.indexOf(topic);
          if (index === undefined || index === -1) return;
          this.cards?.splice(index, 1);
        })
        .catch((error) => {
          this._handleError(error);
        });
    },
  },
});
</script>

<template>
  <HomeButton />
  <h1>Edit Topic</h1>
  <label for="topic-name">Topic Name:</label>
  <input
    id="topic-name"
    type="text"
    v-model="topicName"
    v-on:focusout="submitTopicName"
    @keyup.enter="submitTopicName"
  />
  <div class="cards">
    <CardListItem
      v-for="card in cards"
      :card-id="card.id"
      :init-question="card.question"
      :init-answer="card.answer"
      @delete-card="deleteCard"
    />
  </div>
  <button @click="addCard">Add Card</button>
</template>
