// https://nuxt.com/docs/api/configuration/nuxt-config

export default defineNuxtConfig({
  modules: ["@element-plus/nuxt", "@nuxt/icon"],

  compatibilityDate: "2024-04-03",
  devtools: { enabled: true },
  css: [
    "~/assets/css/main.css", // TailwindCSS styles
    "element-plus/theme-chalk/index.css", // Element Plus default theme
    "element-plus/theme-chalk/dark/css-vars.css", // Element Plus dark theme

  ],
  postcss: {
    plugins: {
      tailwindcss: {},
      autoprefixer: {},
    },
  },
  build: {
    transpile: ["element-plus"],
  },
});