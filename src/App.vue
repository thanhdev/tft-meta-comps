<script setup>
import {reactive} from 'vue'
import TeamPortrait from "@/components/TeamPortrait.vue";
import ItemPanel from "@/components/ItemPanel.vue";

const teams = reactive([]);
const selectedItems = reactive([]);
const itemsCounter = reactive({});

const fetchTeams = async () => {
  const response = await fetch("/tft-meta-comps/team_comps.json");
  const data = await response.json();
  data.forEach(team => {
    team.diffScore = 0;
    for (const [key, value] of Object.entries(team.ingredients)) {
      team.diffScore += value - (itemsCounter[key] || 0);
    }
    team.diffScore = Math.abs(team.diffScore);
  });
  teams.push(...data);
}

const selectItem = (item) => {
  selectedItems.push(item);
  itemsCounter[item] = itemsCounter[item] ? itemsCounter[item] + 1 : 1;
  sortTeams();
}

const removeItem = (item) => {
  const index = selectedItems.indexOf(item);
  if (index > -1) {
    selectedItems.splice(index, 1);
    itemsCounter[item] -= 1;
    sortTeams();
  }
}

const clearItems = () => {
  selectedItems.splice(0, selectedItems.length);
  for (let key of Object.keys(itemsCounter)) {
    itemsCounter[key] = 0;
  }
  sortTeams();
}

const sortTeams = () => {
  teams.forEach(team => {
    team.diffScore = 0;
    for (const [key, value] of Object.entries(team.ingredients)) {
      team.diffScore += Math.max(0, value - (itemsCounter[key] || 0));
    }
    team.diffScore = Math.abs(team.diffScore);
  });

  teams.sort((a, b) => {
    return a.diffScore - b.diffScore;
  });

}

fetchTeams();
</script>

<template>
  <h3 class="text-center p-2">TFT Meta Team Comps Tier List</h3>
  <div class="main-panel p-2 d-flex justify-content-center">
    <div style="max-width: 25%;">
      <ItemPanel :items="selectedItems" @selectItem="selectItem" @removeItem="removeItem" @clearItems="clearItems"/>
    </div>
    <div>
      <TeamPortrait
          v-for="team in teams"
          :key="team.name + team.rank"
          v-bind="team"
      />
    </div>
  </div>
</template>

<style scoped>
</style>
