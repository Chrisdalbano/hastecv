import { defineStore } from 'pinia';
import { ref, computed } from 'vue';
import { useResumeDataStore } from './resumeData';

export const useCanvasStore = defineStore('canvas', () => {
  const resumeStore = useResumeDataStore();
  
  // Default sections in order (NO DIVIDERS by default!)
  const sections = ref([
    { 
      id: 'header-1', 
      type: 'header', 
      enabled: true, 
      width: '100%', 
      height: 'auto',
      padding: 'small',
      order: 0
    },
    { 
      id: 'summary-1', 
      type: 'summary', 
      enabled: true, 
      width: '100%', 
      height: 'auto',
      padding: 'small',
      order: 1
    },
    { 
      id: 'technical_proficiency-1', 
      type: 'technical_proficiency', 
      enabled: true, 
      width: '100%', 
      height: 'auto',
      padding: 'small',
      order: 2
    },
    { 
      id: 'experience-1', 
      type: 'experience', 
      enabled: true, 
      width: '100%', 
      height: 'auto',
      padding: 'small',
      order: 3
    },
    { 
      id: 'projects-1', 
      type: 'projects', 
      enabled: false, 
      width: '100%', 
      height: 'auto',
      padding: 'small',
      order: 4
    },
    { 
      id: 'education-1', 
      type: 'education', 
      enabled: true, 
      width: '100%', 
      height: 'auto',
      padding: 'small',
      order: 5
    },
    { 
      id: 'skills-1', 
      type: 'skills', 
      enabled: true, 
      width: '100%', 
      height: 'auto',
      padding: 'small',
      order: 6
    }
  ]);

  // Get enabled sections in order
  const enabledSections = computed(() => {
    return sections.value
      .filter(s => s.enabled)
      .sort((a, b) => a.order - b.order);
  });

  // Get next ID for section type
  let sectionCounter = 1;
  function getNextId(type) {
    return `${type}-${Date.now()}-${sectionCounter++}`;
  }

  // Add a new section
  function addSection(type) {
    const newSection = {
      id: getNextId(type),
      type: type,
      enabled: true,
      width: '100%',
      height: type === 'spacer' ? '20px' : 'auto',
      padding: type === 'divider' || type === 'spacer' ? 'none' : 'medium',
      order: sections.value.length,
      // Spacer/divider specific
      ...(type === 'spacer' && { color: 'transparent' }),
      ...(type === 'divider' && { color: '#cccccc', thickness: '1px' })
    };
    
    sections.value.push(newSection);
    return newSection;
  }

  // Remove a section
  function removeSection(id) {
    const index = sections.value.findIndex(s => s.id === id);
    if (index !== -1) {
      sections.value.splice(index, 1);
      // Reorder remaining sections
      sections.value.forEach((s, i) => s.order = i);
    }
  }

  // Move section up
  function moveUp(id) {
    const index = sections.value.findIndex(s => s.id === id);
    if (index > 0) {
      // Swap with previous
      const temp = sections.value[index - 1];
      sections.value[index - 1] = sections.value[index];
      sections.value[index] = temp;
      
      // Update orders
      sections.value[index - 1].order = index - 1;
      sections.value[index].order = index;
    }
  }

  // Move section down
  function moveDown(id) {
    const index = sections.value.findIndex(s => s.id === id);
    if (index < sections.value.length - 1) {
      // Swap with next
      const temp = sections.value[index + 1];
      sections.value[index + 1] = sections.value[index];
      sections.value[index] = temp;
      
      // Update orders
      sections.value[index].order = index;
      sections.value[index + 1].order = index + 1;
    }
  }

  // Update section properties
  function updateSection(id, updates) {
    const section = sections.value.find(s => s.id === id);
    if (section) {
      Object.assign(section, updates);
    }
  }

  // Toggle section enabled/disabled
  function toggleSection(id) {
    const section = sections.value.find(s => s.id === id);
    if (section) {
      section.enabled = !section.enabled;
    }
  }

  // Generate layout JSON for backend
  function generateLayout() {
    return {
      version: '1.0',
      template: resumeStore.template,
      sections: enabledSections.value.map(section => ({
        type: section.type,
        width: section.width,
        height: section.height,
        padding: section.padding,
        ...(section.type === 'spacer' && { color: section.color }),
        ...(section.type === 'divider' && { 
          color: section.color, 
          thickness: section.thickness 
        }),
        data: getSectionData(section.type)
      }))
    };
  }

  // Get data for a section type from resume store
  function getSectionData(type) {
    const data = resumeStore.resumeData;
    
    switch (type) {
      case 'header':
        return {
          name: data.name,
          title: data.title,
          contact: data.contact
        };
      case 'summary':
        return { summary: data.summary };
      case 'experience':
        return { experience: data.experience };
      case 'education':
        return { education: data.education };
      case 'skills':
        return { skills: data.skills };
      case 'projects':
        return { projects: data.projects };
      case 'technical_proficiency':
        return { technical_proficiency: data.technical_proficiency };
      case 'spacer':
      case 'divider':
        return null;
      default:
        return {};
    }
  }

  // Reset to default sections
  function resetSections() {
    sections.value = [
      { id: 'header-1', type: 'header', enabled: true, width: '100%', height: 'auto', padding: 'small', order: 0 },
      { id: 'summary-1', type: 'summary', enabled: true, width: '100%', height: 'auto', padding: 'small', order: 1 },
      { id: 'technical_proficiency-1', type: 'technical_proficiency', enabled: true, width: '100%', height: 'auto', padding: 'small', order: 2 },
      { id: 'experience-1', type: 'experience', enabled: true, width: '100%', height: 'auto', padding: 'small', order: 3 },
      { id: 'projects-1', type: 'projects', enabled: false, width: '100%', height: 'auto', padding: 'small', order: 4 },
      { id: 'education-1', type: 'education', enabled: true, width: '100%', height: 'auto', padding: 'small', order: 5 },
      { id: 'skills-1', type: 'skills', enabled: true, width: '100%', height: 'auto', padding: 'small', order: 6 }
    ];
  }

  return {
    sections,
    enabledSections,
    addSection,
    removeSection,
    moveUp,
    moveDown,
    updateSection,
    toggleSection,
    generateLayout,
    resetSections
  };
});

