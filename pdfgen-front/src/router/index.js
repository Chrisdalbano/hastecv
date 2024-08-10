import { createWebHistory, createRouter } from "vue-router";

import HomeView from "../views/HomeView.vue";
import JsonEditor from "@/components/JsonEditor.vue";
import ResumeForm from "@/components/home/ResumeForm.vue";

const routes = [
  {
    path: "/",
    component: HomeView,

    children: [
      {
        path: "",
        component: ResumeForm
      },
      {
        path: "/json",
        component: JsonEditor
      }
    ]
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
