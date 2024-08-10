<template>
  <div class="py-4">
    <div class="mb-4 flex items-center">
      <div class="switch-toggle">
        <button
          @click="toggleView('form')"
          :class="{
            active: view === 'form',
            inactive: view !== 'form'
          }"
          class="switch-toggle-button"
        >
          Manual
        </button>
        <button
          @click="toggleView('json')"
          :class="{
            active: view === 'json',
            inactive: view !== 'json'
          }"
          class="switch-toggle-button"
        >
          JSON
        </button>
      </div>
    </div>
  </div>

  <div class="py-4">
    <div v-show="view === 'form'">
      <form @submit.prevent="submitForm">
        <div class="grid grid-cols-1 gap-4 md:grid-cols-2">
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

        <div class="mt-10 grid grid-cols-1 gap-4 md:grid-cols-2">
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
            v-model="store.resumeData.contact.website"
            class="w-full p-2"
            type="text"
            placeholder="Website"
          />
        </div>

        <textarea
          v-model="store.resumeData.summary"
          class="mt-10 w-full p-2 text-3xl font-bold"
          rows="4"
          placeholder="Summary"
        ></textarea>

        <div
          v-for="(exp, index) in store.resumeData.experience"
          :key="index"
          class="relative mb-4"
        >
          <div class="grid grid-cols-1 gap-4 md:grid-cols-2">
            <input
              v-model="exp.position"
              class="mb-2 w-full p-2"
              type="text"
              placeholder="Position"
            />
            <input
              v-model="exp.company"
              class="mb-2 w-full p-2"
              type="text"
              placeholder="Company"
            />
            <input
              v-model="exp.dates"
              class="mb-2 w-full p-2"
              type="text"
              placeholder="Dates"
            />
          </div>
          <textarea
            v-model="exp.responsibilities"
            class="mb-2 w-full p-2"
            rows="3"
            placeholder="Responsibilities"
          ></textarea>
          <button
            @click.prevent="removeExperience(index)"
            class="absolute right-0 top-0 rounded-full bg-red-500 p-1 text-white"
          >
            x
          </button>
        </div>
        <div class="flex flex-wrap items-center text-center">
          <button @click.prevent="openModal('experience')" class="haste-option">
            + Experience
          </button>

          <div
            v-for="(edu, index) in store.resumeData.education"
            :key="index"
            class="relative mb-4"
          >
            <div class="grid grid-cols-1 gap-4 md:grid-cols-2">
              <input
                v-model="edu.degree"
                class="mb-2 w-full p-2"
                type="text"
                placeholder="Degree"
              />
              <input
                v-model="edu.institution"
                class="mb-2 w-full p-2"
                type="text"
                placeholder="Institution"
              />
              <input
                v-model="edu.dates"
                class="mb-2 w-full p-2"
                type="text"
                placeholder="Dates"
              />
            </div>
            <button
              @click.prevent="removeEducation(index)"
              class="absolute right-0 top-0 mx-2 rounded-full bg-red-500 p-1 text-white"
            >
              x
            </button>
          </div>
          <button @click.prevent="openModal('education')" class="haste-option">
            + Education
          </button>

          <div
            v-for="(skill, index) in store.resumeData.skills"
            :key="index"
            class="relative mb-4"
          >
            <input
              v-model="store.resumeData.skills[index]"
              class="mb-2 w-full p-2"
              type="text"
              placeholder="Skill"
            />
            <button
              @click.prevent="removeSkill(index)"
              class="absolute right-0 top-0 rounded-full bg-red-500 p-1 text-white"
            >
              x
            </button>
          </div>
          <button @click.prevent="addSkill" class="haste-option">
            + Skill
          </button>
          <button type="submit" class="haste-button">Generate</button>
        </div>

        <div></div>
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
      </template>
      <template v-if="modalType === 'education'">
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
  }
  closeModal();
}

function addSkill() {
  store.resumeData.skills.push(newEntry.value.skill);
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

<style scoped>
.switch-toggle {
  --width: 260px;
  --height: 60px;

  position: relative;
  width: var(--width);
  height: var(--height);

  background: transparent;
  border: 1px solid var(--haste-yellow);
  display: flex;
  justify-content: space-between;
}

.switch-toggle-button {
  flex: 1;
  padding: 10px 0;
  font-size: 24px;
  font-weight: 500;
  text-align: center;
  border-radius: calc(var(--radius) - var(--offset));
  transition:
    background-color 250ms cubic-bezier(0.93, 0.26, 0.07, 0.69),
    color 250ms cubic-bezier(0.93, 0.26, 0.07, 0.69);
}

.switch-toggle-button.active {
  background-color: var(--haste-yellow);
  color: var(--primary-black);
}

.switch-toggle-button.inactive {
  background-color: transparent;
  color: var(--haste-yellow);
}
</style>
