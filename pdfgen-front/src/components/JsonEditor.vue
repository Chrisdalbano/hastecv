<template>
  <div ref="jsonEditor" class="my-12 h-[65vmin]"></div>
</template>

<script setup>
import JSONEditor from "jsoneditor";
import { ref, onMounted, onUnmounted } from "vue";
import { useResumeDataStore } from "@/stores/resumeData";

const store = useResumeDataStore();
const jsonEditor = ref(null);
const editor = ref(null);

// Initialize the JSONEditor
onMounted(() => {
  const container = jsonEditor.value;
  editor.value = new JSONEditor(container, {
    modes: ["code", "form", "text", "tree", "view"],
    ace: window.ace,
    theme: "ace/theme-twilight"
  });

  // Set the initial data in the editor
  editor.value.set(store.resumeData);

  // Watch for changes in the JSONEditor and update the store
  editor.value.on("change", () => {
    try {
      const updatedData = editor.value.get(); // Get the updated JSON from editor
      store.updateResumeData(updatedData); // Update the store in real-time
    } catch (error) {
      console.error("Invalid JSON format", error);
    }
  });
});

// Cleanup the editor on unmount
onUnmounted(() => {
  if (editor.value) {
    editor.value.destroy();
  }
});
</script>

<style scoped></style>
