<script lang="ts">
import { defineComponent } from "vue";
import HomeButton from "../components/HomeButton.vue";
import SessionCardItem from "../components/SessionCardItem.vue";

export default defineComponent({
  props: ["practiseSessionId"],
  components: { HomeButton, SessionCardItem },
});
</script>

<template>
  <HomeButton />
  <h1>Practise</h1>
  <SessionCardItem :practise-session-id="practiseSessionId" />
</template>
