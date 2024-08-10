<template>
  <div class="mt-8">
    <h2 class="mb-4 text-2xl font-bold text-white">Edit JSON</h2>
    <form @submit.prevent="submitForm">
      <div ref="jsonEditor" class="my-12 h-72"></div>
      <button type="submit" @click="submitJson" class="haste-button">
        Generate
      </button>
    </form>
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
    theme: "ace/theme/twilight"
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

function submitForm() {
  emit("submit", JSON.stringify(store.resumeData));
}
</script>
<style scoped></style>
