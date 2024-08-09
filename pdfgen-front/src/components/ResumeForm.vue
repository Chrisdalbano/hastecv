<template>
  <div class="p-6">
    <div class="flex items-center mb-4">
      <button
        @click="toggleView('form')"
        :class="{
          'bg-haste-yellow text-black ': view === 'form',
          'bg-black text-gray-200': view !== 'form',
        }"
        class="px-4 py-2 font-bold"
      >
        Manual
      </button>
      <button
        @click="toggleView('json')"
        :class="{
          'bg-haste-yellow text-black': view === 'json',
          'bg-black text-gray-200': view !== 'json',
        }"
        class="px-4 py-2 font-bold"
      >
        JSON
      </button>
    </div>
    <div v-show="view === 'form'">
      <form @submit.prevent="submitForm">
        <h2 class="text-2xl font-bold mb-4 text-white">Personal Information</h2>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <input
            v-model="store.resumeData.name"
            class="w-full p-2"
            type="text"
            placeholder="Name"
          />
          <input
            v-model="store.resumeData.title"
            class="w-full p-2"
            type="text"
            placeholder="Title"
          />
        </div>

        <h2 class="text-2xl font-bold mb-4 mt-6 text-white">
          Contact Information
        </h2>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <input
            v-model="store.resumeData.contact.email"
            class="w-full p-2"
            type="email"
            placeholder="Email"
          />
          <input
            v-model="store.resumeData.contact.phone"
            class="w-full p-2"
            type="tel"
            placeholder="Phone"
          />
          <input
            v-model="store.resumeData.contact.location"
            class="w-full p-2"
            type="text"
            placeholder="Location"
          />
          <input
            v-model="store.resumeData.contact.linkedin"
            class="w-full p-2"
            type="text"
            placeholder="LinkedIn"
          />
          <input
            v-model="store.resumeData.contact.github"
            class="w-full p-2"
            type="text"
            placeholder="GitHub"
          />
          <input
            v-model="store.resumeData.contact.website"
            class="w-full p-2"
            type="text"
            placeholder="Website"
          />
        </div>

        <h2 class="text-2xl font-bold mb-4 mt-6 text-white">Summary</h2>
        <textarea
          v-model="store.resumeData.summary"
          class="w-full p-2 bg-black border-solid border-2 border-whitesmoke text-white"
          rows="4"
          placeholder="Summary"
        ></textarea>

        <div
          v-for="(exp, index) in store.resumeData.experience"
          :key="index"
          class="mb-4 relative"
        >
          <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <input
              v-model="exp.position"
              class="w-full p-2 mb-2"
              type="text"
              placeholder="Position"
            />
            <input
              v-model="exp.company"
              class="w-full p-2 mb-2"
              type="text"
              placeholder="Company"
            />
            <input
              v-model="exp.dates"
              class="w-full p-2 mb-2"
              type="text"
              placeholder="Dates"
            />
          </div>
          <textarea
            v-model="exp.responsibilities"
            class="w-full p-2 mb-2"
            rows="3"
            placeholder="Responsibilities"
          ></textarea>
          <button
            @click.prevent="removeExperience(index)"
            class="absolute top-0 right-0 bg-red-500 text-white p-1 rounded-full"
          >
            x
          </button>
        </div>
        <div class="flex">
          <button
            @click.prevent="openModal('experience')"
            class="p-2 text-white font-bold rounded mt-2 mr-2"
          >
            Add Experience
          </button>

          <div
            v-for="(edu, index) in store.resumeData.education"
            :key="index"
            class="mb-4 relative"
          >
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
              <input
                v-model="edu.degree"
                class="w-full p-2 mb-2"
                type="text"
                placeholder="Degree"
              />
              <input
                v-model="edu.institution"
                class="w-full p-2 mb-2"
                type="text"
                placeholder="Institution"
              />
              <input
                v-model="edu.dates"
                class="w-full p-2 mb-2"
                type="text"
                placeholder="Dates"
              />
            </div>
            <button
              @click.prevent="removeEducation(index)"
              class="absolute top-0 right-0 bg-red-500 text-white p-1 rounded-full mx-2"
            >
              x
            </button>
          </div>
          <button
            @click.prevent="openModal('education')"
            class="text-white font-bold rounded mt-2 mx-4"
          >
            Add Education
          </button>

          <div
            v-for="(skill, index) in store.resumeData.skills"
            :key="index"
            class="mb-4 relative"
          >
            <input
              v-model="store.resumeData.skills[index]"
              class="w-full p-2 mb-2"
              type="text"
              placeholder="Skill"
            />
            <button
              @click.prevent="removeSkill(index)"
              class="absolute top-0 right-0 bg-red-500 text-white p-1 rounded-full"
            >
              x
            </button>
          </div>
          <button
            @click.prevent="openModal('skill')"
            class="text-white font-bold rounded mt-2 mx-4"
          >
            Add Skill
          </button>
        </div>

        <div></div>
        <button type="submit" class="haste-button">Generate Preview</button>
      </form>
    </div>

    <div v-if="view === 'json'">
      <JsonEditor />
    </div>

    <ReusableModal
      :show="showModal"
      :title="modalTitle"
      @close="closeModal"
      @save="saveEntry"
    >
      <template v-if="modalType === 'experience'">
        <input
          v-model="newEntry.position"
          class="w-full p-2 mb-2"
          type="text"
          placeholder="Position"
        />
        <input
          v-model="newEntry.company"
          class="w-full p-2 mb-2"
          type="text"
          placeholder="Company"
        />
        <input
          v-model="newEntry.dates"
          class="w-full p-2 mb-2"
          type="text"
          placeholder="Dates"
        />
        <textarea
          v-model="newEntry.responsibilities"
          class="w-full p-2 mb-2"
          rows="3"
          placeholder="Responsibilities"
        ></textarea>
      </template>
      <template v-if="modalType === 'education'">
        <input
          v-model="newEntry.degree"
          class="w-full p-2 mb-2"
          type="text"
          placeholder="Degree"
        />
        <input
          v-model="newEntry.institution"
          class="w-full p-2 mb-2"
          type="text"
          placeholder="Institution"
        />
        <input
          v-model="newEntry.dates"
          class="w-full p-2 mb-2"
          type="text"
          placeholder="Dates"
        />
      </template>
      <template v-show="modalType === 'skill'">
        <input
          v-model="newEntry.skill"
          class="w-full p-2 mb-2"
          type="text"
          placeholder="Skill"
        />
      </template>
    </ReusableModal>
  </div>
</template>

<script setup>
import { useResumeDataStore } from "../stores/resumeData";
import { ref } from "vue";

import ReusableModal from "./ReusableModal.vue";
import JsonEditor from "./JsonEditor.vue";

const store = useResumeDataStore();
const view = ref("form");
const showModal = ref(false);
const modalType = ref("");
const modalTitle = ref("");
const newEntry = ref({});
const emit = defineEmits(["submit"]);

function submitForm() {
  emit("submit", JSON.stringify(store.resumeData));
}

function openModal(type) {
  showModal.value = true;
  modalType.value = type;
  modalTitle.value = `Add ${type.charAt(0).toUpperCase() + type.slice(1)}`;
  newEntry.value = {};
}
function closeModal() {
  showModal.value = false;
  modalType.value = "";
  modalTitle.value = "";
  newEntry.value = {};
}
function saveEntry() {
  if (modalType.value === "experience") {
    store.resumeData.experience.push(newEntry.value);
  } else if (modalType.value === "education") {
    store.resumeData.education.push(newEntry.value);
  } else if (modalType.value === "skill") {
    store.resumeData.skills.push(newEntry.value.skill);
  }
  closeModal();
}
function removeExperience(index) {
  store.resumeData.experience.splice(index, 1);
}
function removeEducation(index) {
  store.resumeData.education.splice(index, 1);
}
function removeSkill(index) {
  store.resumeData.skills.splice(index, 1);
}
function toggleView(newView) {
  view.value = newView;
}
</script>

<style scoped></style>
