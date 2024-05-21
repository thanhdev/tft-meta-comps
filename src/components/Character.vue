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
    <div class="character-name">{{ props.name }}</div>
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

.character {
    position: relative;
    width: 12%;
    min-width: 60px;
    margin-top: 10px;
    text-align: center;
}

.character-name {
    width: 45px;
    min-height: 15px;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    font-size: 11px;
    text-align: center;
    color: #88a0a7;
    line-height: 1.3em;
    transition: all .3s;
}

img.character-icon  {
    width: 45px;
    height: 45px;
    min-width: 45px;
    min-height: 45px;
}


.character-items {
    margin-left: -26px;
    display: flex;
    justify-content: center;
}

.character-item-wrapper {
    width: 5%;
    padding: 0 10px;
}


.character.c1 img.character-icon {
    border: 1px solid #213042;
}

.character.c2 img.character-icon {
    border: 1px solid #156831;
}

.character.c3 img.character-icon {
    border: 1px solid #12407c;
}

.character.c4 img.character-icon {
    border: 1px solid #893088;
}

.character.c5 img.character-icon {
    border: 1px solid #b89d27;
}

.l3:before {
    content: "★★★";
    color: #e4c157
}

.l3:before,.l4:before {
    position: absolute;
    top: -12px;
    left: 50%;
    font-size: 14px;
    -webkit-transform: translateX(-50%);
    transform: translateX(-50%);
    z-index: 10;
    width: 100%;
    text-align: center;
    text-shadow: 0 3px 3px #000;
    letter-spacing: -3px;
    margin-left: -1px
}

.l4:before {
    content: "★★★★";
    color: #39bda7
}

</style>