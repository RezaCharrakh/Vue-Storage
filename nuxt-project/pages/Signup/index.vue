<template>
  <div class="flex justify-center items-center h-screen gap-52 relative">
    <div class="absolute top-10 left-10 flex items-center gap-2">
      <img class="w-20" src="/assets/V-Cloud logo.png" alt="" />
      <h1 class="text-4xl font-bold text-[#009BA1]">V-Cloud</h1>
    </div>
    <div
      class="flex flex-col items-center w-[700px] gap-5 relative z-10 ml-52 prose"
    >
      <div>
        <h2 class="text-4xl">Sign up</h2>
      </div>

      <el-form
        :model="form"
        :rules="rules"
        ref="signUpForm"
        class="sign-up-form"
      >
        <el-form-item
          label-width="90"
          label-position="top"
          label="Username"
          prop="username"
        >
          <el-input
            v-model="form.username"
            placeholder="Enter your username"
          ></el-input>
        </el-form-item>

        <el-form-item
          label-width="90"
          label-position="top"
          label="Email"
          prop="email"
        >
          <el-input
            v-model="form.email"
            placeholder="Enter your email"
          ></el-input>
        </el-form-item>

        <div class="flex flex-row justify-between">
          <el-form-item label-position="top" label="Password" prop="password">
            <div>
              <el-input
                style="width: 220px"
                type="password"
                v-model="form.password"
                placeholder="Enter your password"
              ></el-input>
            </div>
          </el-form-item>

          <el-form-item
            label-position="top"
            label="Confirm Password"
            prop="confirmPassword"
          >
            <div>
              <el-input
                style="width: 220px"
                type="password"
                v-model="form.confirmPassword"
                placeholder="Confirm your password"
              ></el-input>
            </div>
          </el-form-item>
        </div>

        <el-form-item prop="acceptRules">
          <el-checkbox v-model="form.acceptRules"
            >I accept the rules</el-checkbox
          >
        </el-form-item>

        <el-form-item>
          <el-button
            color="#009BA1"
            size="large"
            @click="submitForm('signUpForm')"
            type="primary"
            class="w-full"
            >Sign up</el-button
          >
        </el-form-item>
      </el-form>

      <div class="relative w-full h-8">
        <span class="text-gray-300 absolute right-0">Have an account ?</span>
      </div>

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
          <img class="w-[30rem]" src="/assets/25 Add Cloud.png" alt="" />
        </div>
      </div>
    </div>

    <!-- Background Gradient -->
  </div>
</template>

<script setup>
import { reactive, ref } from "vue";
import { ElMessage } from "element-plus";

const form = reactive({
  username: "",
  email: "",
  password: "",
  confirmPassword: "",
  acceptRules: false,
});

const rules = {
  username: [
    { required: true, message: "Please input your username", trigger: "blur" },
  ],
  email: [
    { required: true, message: "Please input your email", trigger: "blur" },
    {
      type: "email",
      message: "Please input a valid email",
      trigger: ["blur", "change"],
    },
  ],
  password: [
    { required: true, message: "Please input your password", trigger: "blur" },
  ],
  confirmPassword: [
    {
      required: true,
      message: "Please confirm your password",
      trigger: "blur",
    },
    {
      validator: (rule, value, callback) => {
        if (value !== form.password) {
          callback(new Error("Passwords do not match"));
        } else {
          callback();
        }
      },
      trigger: "blur",
    },
  ],
  acceptRules: [
    { required: true, message: "You must accept the rules", trigger: "change" },
  ],
};

const signUpForm = ref(null);

const submitForm = () => {
  signUpForm.value.validate((valid) => {
    if (valid) {
      ElMessage.success("Sign up successful!");
    } else {
      ElMessage.error("Please fix the errors before submitting");
      return false;
    }
  });
};
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

.sign-up-form {
  width: 500px;
  padding: 20px;
  border-radius: 8px;
  background-color: white;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.1);
}
</style>
