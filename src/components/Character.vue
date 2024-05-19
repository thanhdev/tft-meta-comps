<script setup>

import Item from "@/components/Item.vue";

const props = defineProps(['name', 'attrs', 'items']);
const normalizedName = props.name.replace(/[^a-zA-Z]/g, '');
const src = `https://rerollcdn.com/characters/Skin/11/${normalizedName}.png`
</script>

<template>
  <div class="character" :class="props.attrs">
    <div class="character-wrapper">
      <img class="character-icon" :src :alt="props.name">
    </div>
    <div class="team-character-name">{{ props.name }}</div>
    <div class="row character-items">
      <template v-for="item in props.items" :key="item">
        <div class="col-1 character-item-wrapper">
          <Item :alt="item.name"/>
        </div>
      </template>
    </div>
  </div>
</template>

<style scoped>

</style>