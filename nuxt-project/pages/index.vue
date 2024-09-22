<template>
  <div>
    <el-button @click="toggleDarkMode">
      {{ isDarkMode ? 'Switch to Light Mode' : 'Switch to Dark Mode' }}
    </el-button>
    <Nuxt />
  </div>
</template>

<script setup>
import { ref } from 'vue';

// A ref to track whether dark mode is active or not
const isDarkMode = ref(false);

// Function to toggle dark mode
const toggleDarkMode = () => {
  isDarkMode.value = !isDarkMode.value;
  
  // Toggle the 'dark' class on the <html> element
  if (isDarkMode.value) {
    document.documentElement.classList.add('dark');
  } else {
    document.documentElement.classList.remove('dark');
  }
};
</script>

<style scoped>
/* Add any additional styles for the button if needed */
</style>
