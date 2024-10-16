<template>
  <div class="mt-8">
    <!-- <h2 class="mb-4 text-2xl font-bold text-white">Edit JSON</h2> -->
    <form @submit.prevent="submitJson">
      <div ref="jsonEditor" class="my-12 h-[65vmin]"></div>
      <!-- <div class="flex items-center justify-center">
        <button type="submit" class="haste-button">Generate</button>
      </div> -->
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
