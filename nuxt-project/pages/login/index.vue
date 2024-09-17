<template>
  <div class="flex justify-center items-center h-screen gap-52 relative">
    <div class="flex relative">
      <div class="flex">
        <div class="mt-10 prose relative z-10 p-10">
          <h1>
            Securely store and access<br />
            your files <br />anytime, anywhere!
          </h1>
          <div class="grad w-96 h-96 absolute -bottom-20 -right-7 -z-10"></div>
          <div class="grad_org w-96 h-96 absolute -top-32 -left-32 -z-10"></div>
        </div>
        <div><img class="w-[30rem]" src="/assets/19 Internet of Things (IoT).png" alt="" /></div>
      </div>
    </div>
    <div class="flex flex-col items-center w-96 gap-5 relative z-10 mr-52">
      <div class="w-[60%] mb-7"></div>
      <el-input type="email" v-model="email" placeholder="Email" />
      <el-input
        type="password"
        show-password
        v-model="password"
        placeholder="Password"
      />
      <div class="relative w-full h-8">
        <span class="text-gray-300 absolute right-0">Recover Password ?</span>
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
    rgba(75, 104, 250, 0.3) 0%,
    rgba(255, 255, 255, 0) 20%
  );
  z-index: -1; /* Make sure the gradient is behind the content */
}

.grad_org {
  background: rgb(250, 204, 75);
  background: radial-gradient(
    circle 600px at center,
    rgba(250, 204, 75, 0.17690826330532217) 0%,
    rgba(255, 255, 255, 0) 30%
  );
}
</style>
