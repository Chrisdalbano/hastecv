<template>
  <div class="mt-8">
    <h2 class="text-2xl font-bold mb-4 text-white">Paste JSON Data</h2>
    <div ref="jsonEditor" class="my-12 h-72"></div>
    <button @click="submitJson" class="haste-button">
      Generate
    </button>
  </div>
</template>
<script setup>
import JSONEditor from "jsoneditor";
import { useResumeDataStore } from "../stores/resumeData";
import { ref, onMounted } from "vue";
import "jsoneditor/dist/jsoneditor.css";
import "ace-builds/src-noconflict/ace";
import "ace-builds/src-noconflict/theme-twilight";

const store = useResumeDataStore();
const jsonEditor = ref(null);
const editor = ref(null);
const emit = defineEmits(["submit"]);

onMounted(() => {
  const container = jsonEditor.value;
  editor.value = new JSONEditor(container, {
    modes: ["code", "form", "text", "tree", "view"],
    ace: window.ace,
    theme: "ace/theme/twilight",
  });
  editor.value.set(store.resumeData);
});

function submitJson() {
  try {
    const parsedData = editor.value.get();
    emit("submit", JSON.stringify(parsedData));
    store.resumeData = parsedData;
  } catch (error) {
    alert("Invalid JSON format");
  }
}
</script>
<style scoped></style>
