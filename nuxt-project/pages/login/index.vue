<template>
  <div class="flex">
    <div class="flex">
      <div>Left side 1</div>
      <div>Left side 2</div>
    </div>
    <div class="flex flex-col items-center w-96 gap-5">
      <div class="w-[60%] mb-7"></div>
      <el-input type="email" v-model="email" placeholder="Email" />
      <el-input
        type="password"
        show-password
        v-model="password"
        placeholder="Password"
      />
      <div class="relative w-full h-8">
        <span class="text-gray-300 absolute right-0">Recover Password !?</span>
      </div>
      <el-button @click="login" type="primary" class="w-full">Login</el-button>
      <el-divider>Continue with</el-divider>
      <div class="flex w-full justify-between">
        <el-button class="w-20"
          ><template #default
            ><img
              style="width: 20px"
              alt=""
              src="/assets/Google__G__logo.svg.webp" /></template
        ></el-button>
        <el-button class="w-20"
          ><template #default
            ><img
              style="width: 20px"
              alt=""
              src="/assets/Google__G__logo.svg.webp" /></template
        ></el-button>
        <el-button class="w-20"
          ><template #default
            ><img
              style="width: 20px"
              alt=""
              src="/assets/Google__G__logo.svg.webp" /></template
        ></el-button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";

const email = ref("");
const password = ref("");
</script>

<style scoped></style>
