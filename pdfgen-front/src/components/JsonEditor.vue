<template>
  <div class="mt-8">
    <form @submit.prevent="submitJson">
      <div ref="jsonEditor" class="my-12 h-[65vmin]"></div>
    </form>
  </div>
</template>

<script setup>
import JSONEditor from "jsoneditor";
import { useResumeDataStore } from "@/stores/resumeData";
import { ref, onMounted, watch, onUnmounted } from "vue";
import "jsoneditor/dist/jsoneditor.css";
import "ace-builds/src-noconflict/ace";
import "ace-builds/src-noconflict/theme-twilight";

const store = useResumeDataStore();
const jsonEditor = ref(null);
const editor = ref(null);

// Initialize the JSONEditor on mounted
onMounted(() => {
  const container = jsonEditor.value;
  editor.value = new JSONEditor(container, {
    modes: ["code", "form", "text", "tree", "view"],
    ace: window.ace,
    theme: "ace/theme/twilight"
  });

  // Set the initial data from the store
  editor.value.set(store.resumeData);
});

// Watch for changes in the store's resumeData and update the editor
watch(
  () => store.resumeData, // watching the resumeData from the store
  (newData) => {
    if (editor.value) {
      editor.value.update(newData); // use update to avoid losing focus on small changes
    }
  },
  { deep: true } // deep watching ensures nested changes are detected
);

// Cleanup the editor instance on component unmount
onUnmounted(() => {
  if (editor.value) {
    editor.value.destroy();
  }
});

// Handle form submission
function submitJson() {
  try {
    const parsedData = editor.value.get();
    store.resumeData = parsedData; // Update the store with the new JSON data
    store.generatePdf(parsedData);
  } catch (error) {
    alert("Invalid JSON format");
  }
}
</script>

<script>
export default {
  useHead: {
    title: "HasteCV - JSON Resume Editor",
    meta: [
      {
        name: "description",
        content:
          "Advanced users can modify their resume directly in JSON format using HasteCV’s powerful editor."
      },
      {
        name: "keywords",
        content:
          "resume editor, JSON editor, advanced resume creation, ATS resume"
      },
      { property: "og:title", content: "HasteCV - JSON Resume Editor" },
      {
        property: "og:description",
        content:
          "Directly modify your resume structure using HasteCV’s JSON resume editor for ultimate control."
      }
    ]
  }
};
</script>

<style scoped></style>
