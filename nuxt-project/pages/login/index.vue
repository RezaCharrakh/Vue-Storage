<template>
  <div class="flex justify-center items-center h-screen gap-52 relative">
    <div class="absolute top-10 left-10 flex items-center gap-2">
      <img class="w-20" src="/assets/V-Cloud logo.png" alt="" />
      <h1 class="text-4xl font-bold text-[#009BA1]">V-Cloud</h1>
    </div>
    <div
      class="flex flex-col items-center w-96 gap-5 relative z-10 ml-52 prose"
    >
      <div>
        <h2 class="text-4xl">Login</h2>
      </div>
      <el-input
        v-model="email"
        placeholder="Email"
        input-class="!bg-gray-400 px-4 py-2 border rounded-lg focus:ring-2 focus:ring-[#009BA1]"
        style="width: 400px"
        size="large"
        ><template #append
          ><icon
            name="material-symbols:mail-outline-rounded"
            size="30"
          ></icon></template
      ></el-input>
      <el-input
        v-model="password"
        placeholder="Password"
        show-password
        input-class="!bg-gray-400 px-4 py-2 border rounded-lg focus:ring-2 focus:ring-[#009BA1]"
        style="width: 400px"
        size="large"
      ><template #append
          ><icon
            name="material-symbols:key-outline-rounded"
            size="30"
          ></icon></template
      ></el-input>

      <div class="relative w-full h-8">
        <span class="text-gray-300 absolute right-0">Recover Password ?</span>
      </div>
      <el-button color="#009BA1" size="large" @click="login" type="primary" class="w-full font-bold text-red-200">Login</el-button>
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
              src="/assets/apple-logo-transparent.png" /></template
        ></el-button>
        <el-button class="w-20"
          ><template #default
            ><img
              style="width: 20px"
              alt=""
              src="/assets/vecteezy_facebook-logo-png-facebook-icon-transparent-png_18930476.png" /></template
        ></el-button>
      </div>
    </div>
    <div
      class="flex relative bg-[#009ca17a] h-full w-full justify-center items-center"
    >
      <div class="grad w-96 h-96 absolute top-32 right-32 -z-10"></div>
      <div class="grad_org w-96 h-96 absolute top-5 left-20 -z-10"></div>
      <div class="flex flex-col items-center">
        <div class="mt-10 relative z-10 p-10">
          <h1 class="text-5xl font-bold">Store Smarter, Access Faster</h1>
        </div>
        <div>
          <img class="w-[30rem]" src="/assets/14 Cloud Security.png" alt="" />
        </div>
      </div>
    </div>

    <!-- Background Gradient -->
  </div>
</template>

<script setup>
import { ref } from "vue";

const email = ref("");
const password = ref("");
</script>

<style scoped>
.grad {
  background: rgb(75, 104, 250);
  background: radial-gradient(
    circle 800px at center,
    rgba(75, 104, 250, 0.7) 0%,
    rgba(255, 255, 255, 0) 20%
  );
  z-index: -1; /* Make sure the gradient is behind the content */
}

.grad_org {
  background: rgb(250, 204, 75);
  background: radial-gradient(
    circle 700px at center,
    rgba(250, 204, 75, 0.7) 0%,
    rgba(255, 255, 255, 0) 30%
  );
}
</style>
