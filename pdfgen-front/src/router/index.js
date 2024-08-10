import { createMemoryHistory, createRouter } from "vue-router";

import HomeView from "../views/HomeView.vue";
import JsonEditor from "@/components/JsonEditor.vue";

const routes = [
  {
    path: "/",
    component: HomeView,

    children: [
      {
        name: "json",
        path: "json",
        component: JsonEditor
      }
    ]
  }
];

const router = createRouter({
  history: createMemoryHistory(),
  routes
});

export default router;
