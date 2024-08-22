<template>
  <div class="mt-8">
    <h2 class="mb-4 text-2xl font-bold text-white">Edit JSON</h2>
    <form @submit.prevent="submitJson">
      <div ref="jsonEditor" class="my-12 h-[45vmin]"></div>
      <button type="submit" class="haste-button">Generate</button>
    </form>
  </div>
</template>

<script setup>
import JSONEditor from "jsoneditor";
import { useResumeDataStore } from "@/stores/resumeData";
import { ref, onMounted } from "vue";
import "jsoneditor/dist/jsoneditor.css";
import "ace-builds/src-noconflict/ace";
import "ace-builds/src-noconflict/theme-twilight";

const store = useResumeDataStore();
const jsonEditor = ref(null);
const editor = ref(null);

onMounted(() => {
  const container = jsonEditor.value;
  editor.value = new JSONEditor(container, {
    modes: ["code", "form", "text", "tree", "view"],
    ace: window.ace,
    theme: "ace/theme/twilight"
  });
  editor.value.set(store.resumeData);
});

function submitJson() {
  try {
    const parsedData = editor.value.get();
    store.resumeData = parsedData;
    store.generatePdf(parsedData);
  } catch (error) {
    alert("Invalid JSON format");
  }
}
</script>
<style scoped></style>
