import { createApp } from "vue";
import { createPinia } from "pinia";

import App from "./App.vue";
import router from "./router";

import "@/assets/tailwind.css";
import "@/assets/global.css";
import "@/assets/fonts.css";

import "ace-builds/src-noconflict/ace";
import "ace-builds/src-noconflict/theme-twilight";
import "jsoneditor/dist/jsoneditor.css";

const pinia = createPinia();
createApp(App).use(router).use(pinia).mount("#app");
