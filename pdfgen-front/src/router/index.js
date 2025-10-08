import { createWebHistory, createRouter } from "vue-router";
import LandingView from "../views/LandingView.vue";
import HomeView from "../views/HomeView.vue"; // Main app view
import JsonEditor from "@/components/JsonEditor.vue"; // JSON editor component
import ResumeForm from "@/components/home/ResumeForm.vue"; // Manual CV creation component
import VisualBuilder from "@/components/visual-builder/VisualBuilder.vue"; // Visual builder component

const routes = [
  {
    path: "/", // Landing page route
    component: LandingView
  },
  {
    path: "/app", // Main app route (formerly at "/")
    component: HomeView,
    children: [
      {
        path: "", // Default child (manual CV creation)
        name: "ManualCV",
        component: ResumeForm
      },
      {
        path: "json", // JSON editor route
        name: "JsonEditor",
        component: JsonEditor
      },
      {
        path: "visual", // Visual builder route
        name: "VisualBuilder",
        component: VisualBuilder
      }
    ]
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

router.afterEach((to) => {
  if (typeof window._mfq !== "undefined") {
    window._mfq.push(["newPageView", to.fullPath]);
  }
});
export default router;
