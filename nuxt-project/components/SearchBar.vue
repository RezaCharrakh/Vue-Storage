<template>
  <div class="flex justify-center items-center">
    <el-input
    style="border-radius: 16px;"
      v-model="searchQuery"
      placeholder="Search..."
      class="w-full max-w-md"
      clearable
      @clear="onClear"
      @keyup.enter="onSearch"
    >
      <template #append>
        <icon
          @click="onSearch"
          name="fa:search"
          class="cursor-pointer"
          size="16"
        ></icon>
      </template>
    </el-input>
  </div>
</template>

<script setup>
import { ref, defineEmits } from "vue";

const searchQuery = ref("");
const emit = defineEmits(["search", "clear"]);

const onSearch = () => {
  if (searchQuery.value) {
    console.log("Searching for:", searchQuery.value);
    emit("search", searchQuery.value);
  }
};

const onClear = () => {
  searchQuery.value = "";
  emit("clear");
};
</script>

<style scoped>
/* Custom styles if needed */
</style>
