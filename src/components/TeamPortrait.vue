<script setup>
import Character from "@/components/Character.vue";
import {computed} from "vue";

const props = defineProps({
  name: String,
  rank: String,
  playStyle: String,
  diffScore: Number,
  characters: Array,
  ingredients: Object
});

const rankClass = computed(() => {
  if (props.rank === "S") {
    return "tone";
  } else if (props.rank === "A") {
    return "ttwo";
  } else if (props.rank === "B") {
    return "tthree";
  }
});

</script>

<template>
  <div class="team-portrait d-flex justify-content-between align-items-start
    flex-column flex-md-row">
    <div class="team-name d-flex justify-content-center align-items-center align-self-start align-self-md-center">
      <div class="team-rank" :class="rankClass">{{ props.rank}}</div>
      <div class="team-name-elipsis">
        {{ props.name }}
        <div class="team-playstyle">required: {{ props.diffScore }} items</div>
      </div>
    </div>
    <div class="team-characters d-flex justify-content-start flex-wrap ">
      <template v-for="character in props.characters" :key="props.name + character.name">
        <Character v-bind="character" />
      </template>
    </div>
  </div>
</template>

<style scoped>
.team-portrait {
    max-width: 900px;
    border: 1px solid #17313a;
    margin: 0 0 7px 7px;
    padding: 7px;
    background: #102531;
}

.team-rank {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 25px;
    height: 25px;
    padding: 5px;
    margin: 0 15px;
    color: #0d202b;
    font-weight: 600;
    border-radius: 2.5px;
    cursor: default;
}

.team-playstyle {
    text-align: center;
    display: flex;
    align-items: center;
    color: #88a0a7;
    font-size: 12px;
    font-weight: 300;
    letter-spacing: .05em;
    background: #123040;
    margin-top: 4px;
    padding: 4px;
    border-radius: 4px;
    line-height: 1em;
}

.team-name-elipsis {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    text-transform: capitalize;
}

.team-rank.tone {
    background: #ff7f7f;
}

.team-rank.ttwo {
    background: #ffbf7f;
}

.team-rank.tthree {
    background: #ffdf7f;
}

</style>