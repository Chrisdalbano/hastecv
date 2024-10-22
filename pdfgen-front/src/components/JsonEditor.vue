<template>
  <div class="mt-8">
    <div ref="jsonEditor" class="my-12 h-[65vmin]"></div>
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
let isUpdatingFromEditor = false; // Flag to avoid circular updates

// Initialize the JSONEditor on mounted
onMounted(() => {
  const container = jsonEditor.value;
  editor.value = new JSONEditor(container, {
    modes: ["code", "form", "text", "tree", "view"],
    ace: window.ace,
    theme: "ace/theme/twilight",
    onChange: () => {
      // When the user changes the data in the editor, update the store
      try {
        const updatedData = editor.value.get(); // Get the new data from the editor
        isUpdatingFromEditor = true;
        store.resumeData = updatedData; // Update the store with the new data
      } catch (error) {
        console.error("Failed to parse JSON data:", error);
      } finally {
        isUpdatingFromEditor = false; // Reset flag
      }
    }
  });

  // Set the initial data from the store
  editor.value.set(store.resumeData);
});

// Watch the store and update the editor when the store changes
watch(
  () => store.resumeData,
  (newData) => {
    // Avoid circular updates: only update the editor if the change did not come from the editor itself
    if (!isUpdatingFromEditor && editor.value) {
      editor.value.update(newData);
    }
  },
  { deep: true } // Deep watch to capture nested changes
);

onUnmounted(() => {
  if (editor.value) {
    editor.value.destroy();
  }
});
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
          "Directly modify your resume structure using HasteCV JSON resume editor for ultimate control."
      }
    ]
  }
};
</script>

<style scoped></style>
