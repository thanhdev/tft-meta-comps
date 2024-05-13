<script setup>
import Character from "@/components/Character.vue";

const props = defineProps({
  name: String,
  rank: String,
  playStyle: String,
  diffScore: Number,
  characters: Array
});

let rankClass;
if (props.rank === "S") {
  rankClass = "tone";
} else if (props.rank === "A") {
  rankClass = "ttwo";
} else if (props.rank === "B") {
  rankClass = "tthree";
}

</script>

<template>
  <div class="row team-portrait">
    <div class="col-4 team-name">
      <div class="row">
        <div class="col-1 team-rank" :class="rankClass">{{ props.rank}}</div>
        <div class="col team-name-elipsis">
          {{ props.name }}
          <div class="team-playstyle">required: {{ props.diffScore }} items</div>
        </div>
      </div>
    </div>
    <div class="col-8 team-characters">
      <div class="row">
        <template v-for="character in props.characters" :key="props.name + character.name">
          <Character :name="character.name" :items="character.items" :class="character.attrs[0]" />
        </template>
      </div>
    </div>
  </div>
</template>

<style scoped>

</style>