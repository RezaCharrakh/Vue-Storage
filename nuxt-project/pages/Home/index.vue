<template>
  <div>
    <header class="flex w-screen h-24 justify-between p-10 items-center">
      <div class="flex items-center gap-2">
        <img class="w-16" src="/assets/V-Cloud logo.png" alt="" />
        <h1 class="text-4xl font-bold text-[#009BA1]">V-Cloud</h1>
      </div>
      <div class="w-[30%] mr-20">
        <SearchBar @search="handleSearch" @clear="handleClear"></SearchBar>
      </div>
      <div class="flex gap-14 items-center">
        <div>
          <el-button color="#009BA1" size="large" round=""
            ><icon class="mr-2" size="17" name="tabler:cloud-upload"></icon
            >Upload</el-button
          >
        </div>
        <div class="flex items-center gap-4">
          <el-avatar><icon size="22" name="fa:user"></icon></el-avatar>
          <div>Reza</div>
        </div>
      </div>
    </header>
    <main>
      <!-- Use v-for to render ObjectCard 20 times -->
      <div class="grid grid-cols-4 gap-4 p-10">
        <ObjectCard v-for="n in 20" :key="n" />
      </div>
    </main>
  </div>
</template>

<script setup>
const handleSearch = (query) => {
  console.log("Search query:", query);
  // Add your search handling logic here
};

const handleClear = () => {
  console.log("Search cleared.");
};
</script>

<style scoped></style>
