<template>
  <div>
    <form @submit.prevent="generatePdf">
      <fieldset class="mt-10 space-y-10">
        <div class="grid grid-cols-1 gap-x-6 gap-y-10 md:grid-cols-2">
          <TextInput
            v-model="store.resumeData.name"
            label="name"
            id="name-input"
          />
          <TextInput
            v-model="store.resumeData.title"
            label="title"
            id="title-input"
          />

          <TextInput
            v-model="store.resumeData.contact.email"
            label="email"
            id="email-input"
          />

          <TextInput
            v-model="store.resumeData.contact.phone"
            label="phone"
            id="phone-input"
          />

          <TextInput
            v-model="store.resumeData.contact.location"
            label="location"
            id="location-input"
          />

          <TextInput
            v-model="store.resumeData.contact.website"
            label="website"
            id="website-input"
          />
        </div>

        <AreaTextInput
          v-model="store.resumeData.summary"
          label="Summary"
          id="summary-input"
        />
      </fieldset>
      <div class="flex flex-col">
        <button @click.prevent="openModal('experience')" class="haste-option">
          + EXPERIENCE
        </button>
        <div
          v-for="(exp, index) in store.resumeData.experience"
          :key="index"
          class="relative my-4"
        >
          <div
            class="grid grid-cols-1 gap-4 bg-black bg-opacity-50 p-2 md:grid-cols-2"
          >
            <input
              v-model="exp.position"
              class="my-1 w-full p-2"
              type="text"
              placeholder="POSITION"
            />
            <input
              v-model="exp.company"
              class="my-1 w-full p-2"
              type="text"
              placeholder="COMPANY"
            />
            <input
              v-model="exp.dates"
              class="my-1 w-full p-2"
              type="text"
              placeholder="DATES"
            />
          </div>
          <textarea
            v-model="exp.responsibilities"
            class="mb-2 w-full bg-black bg-opacity-50 p-2"
            rows="3"
            placeholder="RESPONSIBILITIES"
            style="white-space: pre-wrap"
          ></textarea>

          <button
            @click.prevent="removeExperience(index)"
            class="remove-sub-button"
          >
            x
          </button>
        </div>
      </div>

      <div class="flex flex-col">
        <button @click.prevent="openModal('education')" class="haste-option">
          + EDUCATION
        </button>
        <div
          v-for="(edu, index) in store.resumeData.education"
          :key="index"
          class="relative mb-4"
        >
          <div
            class="grid grid-cols-1 gap-4 bg-black bg-opacity-50 md:grid-cols-2"
          >
            <input
              v-model="edu.degree"
              class="mb-2 w-full p-2"
              type="text"
              placeholder="DEGREE"
            />
            <input
              v-model="edu.institution"
              class="mb-2 w-full p-2"
              type="text"
              placeholder="INSTITUTION"
            />
            <input
              v-model="edu.dates"
              class="mb-2 w-full p-2"
              type="text"
              placeholder="DATES"
            />
          </div>
          <button
            @click.prevent="removeEducation(index)"
            class="remove-sub-button"
          >
            x
          </button>
        </div>
      </div>
      <div class="start flex w-auto flex-col">
        <button @click.prevent="addSkill" class="haste-option">+ SKILL</button>

        <ul v-auto-animate class="flex flex-wrap items-start">
          <li
            v-for="(skill, index) in store.resumeData.skills"
            :key="index"
            class="relative mb-4 w-[33%] p-1"
          >
            <input
              v-model="store.resumeData.skills[index]"
              class="mb-2 w-full p-2"
              type="text"
              placeholder="Skill"
            />
            <button
              @click.prevent="removeSkill(index)"
              class="remove-sub-button"
            >
              x
            </button>
          </li>
        </ul>
      </div>
      <div class="flex items-center justify-center">
        <button type="submit" class="haste-button">GENERATE</button>
      </div>
    </form>

    <ReusableModal
      :show="showModal"
      :title="modalTitle"
      @close="closeModal"
      @save="saveEntry"
    >
      <div v-if="modalType == 'education'">
        <input
          v-model="newEntry.degree"
          class="mb-2 w-full p-2"
          type="text"
          placeholder="Degree"
        />
        <input
          v-model="newEntry.institution"
          class="mb-2 w-full p-2"
          type="text"
          placeholder="Institution"
        />
        <input
          v-model="newEntry.dates"
          class="mb-2 w-full p-2"
          type="text"
          placeholder="Dates"
        />
      </div>
      <div v-else-if="modalType == 'experience'">
        <input
          v-model="newEntry.position"
          class="mb-2 w-full p-2"
          type="text"
          placeholder="Position"
        />
        <input
          v-model="newEntry.company"
          class="mb-2 w-full p-2"
          type="text"
          placeholder="Company"
        />
        <input
          v-model="newEntry.dates"
          class="mb-2 w-full p-2"
          type="text"
          placeholder="Dates"
        />
        <textarea
          v-model="newEntry.responsibilities"
          class="mb-2 w-full p-2"
          rows="3"
          placeholder="Responsibilities"
        ></textarea>
      </div>
    </ReusableModal>
  </div>
</template>

<script setup>
import { useResumeDataStore } from "@/stores/resumeData";
import { ref } from "vue";
import TextInput from "@/components/home/resume_form/TextInput.vue";
import AreaTextInput from "@/components/home/resume_form/AreaTextInput.vue";

import ReusableModal from "@/components/ReusableModal.vue";

const store = useResumeDataStore();
const showModal = ref(false);
const modalType = ref("");
const modalTitle = ref("");
const newEntry = ref({});

function generatePdf() {
  store.generatePdf(JSON.stringify(store.resumeData));
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
  }
  closeModal();
}

function addSkill() {
  store.resumeData.skills.push(newEntry.value.skill);
}

function removeSkill(index) {
  store.resumeData.skills.splice(index, 1);
}

// function updateResponsibilities(index, value) {
//   store.resumeData.experience[index].responsibilities = value
//     .split(/\n+/)
//     .map((item) => item.trim())
//     .filter(Boolean);
// }

function removeExperience(index) {
  store.resumeData.experience.splice(index, 1);
}
function removeEducation(index) {
  store.resumeData.education.splice(index, 1);
}
</script>

<style scoped>
input,
textarea {
  font-size: 20px;
  font-weight: 600;

  font-family: monospace;
}
</style>
