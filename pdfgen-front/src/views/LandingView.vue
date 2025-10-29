<template>
  <div class="bg-primary-black text-whitesmoke font-OpenSans">
    <!-- Hero Section -->
    <section class="hero bg-primary-black text-whitesmoke">
      <div class="center px-4">
        <div class="hero-content">
          <!-- Content Side -->
          <div class="hero-text-content">
            <h1 class="hero-title">
              Rapidly Build Resumes
              <span class="title-highlight">That Get Results</span>
            </h1>
            
            <p class="hero-description">
              Build ATS-optimized resumes with our intuitive editor. Choose from professional 
              themes, customize layouts, and export to PDF in minutes. No design skills required.
            </p>

            <div class="hero-actions">
              <button @click="navigateToApp" class="btn-primary">
                <span>Build Your Resume</span>
                <svg width="20" height="20" viewBox="0 0 20 20" fill="none">
                  <path d="M7.5 15L12.5 10L7.5 5" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
              </button>
              <button @click="scrollToExamples" class="btn-secondary">
                About HasteCV
              </button>
            </div>

            <div class="hero-stats">
              <div class="stat-item">
                <div class="stat-value">100%</div>
                <div class="stat-label">Free Forever</div>
              </div>
              <div class="stat-divider"></div>
              <div class="stat-item">
                <div class="stat-value">Customizable</div>
                <div class="stat-label">Themes</div>
              </div>
              <div class="stat-divider"></div>
              <div class="stat-item">
                <div class="stat-value">ATS</div>
                <div class="stat-label">Optimized</div>
              </div>
            </div>
          </div>
          
          <!-- 3D Cube Animation - Right Side -->
          <div class="cube-container" ref="cubeContainer">
            <div class="cube" v-for="(cube, idx) in 3" :key="idx" :class="`cube-${idx + 1}`">
              <div v-for="col in 3" :key="col" :style="{ '--x': col - 2, '--y': 0 }">
                <span v-for="row in 3" :key="row" :style="{ '--i': 4 - row }"></span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Live Stats Section -->
    <section class="stats-showcase">
      <div class="center">
        <div class="stats-grid">
          <div v-for="(stat, index) in liveStats" :key="index" class="stat-card" :ref="el => statCards[index] = el">
            <div class="stat-icon-wrapper">
              <component :is="stat.icon" class="stat-icon" />
            </div>
            <div class="stat-number" :data-target="stat.value">0</div>
            <div class="stat-label">{{ stat.label }}</div>
            <div class="stat-sublabel">{{ stat.sublabel }}</div>
          </div>
        </div>
      </div>
    </section>

    <!-- Interactive Demo Section -->
    <section class="demo-section" id="live-demo">
      <div class="center">
        <div class="section-header">
          <div class="badge-pill">
            <span class="badge-dot"></span>
            Live Demo
          </div>
          <h2 class="section-title">See It In Action</h2>
          <p class="section-description">
            Watch how HasteCV transforms your data into professional resumes in real-time
          </p>
        </div>

        <div class="demo-container">
          <div class="demo-tabs">
            <button 
              v-for="(tab, index) in demoTabs" 
              :key="index"
              :class="['demo-tab', { active: activeDemoTab === index }]"
              @click="activeDemoTab = index"
            >
              <component :is="tab.icon" class="tab-icon" />
              {{ tab.label }}
            </button>
          </div>

          <div class="demo-content">
            <!-- Templates Demo -->
            <div v-if="activeDemoTab === 0" class="demo-panel">
              <div class="templates-showcase">
                <div 
                  v-for="(template, index) in availableTemplates" 
                  :key="index"
                  :class="['template-card', { selected: selectedTemplate === index }]"
                  @click="selectedTemplate = index"
                >
                  <div class="template-preview">
                    <div class="template-thumbnail" :style="{ background: template.gradient }">
                      <div class="template-lines">
                        <div class="line" v-for="i in 5" :key="i"></div>
                      </div>
                    </div>
                  </div>
                  <div class="template-info">
                    <h4>{{ template.name }}</h4>
                    <p>{{ template.description }}</p>
                    <div class="template-tags">
                      <span v-for="tag in template.tags" :key="tag" class="tag">{{ tag }}</span>
                    </div>
                  </div>
                  <div class="selected-badge" v-if="selectedTemplate === index">
                    <svg width="20" height="20" viewBox="0 0 20 20" fill="none">
                      <path d="M16.6667 5L7.50004 14.1667L3.33337 10" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                    </svg>
                  </div>
                </div>
              </div>
            </div>

            <!-- Customization Demo -->
            <div v-if="activeDemoTab === 1" class="demo-panel">
              <div class="customization-showcase">
                <div class="custom-option" v-for="(option, index) in customOptions" :key="index">
                  <div class="option-header">
                    <component :is="option.icon" class="option-icon" />
                    <div>
                      <h4>{{ option.title }}</h4>
                      <p>{{ option.description }}</p>
                    </div>
                  </div>
                  <div class="option-examples">
                    <div 
                      v-for="example in option.examples" 
                      :key="example"
                      class="example-chip"
                    >
                      {{ example }}
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <!-- Speed Demo -->
            <div v-if="activeDemoTab === 2" class="demo-panel">
              <div class="speed-showcase">
                <div class="speed-metric">
                  <div class="metric-visual">
                    <div class="progress-ring">
                      <svg width="200" height="200">
                        <circle cx="100" cy="100" r="90" />
                        <circle cx="100" cy="100" r="90" :style="{ strokeDashoffset: speedProgress }" />
                      </svg>
                      <div class="metric-value">
                        <span class="big-number">{{ generationTime }}</span>
                        <span class="unit">seconds</span>
                      </div>
                    </div>
                  </div>
                  <h3>Lightning Fast Generation</h3>
                  <p>Average PDF generation time from data input to download</p>
                  <div class="speed-features">
                    <div class="speed-feature">
                      <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
                        <path d="M13 2L3 14h8l-1 8 10-12h-8l1-8z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                      </svg>
                      <span>Instant Preview</span>
                    </div>
                    <div class="speed-feature">
                      <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
                        <path d="M12 2v20M17 5H9.5a3.5 3.5 0 000 7h5a3.5 3.5 0 010 7H6" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                      </svg>
                      <span>No Rate Limits</span>
                    </div>
                    <div class="speed-feature">
                      <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
                        <circle cx="12" cy="12" r="10" stroke="currentColor" stroke-width="2"/>
                        <path d="M12 6v6l4 2" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
                      </svg>
                      <span>Real-time Updates</span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Features Section -->
    <section class="features" id="about-hastecv">
      <div class="center">
        <div class="section-header">
          <h2 class="section-title">Powerful Features</h2>
          <p class="section-description">
            Everything you need to create a standout resume
          </p>
        </div>

        <div class="features-grid">
          <div v-for="(feature, index) in features" :key="index" class="feature-card">
            <div class="feature-icon" :style="{ background: feature.gradient }">
              <component :is="feature.icon" />
            </div>
            <div class="feature-content">
              <h3 class="feature-title">{{ feature.title }}</h3>
              <p class="feature-description">{{ feature.description }}</p>
              <ul v-if="feature.benefits" class="feature-benefits">
                <li v-for="(benefit, i) in feature.benefits" :key="i">
                  <svg width="16" height="16" viewBox="0 0 16 16" fill="none">
                    <path d="M13.3333 4L6 11.3333L2.66667 8" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                  </svg>
                  {{ benefit }}
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- How it Works - Interactive -->
    <section class="how-it-works-interactive">
      <div class="center">
        <div class="section-header">
          <h2 class="section-title">From Zero to Hired in 4 Steps</h2>
          <p class="section-description">
            Simple, fast, and effective. No learning curve required.
          </p>
        </div>

        <div class="steps-container">
          <div 
            v-for="(step, index) in workflowSteps" 
            :key="index"
            class="step-card"
            :class="{ active: activeStep === index }"
            @mouseenter="activeStep = index"
            :ref="el => stepCards[index] = el"
          >
            <div class="step-number">{{ index + 1 }}</div>
            <div class="step-icon">
              <component :is="step.icon" />
            </div>
            <h3 class="step-title">{{ step.title }}</h3>
            <p class="step-description">{{ step.description }}</p>
            <div class="step-tech" v-if="step.tech">
              <span v-for="tech in step.tech" :key="tech" class="tech-badge">{{ tech }}</span>
            </div>
            <div class="step-connector" v-if="index < workflowSteps.length - 1">
              <svg width="40" height="40" viewBox="0 0 40 40">
                <path d="M5 20 L35 20" stroke="currentColor" stroke-width="2" stroke-dasharray="4 4"/>
                <path d="M30 15 L35 20 L30 25" stroke="currentColor" stroke-width="2"/>
              </svg>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Tech Stack Showcase -->
    <section class="tech-stack-section">
      <div class="center">
        <div class="section-header">
          <h2 class="section-title">Built with Modern Tech</h2>
          <p class="section-description">
            Full-stack portfolio project showcasing best practices & scalable architecture
          </p>
        </div>

        <div class="tech-grid">
          <div v-for="(tech, index) in techStack" :key="index" class="tech-item">
            <div class="tech-logo" :style="{ background: tech.gradient }">
              <span class="tech-name">{{ tech.name }}</span>
            </div>
            <div class="tech-role">{{ tech.role }}</div>
          </div>
        </div>

        <div class="architecture-diagram">
          <div class="arch-box frontend">
            <h4>Frontend</h4>
            <p>Vue 3 + Vite</p>
            <span class="deployment">Deployed on Vercel</span>
          </div>
          <div class="arch-arrow">
            <svg width="60" height="40" viewBox="0 0 60 40">
              <path d="M5 20 H55" stroke="#ef4444" stroke-width="2"/>
              <path d="M50 15 L55 20 L50 25" stroke="#ef4444" stroke-width="2"/>
            </svg>
          </div>
          <div class="arch-box backend">
            <h4>Backend</h4>
            <p>Flask + Python</p>
            <span class="deployment">Deployed on Heroku</span>
          </div>
          <div class="arch-arrow">
            <svg width="60" height="40" viewBox="0 0 60 40">
              <path d="M5 20 H55" stroke="#ef4444" stroke-width="2"/>
              <path d="M50 15 L55 20 L50 25" stroke="#ef4444" stroke-width="2"/>
            </svg>
          </div>
          <div class="arch-box pdf">
            <h4>PDF Engine</h4>
            <p>ReportLab</p>
            <span class="deployment">Python Library</span>
          </div>
        </div>

       
      </div>
    </section>

    <!-- CTA Section -->
    <section class="final-cta">
      <div class="center">
        <div class="cta-content">
          <h2 class="cta-title">Ready to Build Your Resume?</h2>
          <p class="cta-description">
            Join thousands creating ATS-optimized resumes. Free forever, no sign-up required.
          </p>
          <div class="cta-actions">
            <button @click="navigateToApp" class="btn-cta-primary">
              Start Building Now
              <svg width="20" height="20" viewBox="0 0 20 20" fill="none">
                <path d="M7.5 15L12.5 10L7.5 5" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </button>
            <a href="https://github.com/yourusername/hastecv" target="_blank" class="btn-cta-secondary">
              <svg width="20" height="20" viewBox="0 0 20 20" fill="currentColor">
                <path fill-rule="evenodd" d="M10 0C4.477 0 0 4.477 0 10c0 4.42 2.865 8.17 6.839 9.49.5.092.682-.217.682-.482 0-.237-.008-.866-.013-1.7-2.782.603-3.369-1.34-3.369-1.34-.454-1.156-1.11-1.463-1.11-1.463-.908-.62.069-.608.069-.608 1.003.07 1.531 1.03 1.531 1.03.892 1.529 2.341 1.087 2.91.831.092-.646.35-1.086.636-1.336-2.22-.253-4.555-1.11-4.555-4.943 0-1.091.39-1.984 1.029-2.683-.103-.253-.446-1.27.098-2.647 0 0 .84-.269 2.75 1.025A9.578 9.578 0 0110 4.836c.85.004 1.705.114 2.504.336 1.909-1.294 2.747-1.025 2.747-1.025.546 1.377.203 2.394.1 2.647.64.699 1.028 1.592 1.028 2.683 0 3.842-2.339 4.687-4.566 4.935.359.309.678.919.678 1.852 0 1.336-.012 2.415-.012 2.743 0 .267.18.578.688.48C17.137 18.165 20 14.418 20 10c0-5.523-4.477-10-10-10z" clip-rule="evenodd"/>
              </svg>
              View on GitHub
            </a>
          </div>
          <div class="cta-stats">
            <div class="cta-stat">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
                <path d="M20 21v-2a4 4 0 00-4-4H8a4 4 0 00-4 4v2M12 11a4 4 0 100-8 4 4 0 000 8z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
              <span>No account needed</span>
            </div>
            <div class="cta-stat">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
                <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
              <span>Your data stays private</span>
            </div>
            <div class="cta-stat">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
                <path d="M21 15v4a2 2 0 01-2 2H5a2 2 0 01-2-2v-4M7 10l5 5 5-5M12 15V3" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
              <span>Instant PDF download</span>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { useRouter } from "vue-router";
import { onMounted, defineComponent, h, ref } from "vue";
import { gsap } from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";

gsap.registerPlugin(ScrollTrigger);

const router = useRouter();
const cubeContainer = ref(null);
const statCards = ref([]);
const stepCards = ref([]);
const activeDemoTab = ref(0);
const selectedTemplate = ref(0);
const activeStep = ref(0);
const easterEggRevealed = ref(false);
const generationTime = ref(1.6);
const speedProgress = ref(440);

// Feature Icons as inline components
const ThemeIcon = defineComponent({
  render() {
    return h('svg', { width: '32', height: '32', viewBox: '0 0 24 24', fill: 'none', stroke: 'currentColor', 'stroke-width': '2' }, [
      h('circle', { cx: '12', cy: '12', r: '3' }),
      h('path', { d: 'M12 1v6m0 6v6m8.66-5H15m-6 0H3m16.66-5.66l-4.24 4.24m-7.08 0L4.5 6.34m15.16 11.32l-4.24-4.24m-7.08 0L4.5 17.66' })
    ]);
  }
});

const LayoutIcon = defineComponent({
  render() {
    return h('svg', { width: '32', height: '32', viewBox: '0 0 24 24', fill: 'none', stroke: 'currentColor', 'stroke-width': '2' }, [
      h('rect', { x: '3', y: '3', width: '18', height: '18', rx: '2' }),
      h('line', { x1: '3', y1: '9', x2: '21', y2: '9' }),
      h('line', { x1: '9', y1: '21', x2: '9', y2: '9' })
    ]);
  }
});

const EditIcon = defineComponent({
  render() {
    return h('svg', { width: '32', height: '32', viewBox: '0 0 24 24', fill: 'none', stroke: 'currentColor', 'stroke-width': '2' }, [
      h('path', { d: 'M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7' }),
      h('path', { d: 'M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z' })
    ]);
  }
});

const DownloadIcon = defineComponent({
  render() {
    return h('svg', { width: '32', height: '32', viewBox: '0 0 24 24', fill: 'none', stroke: 'currentColor', 'stroke-width': '2' }, [
      h('path', { d: 'M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4' }),
      h('polyline', { points: '7 10 12 15 17 10' }),
      h('line', { x1: '12', y1: '15', x2: '12', y2: '3' })
    ]);
  }
});

const PrivacyIcon = defineComponent({
  render() {
    return h('svg', { width: '32', height: '32', viewBox: '0 0 24 24', fill: 'none', stroke: 'currentColor', 'stroke-width': '2' }, [
      h('path', { d: 'M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z' }),
      h('path', { d: 'M9 12l2 2 4-4' })
    ]);
  }
});

const ATSIcon = defineComponent({
  render() {
    return h('svg', { width: '32', height: '32', viewBox: '0 0 24 24', fill: 'none', stroke: 'currentColor', 'stroke-width': '2' }, [
      h('polyline', { points: '22 12 18 12 15 21 9 3 6 12 2 12' }),
      h('circle', { cx: '12', cy: '12', r: '10' })
    ]);
  }
});

// Live Stats Data
const liveStats = [
  {
    icon: defineComponent({
      render() {
        return h('svg', { width: '32', height: '32', viewBox: '0 0 24 24', fill: 'none', stroke: 'currentColor', 'stroke-width': '2' }, [
          h('path', { d: 'M12 2v20M17 5H9.5a3.5 3.5 0 000 7h5a3.5 3.5 0 010 7H6' })
        ]);
      }
    }),
    value: 100,
    label: 'Free Forever',
    sublabel: 'No hidden costs'
  },
  {
    icon: defineComponent({
      render() {
        return h('svg', { width: '32', height: '32', viewBox: '0 0 24 24', fill: 'none', stroke: 'currentColor', 'stroke-width': '2' }, [
          h('path', { d: 'M13 2L3 14h8l-1 8 10-12h-8l1-8z' })
        ]);
      }
    }),
    value: 1.6,
    label: 'Second Generation',
    sublabel: 'Average time'
  },
  {
    icon: defineComponent({
      render() {
        return h('svg', { width: '32', height: '32', viewBox: '0 0 24 24', fill: 'none', stroke: 'currentColor', 'stroke-width': '2' }, [
          h('path', { d: 'M17 21v-2a4 4 0 00-4-4H5a4 4 0 00-4 4v2' }),
          h('circle', { cx: '9', cy: '7', r: '4' }),
          h('path', { d: 'M23 21v-2a4 4 0 00-3-3.87M16 3.13a4 4 0 010 7.75' })
        ]);
      }
    }),
    value: 5,
    label: 'Theme Options',
    sublabel: 'Professional designs'
  },
  {
    icon: defineComponent({
      render() {
        return h('svg', { width: '32', height: '32', viewBox: '0 0 24 24', fill: 'none', stroke: 'currentColor', 'stroke-width': '2' }, [
          h('polyline', { points: '22 12 18 12 15 21 9 3 6 12 2 12' })
        ]);
      }
    }),
    value: 95,
    label: 'ATS Pass Rate',
    sublabel: 'Tested & verified'
  }
];

// Demo Tabs
const demoTabs = [
  {
    label: 'Templates',
    icon: defineComponent({
      render() {
        return h('svg', { width: '20', height: '20', viewBox: '0 0 24 24', fill: 'none', stroke: 'currentColor', 'stroke-width': '2' }, [
          h('rect', { x: '3', y: '3', width: '18', height: '18', rx: '2' }),
          h('line', { x1: '3', y1: '9', x2: '21', y2: '9' }),
          h('line', { x1: '9', y1: '21', x2: '9', y2: '9' })
        ]);
      }
    })
  },
  {
    label: 'Customization',
    icon: defineComponent({
      render() {
        return h('svg', { width: '20', height: '20', viewBox: '0 0 24 24', fill: 'none', stroke: 'currentColor', 'stroke-width': '2' }, [
          h('circle', { cx: '12', cy: '12', r: '3' }),
          h('path', { d: 'M12 1v6m0 6v6m8.66-5H15m-6 0H3m16.66-5.66l-4.24 4.24m-7.08 0L4.5 6.34m15.16 11.32l-4.24-4.24m-7.08 0L4.5 17.66' })
        ]);
      }
    })
  },
  {
    label: 'Speed',
    icon: defineComponent({
      render() {
        return h('svg', { width: '20', height: '20', viewBox: '0 0 24 24', fill: 'none', stroke: 'currentColor', 'stroke-width': '2' }, [
          h('path', { d: 'M13 2L3 14h8l-1 8 10-12h-8l1-8z' })
        ]);
      }
    })
  }
];

// Available Templates
const availableTemplates = [
  {
    name: 'Executive',
    description: 'Bold and professional for leadership roles',
    gradient: 'linear-gradient(135deg, #1e3a8a, #3b82f6)',
    tags: ['Bold', 'Leadership', 'Corporate']
  },
  {
    name: 'Technical',
    description: 'Clean design perfect for developers and engineers',
    gradient: 'linear-gradient(135deg, #065f46, #10b981)',
    tags: ['Clean', 'Tech', 'Modern']
  },
  {
    name: 'Modern',
    description: 'Contemporary layout with visual hierarchy',
    gradient: 'linear-gradient(135deg, #7c2d12, #ea580c)',
    tags: ['Contemporary', 'Creative', 'Stylish']
  },
  
];

// Customization Options
const customOptions = [
  {
    title: 'Color Themes',
    description: 'Choose from 5 professional color schemes',
    icon: defineComponent({
      render() {
        return h('svg', { width: '24', height: '24', viewBox: '0 0 24 24', fill: 'none', stroke: 'currentColor', 'stroke-width': '2' }, [
          h('circle', { cx: '12', cy: '12', r: '10' }),
          h('path', { d: 'M12 2a7 7 0 100 10' })
        ]);
      }
    }),
    examples: ['Professional Blue', 'Tech Green', 'Creative Orange', 'Royal Purple', 'Classic Gray']
  },
  {
    title: 'Layout Options',
    description: 'Multiple column and section arrangements',
    icon: defineComponent({
      render() {
        return h('svg', { width: '24', height: '24', viewBox: '0 0 24 24', fill: 'none', stroke: 'currentColor', 'stroke-width': '2' }, [
          h('rect', { x: '3', y: '3', width: '18', height: '18', rx: '2' }),
          h('line', { x1: '12', y1: '3', x2: '12', y2: '21' })
        ]);
      }
    }),
    examples: ['Single Column', 'Two Column', 'Sidebar Left', 'Sidebar Right', 'Grid Layout']
  },
  {
    title: 'Spacing Control',
    description: 'Adjust density to fit your content',
    icon: defineComponent({
      render() {
        return h('svg', { width: '24', height: '24', viewBox: '0 0 24 24', fill: 'none', stroke: 'currentColor', 'stroke-width': '2' }, [
          h('line', { x1: '4', y1: '6', x2: '20', y2: '6' }),
          h('line', { x1: '4', y1: '12', x2: '20', y2: '12' }),
          h('line', { x1: '4', y1: '18', x2: '20', y2: '18' })
        ]);
      }
    }),
    examples: ['Compact', 'Normal', 'Relaxed']
  },
  {
    title: 'Multi-Language',
    description: 'Generate resumes in multiple languages',
    icon: defineComponent({
      render() {
        return h('svg', { width: '24', height: '24', viewBox: '0 0 24 24', fill: 'none', stroke: 'currentColor', 'stroke-width': '2' }, [
          h('circle', { cx: '12', cy: '12', r: '10' }),
          h('line', { x1: '2', y1: '12', x2: '22', y2: '12' }),
          h('path', { d: 'M12 2a15.3 15.3 0 014 10 15.3 15.3 0 01-4 10 15.3 15.3 0 01-4-10 15.3 15.3 0 014-10z' })
        ]);
      }
    }),
    examples: ['English', 'Spanish', 'French', 'German', 'Portuguese']
  }
];

// Workflow Steps
const workflowSteps = [
  {
    title: 'Input Data',
    description: 'Use the visual editor or paste JSON for quick setup',
    icon: defineComponent({
      render() {
        return h('svg', { width: '32', height: '32', viewBox: '0 0 24 24', fill: 'none', stroke: 'currentColor', 'stroke-width': '2' }, [
          h('path', { d: 'M11 4H4a2 2 0 00-2 2v14a2 2 0 002 2h14a2 2 0 002-2v-7' }),
          h('path', { d: 'M18.5 2.5a2.121 2.121 0 013 3L12 15l-4 1 1-4 9.5-9.5z' })
        ]);
      }
    }),
    tech: ['Vue 3', 'JSON Editor', 'Form Validation']
  },
  {
    title: 'Customize',
    description: 'Pick your theme, layout, and styling preferences',
    icon: defineComponent({
      render() {
        return h('svg', { width: '32', height: '32', viewBox: '0 0 24 24', fill: 'none', stroke: 'currentColor', 'stroke-width': '2' }, [
          h('circle', { cx: '12', cy: '12', r: '3' }),
          h('path', { d: 'M19.4 15a1.65 1.65 0 00.33 1.82l.06.06a2 2 0 010 2.83 2 2 0 01-2.83 0l-.06-.06a1.65 1.65 0 00-1.82-.33 1.65 1.65 0 00-1 1.51V21a2 2 0 01-2 2 2 2 0 01-2-2v-.09A1.65 1.65 0 009 19.4a1.65 1.65 0 00-1.82.33l-.06.06a2 2 0 01-2.83 0 2 2 0 010-2.83l.06-.06a1.65 1.65 0 00.33-1.82 1.65 1.65 0 00-1.51-1H3a2 2 0 01-2-2 2 2 0 012-2h.09A1.65 1.65 0 004.6 9a1.65 1.65 0 00-.33-1.82l-.06-.06a2 2 0 010-2.83 2 2 0 012.83 0l.06.06a1.65 1.65 0 001.82.33H9a1.65 1.65 0 001-1.51V3a2 2 0 012-2 2 2 0 012 2v.09a1.65 1.65 0 001 1.51 1.65 1.65 0 001.82-.33l.06-.06a2 2 0 012.83 0 2 2 0 010 2.83l-.06.06a1.65 1.65 0 00-.33 1.82V9a1.65 1.65 0 001.51 1H21a2 2 0 012 2 2 2 0 01-2 2h-.09a1.65 1.65 0 00-1.51 1z' })
        ]);
      }
    }),
    tech: ['Pinia Store', 'Real-time Preview', 'Theme System']
  },
  {
    title: 'Generate',
    description: 'Backend processes your data with Python & ReportLab',
    icon: defineComponent({
      render() {
        return h('svg', { width: '32', height: '32', viewBox: '0 0 24 24', fill: 'none', stroke: 'currentColor', 'stroke-width': '2' }, [
          h('polyline', { points: '16 18 22 12 16 6' }),
          h('polyline', { points: '8 6 2 12 8 18' })
        ]);
      }
    }),
    tech: ['Flask API', 'Python', 'ReportLab PDF']
  },
  {
    title: 'Download',
    description: 'Get your professional, ATS-optimized PDF instantly',
    icon: defineComponent({
      render() {
        return h('svg', { width: '32', height: '32', viewBox: '0 0 24 24', fill: 'none', stroke: 'currentColor', 'stroke-width': '2' }, [
          h('path', { d: 'M21 15v4a2 2 0 01-2 2H5a2 2 0 01-2-2v-4' }),
          h('polyline', { points: '7 10 12 15 17 10' }),
          h('line', { x1: '12', y1: '15', x2: '12', y2: '3' })
        ]);
      }
    }),
    tech: ['PDF Response', 'Instant Download', 'No Watermarks']
  }
];

// Tech Stack
const techStack = [
  { name: 'Vue 3', role: 'Frontend Framework', gradient: 'linear-gradient(135deg, #42b883, #35495e)' },
  { name: 'Vite', role: 'Build Tool', gradient: 'linear-gradient(135deg, #646cff, #747bff)' },
  { name: 'Flask', role: 'Backend API', gradient: 'linear-gradient(135deg, #000000, #4B4B4B)' },
  { name: 'Python', role: 'Server Language', gradient: 'linear-gradient(135deg, #306998, #FFD43B)' },
  { name: 'ReportLab', role: 'PDF Generation', gradient: 'linear-gradient(135deg, #D32F2F, #F44336)' },
  { name: 'Pinia', role: 'State Management', gradient: 'linear-gradient(135deg, #ffd859, #ffc107)' },
  { name: 'Tailwind', role: 'CSS Framework', gradient: 'linear-gradient(135deg, #06b6d4, #0891b2)' },
  { name: 'GSAP', role: 'Animations', gradient: 'linear-gradient(135deg, #88CE02, #5CB85C)' }
];

const features = [
  {
    title: "Professional Themes",
    description: "Choose from 5 carefully designed professional themes with perfect color contrast.",
    icon: ThemeIcon,
    gradient: 'linear-gradient(135deg, #1E3A8A, #3B82F6)',
    benefits: ['AAA accessibility', 'Industry-specific', 'Customizable colors']
  },
  {
    title: "Flexible Layouts",
    description: "Multiple layout options to match your industry and style preferences.",
    icon: LayoutIcon,
    gradient: 'linear-gradient(135deg, #881337, #BE123C)',
    benefits: ['Single/Multi-column', 'Grid layouts', 'Sidebar options']
  },
  {
    title: "Intuitive Editor",
    description: "Edit your resume with our user-friendly interface or use JSON for advanced control.",
    icon: EditIcon,
    gradient: 'linear-gradient(135deg, #0F766E, #14B8A6)',
    benefits: ['Visual editor', 'JSON support', 'Real-time preview']
  },
  {
    title: "Instant PDF Export",
    description: "Download professional PDF resumes optimized for both ATS systems and human readers.",
    icon: DownloadIcon,
    gradient: 'linear-gradient(135deg, #334155, #64748B)',
    benefits: ['High-quality PDFs', 'ATS-friendly', 'Instant download']
  },
  {
    title: "Complete Privacy",
    description: "Your data stays on your device. We don't collect, store, or share your information.",
    icon: PrivacyIcon,
    gradient: 'linear-gradient(135deg, #065F46, #059669)',
    benefits: ['No data collection', 'No sign-up required', '100% private']
  },
  {
    title: "ATS Optimized",
    description: "Resume structure automatically optimized to pass Applicant Tracking Systems.",
    icon: ATSIcon,
    gradient: 'linear-gradient(135deg, #7C2D12, #C2410C)',
    benefits: ['Keyword friendly', 'Proper formatting', 'Scannable structure']
  }
];

function navigateToApp() {
  router.push("/app");
}

function scrollToExamples() {
  document.getElementById('about-hastecv').scrollIntoView({ behavior: 'smooth' });
}

function activateEasterEgg() {
  easterEggRevealed.value = !easterEggRevealed.value;
  if (easterEggRevealed.value) {
    gsap.from('.riot-tribute', {
      duration: 0.6,
      scale: 0.8,
      opacity: 0,
      ease: 'back.out(1.7)'
    });
  }
}

// Animate stat numbers
function animateStatNumbers() {
  statCards.value.forEach((card, index) => {
    if (!card) return;
    const target = liveStats[index].value;
    const numberEl = card.querySelector('.stat-number');
    
    gsap.to({ val: 0 }, {
      val: target,
      duration: 2,
      ease: 'power2.out',
      delay: index * 0.1,
      onUpdate: function() {
        if (target >= 90) {
          numberEl.textContent = Math.ceil(this.targets()[0].val) + '%';
        } else if (target === 100) {
          numberEl.textContent = Math.ceil(this.targets()[0].val) + '%';
        } else {
          numberEl.textContent = this.targets()[0].val.toFixed(1) + (target < 10 ? 's' : '');
        }
      }
    });
  });
}

onMounted(() => {
  // 3D Cube GSAP Animations - Subtle & Non-intrusive
  if (cubeContainer.value) {
    const cubes = cubeContainer.value.querySelectorAll('.cube');
    const spans = cubeContainer.value.querySelectorAll('span');
    
    // Initial entrance animation - smooth fade in
    gsap.from(cubeContainer.value, {
      duration: 0.7,
      opacity: 0,
      scale: 0.85,
      ease: "power2.out",
      delay: 0.2
    });
    
    // Very slow continuous rotation - almost imperceptible
    gsap.to(cubeContainer.value, {
      duration: 40,
      rotation: 360,
      repeat: -1,
      ease: "none"
    });
    
    // Stagger animation for cubes - subtle
    gsap.from(cubes, {
      duration: 0.8,
      opacity: 0,
      y: 20,
      stagger: 0.15,
      ease: "power2.out",
      delay: 0.5
    });
    
    // Add subtle hover animation to spans
    spans.forEach(span => {
      span.addEventListener('mouseenter', () => {
        gsap.to(span, {
          duration: 0.25,
          scale: 1.05,
          ease: "power2.out"
        });
      });
      
      span.addEventListener('mouseleave', () => {
        gsap.to(span, {
          duration: 0.4,
          scale: 1,
          ease: "power2.out"
        });
      });
    });
    
    // Very subtle floating animation
    gsap.to(cubeContainer.value, {
      duration: 4,
      y: -10,
      repeat: -1,
      yoyo: true,
      ease: "sine.inOut"
    });
  }
  
  // Animate stats when they come into view
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        animateStatNumbers();
        observer.disconnect();
      }
    });
  });
  
  if (statCards.value[0]) {
    observer.observe(statCards.value[0]);
  }
  
  // Animate step cards - faster, earlier, and smoother
  if (stepCards.value.length > 0) {
    // Set initial state immediately
    gsap.set(stepCards.value, { opacity: 1, y: 0 });
    
    // Use the container as trigger instead of individual cards for better performance
    const stepsContainer = stepCards.value[0]?.parentElement;
    if (stepsContainer) {
      stepCards.value.forEach((card, index) => {
        if (!card) return;
        
        gsap.fromTo(card, 
          {
            opacity: 0,
            y: 30
          },
          {
            scrollTrigger: {
              trigger: card,
              start: 'top 90%',
              toggleActions: 'play none none none',
              once: true
            },
            duration: 0.5,
            opacity: 1,
            y: 0,
            delay: index * 0.08,
            ease: 'power3.out'
          }
        );
      });
    }
  }
  
  // Animate speed ring
  gsap.to({ val: 565 }, {
    val: 110,
    duration: 2,
    ease: 'power2.out',
    delay: 1,
    onUpdate: function() {
      speedProgress.value = this.targets()[0].val;
    }
  });
});
</script>

<script>
export default {
  useHead: {
    title: "HasteCV - Professional CV Builder",
    meta: [
      {
        name: "description",
        content:
          "Craft professional, ATS-ready resumes in minutes. HasteCV offers quick, easy, and free CV-building tools."
      },
      {
        name: "keywords",
        content:
          "resume builder, ATS resume, job application, CV builder, resume templates"
      },
      { property: "og:title", content: "HasteCV - Professional CV Builder" },
      {
        property: "og:description",
        content:
          "Create ATS-passing resumes with HasteCV, offering fast and free CV-building tools."
      }
    ]
  }
};
</script>

<style scoped>
.center {
  width: min(100% - 2rem, 1200px);
  margin-inline: auto;
  padding-inline: 1rem;
}

/* Hero Section Styling */
.hero {
  background: var(--primary-black);
  position: relative;
  padding: 5rem 0 6rem;
  overflow: hidden;
}

.hero::before {
  content: '';
  position: absolute;
  top: 0;
  left: 50%;
  transform: translateX(-50%);
  width: 100%;
  max-width: 1400px;
  height: 100%;
  background: radial-gradient(ellipse at top, rgba(var(--haste-primary-rgb), 0.15), transparent 50%);
  pointer-events: none;
}

.hero-content {
  position: relative;
  display: grid;
  grid-template-columns: 1fr auto;
  gap: 4rem;
  align-items: center;
  max-width: 1200px;
  margin: 0 auto;
}

.hero-text-content {
  display: flex;
  flex-direction: column;
  gap: 2rem;
  text-align: left;
  z-index: 2;
}

/* 3D Cube Animation Styling */
.cube-container {
  position: relative;
  width: 320px;
  height: 320px;
  flex-shrink: 0;
  transform-style: preserve-3d;
  perspective: 1000px;
  filter: drop-shadow(0 15px 30px rgba(0, 0, 0, 0.4));
  opacity: 0.85;
}

@keyframes subtleGlow {
  0%, 100% {
    filter: drop-shadow(0 15px 30px rgba(239, 68, 68, 0.2)) brightness(0.9);
  }
  50% {
    filter: drop-shadow(0 15px 40px rgba(239, 68, 68, 0.3)) brightness(1);
  }
}

.cube-container {
  animation: subtleGlow 4s ease-in-out infinite;
}

.cube {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%) skewY(-20deg);
  transform-style: preserve-3d;
  z-index: 2;
}

.cube.cube-1 {
  z-index: 2;
}

.cube.cube-2 {
  z-index: 1;
  transform: translate(-50%, -50%) skewY(-20deg) translate(-60px, -60px);
}

.cube.cube-3 {
  z-index: 3;
  transform: translate(-50%, -50%) skewY(-20deg) translate(60px, 60px);
}

.cube > div {
  position: absolute;
  display: flex;
  flex-direction: column;
  gap: 30px;
  transform: translate(calc(-70px * var(--x)), calc(-60px * var(--y)));
}

.cube span {
  position: relative;
  display: inline-block;
  width: 50px;
  height: 50px;
  background: linear-gradient(135deg, #1e1e1e, #2a2a2a);
  border: 1px solid rgba(239, 68, 68, 0.15);
  z-index: calc(1 * var(--i));
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
  cursor: pointer;
  box-shadow: 
    0 2px 8px rgba(0, 0, 0, 0.3),
    inset 0 1px 0 rgba(255, 255, 255, 0.03);
}

.cube span:hover {
  background: linear-gradient(135deg, #ef4444, #f87171);
  border-color: #ef4444;
  transform: scale(1.08);
  box-shadow: 
    0 0 25px rgba(239, 68, 68, 0.5),
    0 0 40px rgba(239, 68, 68, 0.3),
    inset 0 0 15px rgba(255, 255, 255, 0.2);
  filter: brightness(1.15);
}

.cube span:hover::before,
.cube span:hover::after {
  background: linear-gradient(135deg, #dc2626, #ef4444);
  border-color: rgba(239, 68, 68, 0.4);
  box-shadow: 0 0 15px rgba(239, 68, 68, 0.3);
}

.cube span::before {
  content: "";
  position: absolute;
  left: -40px;
  width: 40px;
  height: 100%;
  background: linear-gradient(135deg, #0a0a0a, #1a1a1a);
  border: 1px solid rgba(239, 68, 68, 0.1);
  transform-origin: right;
  transform: skewY(45deg);
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
  box-shadow: inset -2px 0 8px rgba(0, 0, 0, 0.4);
}

.cube span::after {
  content: "";
  position: absolute;
  top: -40px;
  left: 0;
  width: 100%;
  height: 40px;
  background: linear-gradient(135deg, #252525, #333333);
  border: 1px solid rgba(239, 68, 68, 0.1);
  transform-origin: bottom;
  transform: skewX(45deg);
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
  box-shadow: inset 0 -2px 8px rgba(0, 0, 0, 0.3);
}

/* Add subtle glow effect on container */
.cube-container::before {
  content: '';
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 140%;
  height: 140%;
  background: radial-gradient(circle, rgba(239, 68, 68, 0.08), transparent 65%);
  pointer-events: none;
  z-index: -1;
}

.hero-badge {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.5rem 1rem;
  background: var(--gray-800);
  border: 1px solid var(--border-color);
  border-radius: 9999px;
  font-size: 0.875rem;
  font-weight: 500;
  color: var(--gray-300);
  width: fit-content;
  margin: 0 auto;
}

.badge-dot {
  width: 8px;
  height: 8px;
  background: var(--haste-primary);
  border-radius: 50%;
  animation: pulse 2s infinite;
}

@keyframes pulse {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.5; }
}

.hero-title {
  font-size: clamp(2.5rem, 5vw, 3.5rem);
  font-weight: 800;
  line-height: 1.1;
  letter-spacing: -0.02em;
  color: white;
  margin: 0;
}

.title-highlight {
  display: block;
  background: linear-gradient(135deg, #ef4444, #f87171);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.hero-description {
  font-size: 1.125rem;
  line-height: 1.7;
  color: var(--gray-300);
  max-width: 550px;
  margin: 0;
}

.hero-actions {
  display: flex;
  gap: 1rem;
  justify-content: flex-start;
  flex-wrap: wrap;
}

.btn-primary {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 1rem 2rem;
  background: var(--haste-primary);
  color: white;
  border: none;
  border-radius: 8px;
  font-weight: 600;
  font-size: 1rem;
  cursor: pointer;
  transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
  box-shadow: 0 4px 12px rgba(var(--haste-primary-rgb), 0.3);
}

.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(var(--haste-primary-rgb), 0.4);
}

.btn-primary:active {
  transform: translateY(0);
}

.btn-secondary {
  padding: 1rem 2rem;
  background: transparent;
  color: white;
  border: 2px solid var(--border-color);
  border-radius: 8px;
  font-weight: 600;
  font-size: 1rem;
  cursor: pointer;
  transition: all 0.2s;
}

.btn-secondary:hover {
  border-color: var(--haste-primary);
  color: var(--haste-primary);
  background: rgba(var(--haste-primary-rgb), 0.1);
}

.hero-stats {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 2rem;
  padding: 2rem;
  background: var(--gray-900);
  border: 1px solid var(--border-color);
  border-radius: 12px;
  flex-wrap: wrap;
  width: max-content;
  max-width: 100%;
}

.stat-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.25rem;
}

.stat-value {
  font-size: 1.75rem;
  font-weight: 700;
  color: var(--haste-primary);
  line-height: 1;
}

.stat-label {
  font-size: 0.875rem;
  color: var(--gray-400);
  font-weight: 500;
}

.stat-divider {
  width: 1px;
  height: 40px;
  background: var(--border-color);
}

/* Live Stats Section */
.stats-showcase {
  padding: 4rem 0;
  background: var(--gray-900);
  border-top: 1px solid var(--border-color);
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 2rem;
}

.stat-card {
  background: linear-gradient(135deg, var(--gray-800), var(--primary-black));
  border: 1px solid var(--border-color);
  border-radius: 16px;
  padding: 2rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1rem;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  position: relative;
  overflow: hidden;
}

.stat-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: radial-gradient(circle at top, rgba(239, 68, 68, 0.1), transparent);
  opacity: 0;
  transition: opacity 0.3s;
}

.stat-card:hover::before {
  opacity: 1;
}

.stat-card:hover {
  transform: translateY(-4px);
  border-color: rgba(239, 68, 68, 0.5);
  box-shadow: 0 12px 24px rgba(239, 68, 68, 0.2);
}

.stat-icon-wrapper {
  width: 64px;
  height: 64px;
  border-radius: 12px;
  background: linear-gradient(135deg, #ef4444, #dc2626);
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
}

.stat-icon {
  filter: drop-shadow(0 2px 4px rgba(0, 0, 0, 0.2));
}

.stat-number {
  font-size: 3rem;
  font-weight: 800;
  background: linear-gradient(135deg, #ef4444, #f87171);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  line-height: 1;
}

.stat-label {
  font-size: 1.125rem;
  font-weight: 600;
  color: white;
  text-align: center;
}

.stat-sublabel {
  font-size: 0.875rem;
  color: var(--gray-400);
  text-align: center;
}

/* Demo Section */
.demo-section {
  padding: 5rem 0;
  background: var(--primary-black);
}

.badge-pill {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.5rem 1.25rem;
  background: rgba(239, 68, 68, 0.1);
  border: 1px solid rgba(239, 68, 68, 0.3);
  border-radius: 9999px;
  font-size: 0.875rem;
  font-weight: 600;
  color: #ef4444;
  margin-bottom: 1rem;
}

.badge-dot {
  width: 8px;
  height: 8px;
  background: #ef4444;
  border-radius: 50%;
  animation: pulse 2s infinite;
}

.demo-container {
  margin-top: 3rem;
  background: var(--gray-900);
  border: 1px solid var(--border-color);
  border-radius: 16px;
  overflow: hidden;
}

.demo-tabs {
  display: flex;
  border-bottom: 1px solid var(--border-color);
  background: var(--gray-800);
}

.demo-tab {
  flex: 1;
  padding: 1.25rem 2rem;
  background: transparent;
  border: none;
  color: var(--gray-400);
  font-weight: 600;
  font-size: 1rem;
  cursor: pointer;
  transition: all 0.2s;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.75rem;
  border-bottom: 3px solid transparent;
}

.demo-tab:hover {
  color: white;
  background: rgba(239, 68, 68, 0.05);
}

.demo-tab.active {
  color: #ef4444;
  background: rgba(239, 68, 68, 0.1);
  border-bottom-color: #ef4444;
}

.tab-icon {
  flex-shrink: 0;
}

.demo-content {
  padding: 3rem;
  min-height: 400px;
}

.demo-panel {
  animation: fadeIn 0.3s ease-out;
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* Templates Showcase */
.templates-showcase {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1.5rem;
}

.template-card {
  background: var(--gray-800);
  border: 2px solid var(--border-color);
  border-radius: 12px;
  padding: 1.5rem;
  cursor: pointer;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  position: relative;
}

.template-card:hover {
  transform: translateY(-4px);
  border-color: rgba(239, 68, 68, 0.5);
  box-shadow: 0 12px 24px rgba(0, 0, 0, 0.3);
}

.template-card.selected {
  border-color: #ef4444;
  box-shadow: 0 0 0 3px rgba(239, 68, 68, 0.2);
}

.template-preview {
  margin-bottom: 1rem;
}

.template-thumbnail {
  height: 180px;
  border-radius: 8px;
  padding: 1.5rem;
  display: flex;
  align-items: center;
  justify-content: center;
}

.template-lines {
  width: 100%;
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.template-lines .line {
  height: 12px;
  background: rgba(255, 255, 255, 0.3);
  border-radius: 4px;
}

.template-lines .line:nth-child(1) {
  width: 80%;
}

.template-lines .line:nth-child(2) {
  width: 100%;
}

.template-lines .line:nth-child(3) {
  width: 90%;
}

.template-lines .line:nth-child(4) {
  width: 70%;
}

.template-lines .line:nth-child(5) {
  width: 85%;
}

.template-info h4 {
  font-size: 1.125rem;
  font-weight: 700;
  color: white;
  margin: 0 0 0.5rem;
}

.template-info p {
  font-size: 0.9375rem;
  color: var(--gray-400);
  margin: 0 0 1rem;
}

.template-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
}

.tag {
  padding: 0.375rem 0.75rem;
  background: rgba(239, 68, 68, 0.1);
  border: 1px solid rgba(239, 68, 68, 0.3);
  border-radius: 6px;
  font-size: 0.75rem;
  font-weight: 600;
  color: #ef4444;
}

.selected-badge {
  position: absolute;
  top: 1rem;
  right: 1rem;
  width: 32px;
  height: 32px;
  background: #ef4444;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  box-shadow: 0 4px 12px rgba(239, 68, 68, 0.4);
}

/* Customization Showcase */
.customization-showcase {
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

.custom-option {
  background: var(--gray-800);
  border: 1px solid var(--border-color);
  border-radius: 12px;
  padding: 2rem;
}

.option-header {
  display: flex;
  align-items: flex-start;
  gap: 1rem;
  margin-bottom: 1.5rem;
}

.option-icon {
  flex-shrink: 0;
  color: #ef4444;
}

.option-header h4 {
  font-size: 1.125rem;
  font-weight: 700;
  color: white;
  margin: 0 0 0.375rem;
}

.option-header p {
  font-size: 0.9375rem;
  color: var(--gray-400);
  margin: 0;
}

.option-examples {
  display: flex;
  flex-wrap: wrap;
  gap: 0.75rem;
}

.example-chip {
  padding: 0.625rem 1.25rem;
  background: rgba(239, 68, 68, 0.05);
  border: 1px solid rgba(239, 68, 68, 0.2);
  border-radius: 8px;
  font-size: 0.875rem;
  font-weight: 500;
  color: var(--gray-300);
  transition: all 0.2s;
  cursor: pointer;
}

.example-chip:hover {
  background: rgba(239, 68, 68, 0.1);
  border-color: rgba(239, 68, 68, 0.4);
  color: white;
  transform: translateY(-2px);
}

/* Speed Showcase */
.speed-showcase {
  display: flex;
  justify-content: center;
  align-items: center;
}

.speed-metric {
  text-align: center;
  max-width: 500px;
}

.metric-visual {
  margin-bottom: 2rem;
  display: flex;
  justify-content: center;
}

.progress-ring {
  position: relative;
}

.progress-ring svg {
  transform: rotate(-90deg);
}

.progress-ring circle {
  fill: none;
  stroke-width: 8;
}

.progress-ring circle:first-child {
  stroke: var(--border-color);
}

.progress-ring circle:last-child {
  stroke: #ef4444;
  stroke-dasharray: 565;
  stroke-dashoffset: 565;
  stroke-linecap: round;
  transition: stroke-dashoffset 1s ease-out;
}

.metric-value {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  display: flex;
  flex-direction: column;
  align-items: center;
}

.big-number {
  font-size: 3rem;
  font-weight: 800;
  background: linear-gradient(135deg, #ef4444, #f87171);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  line-height: 1;
}

.unit {
  font-size: 0.875rem;
  color: var(--gray-400);
  margin-top: 0.25rem;
}

.speed-metric h3 {
  font-size: 1.5rem;
  font-weight: 700;
  color: white;
  margin: 0 0 0.5rem;
}

.speed-metric p {
  font-size: 1rem;
  color: var(--gray-400);
  margin: 0 0 2rem;
}

.speed-features {
  display: flex;
  justify-content: center;
  gap: 2rem;
  flex-wrap: wrap;
}

.speed-feature {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 0.75rem 1.25rem;
  background: var(--gray-800);
  border: 1px solid var(--border-color);
  border-radius: 8px;
  color: var(--gray-300);
  font-size: 0.9375rem;
  font-weight: 500;
}

.speed-feature svg {
  color: #ef4444;
  flex-shrink: 0;
}

/* Features Section */
.features {
  padding: 5rem 0;
  background: var(--gray-900);
}

.section-header {
  text-align: center;
  margin-bottom: 3rem;
}

.section-title {
  font-size: 2.5rem;
  font-weight: 700;
  color: white;
  margin: 0 0 1rem;
  letter-spacing: -0.02em;
}

.section-description {
  font-size: 1.125rem;
  color: var(--gray-400);
  max-width: 600px;
  margin: 0 auto;
}

.features-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  gap: 1.5rem;
}

.feature-card {
  background: var(--gray-800);
  border: 1px solid var(--border-color);
  border-radius: 12px;
  padding: 1.5rem;
  display: flex;
  flex-direction: column;
  gap: 1rem;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.feature-card:hover {
  transform: translateY(-4px);
  border-color: var(--haste-primary);
  box-shadow: 0 12px 24px rgba(0, 0, 0, 0.3);
}

.feature-icon {
  width: 56px;
  height: 56px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  flex-shrink: 0;
}

.feature-content {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
  flex: 1;
}

.feature-title {
  font-size: 1.25rem;
  font-weight: 600;
  color: white;
  margin: 0;
  letter-spacing: -0.01em;
}

.feature-description {
  font-size: 0.9375rem;
  color: var(--gray-400);
  line-height: 1.6;
  margin: 0;
}

.feature-benefits {
  list-style: none;
  padding: 0;
  margin: 0.5rem 0 0;
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.feature-benefits li {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.875rem;
  color: var(--gray-300);
}

.feature-benefits li svg {
  flex-shrink: 0;
  color: var(--haste-primary);
}

/* Workflow Steps */
.how-it-works-interactive {
  padding: 5rem 0;
  background: var(--gray-900);
}

.steps-container {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1.5rem;
  position: relative;
  max-width: 1400px;
  margin: 0 auto;
}

@media (max-width: 1200px) {
  .steps-container {
    grid-template-columns: repeat(2, 1fr);
  }
}

.step-card {
  background: var(--gray-800);
  border: 2px solid var(--border-color);
  border-radius: 16px;
  padding: 2.5rem 2rem 2rem;
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  gap: 1.25rem;
  min-height: 380px;
}

.step-card:hover,
.step-card.active {
  transform: translateY(-8px) scale(1.02);
  border-color: #ef4444;
  box-shadow: 0 20px 40px rgba(239, 68, 68, 0.2);
  background: linear-gradient(135deg, var(--gray-800), rgba(239, 68, 68, 0.05));
}

.step-number {
  position: absolute;
  top: -15px;
  left: 50%;
  transform: translateX(-50%);
  width: 40px;
  height: 40px;
  background: linear-gradient(135deg, #ef4444, #dc2626);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.25rem;
  font-weight: 800;
  color: white;
  box-shadow: 0 4px 12px rgba(239, 68, 68, 0.4);
}

.step-icon {
  width: 72px;
  height: 72px;
  color: #ef4444;
  flex-shrink: 0;
  display: flex;
  align-items: center;
  justify-content: center;
}

.step-icon svg {
  width: 100%;
  height: 100%;
}

.step-title {
  font-size: 1.25rem;
  font-weight: 700;
  color: white;
  margin: 0;
  line-height: 1.3;
}

.step-description {
  font-size: 0.9375rem;
  color: var(--gray-400);
  line-height: 1.6;
  margin: 0;
  flex: 1;
}

.step-tech {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  justify-content: center;
  margin-top: auto;
}

.tech-badge {
  padding: 0.375rem 0.75rem;
  background: rgba(239, 68, 68, 0.1);
  border: 1px solid rgba(239, 68, 68, 0.3);
  border-radius: 6px;
  font-size: 0.75rem;
  font-weight: 600;
  color: #ef4444;
}

.step-connector {
  position: absolute;
  top: 100px;
  right: -1.25rem;
  color: var(--border-color);
  z-index: 1;
}

@media (max-width: 1200px) {
  .step-card:nth-child(2) .step-connector {
    display: none;
  }
  
  .step-card:nth-child(4) .step-connector {
    display: none;
  }
}

/* Tech Stack Section */
.tech-stack-section {
  padding: 5rem 0;
  background: var(--primary-black);
}

.tech-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
  gap: 1.5rem;
  margin-bottom: 4rem;
}

.tech-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.75rem;
}

.tech-logo {
  width: 80px;
  height: 80px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.3s;
  cursor: pointer;
}

.tech-logo:hover {
  transform: translateY(-4px) rotate(5deg);
  box-shadow: 0 8px 20px rgba(239, 68, 68, 0.3);
}

.tech-name {
  font-size: 1rem;
  font-weight: 700;
  color: white;
}

.tech-role {
  font-size: 0.8125rem;
  color: var(--gray-400);
  text-align: center;
}

/* Architecture Diagram */
.architecture-diagram {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 1rem;
  flex-wrap: wrap;
  padding: 3rem;
  background: var(--gray-900);
  border: 1px solid var(--border-color);
  border-radius: 16px;
  margin-bottom: 3rem;
}

.arch-box {
  padding: 1.5rem 2rem;
  background: var(--gray-800);
  border: 2px solid var(--border-color);
  border-radius: 12px;
  min-width: 180px;
  text-align: center;
  transition: all 0.3s;
}

.arch-box:hover {
  border-color: #ef4444;
  transform: translateY(-4px);
  box-shadow: 0 8px 20px rgba(239, 68, 68, 0.2);
}

.arch-box h4 {
  font-size: 1.125rem;
  font-weight: 700;
  color: white;
  margin: 0 0 0.5rem;
}

.arch-box p {
  font-size: 0.9375rem;
  color: var(--gray-300);
  margin: 0 0 0.75rem;
}

.deployment {
  display: inline-block;
  padding: 0.375rem 0.75rem;
  background: rgba(239, 68, 68, 0.1);
  border: 1px solid rgba(239, 68, 68, 0.3);
  border-radius: 6px;
  font-size: 0.75rem;
  font-weight: 600;
  color: #ef4444;
}

.arch-arrow {
  flex-shrink: 0;
}

/* Easter Egg */
.easter-egg-container {
  display: flex;
  justify-content: center;
  margin-top: 3rem;
}

.easter-egg {
  position: relative;
  width: 120px;
  height: 120px;
  cursor: pointer;
  transition: transform 0.6s;
  transform-style: preserve-3d;
}

.easter-egg.revealed {
  transform: rotateY(180deg);
}

.egg-front,
.egg-back {
  position: absolute;
  width: 100%;
  height: 100%;
  backface-visibility: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 16px;
}

.egg-front {
  background: linear-gradient(135deg, #ef4444, #dc2626);
  border: 2px solid rgba(255, 255, 255, 0.2);
  box-shadow: 0 8px 24px rgba(239, 68, 68, 0.4);
}

.hint-text {
  font-size: 1.5rem;
  color: white;
  font-weight: 600;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
}

.egg-back {
  background: linear-gradient(135deg, #1a1a1a, #2a2a2a);
  border: 2px solid #ef4444;
  transform: rotateY(180deg);
  padding: 1rem;
}

.riot-tribute {
  text-align: center;
  color: white;
}

.tribute-icon {
  font-size: 2rem;
  margin-bottom: 0.5rem;
}

.tribute-text {
  font-size: 0.8125rem;
  font-weight: 600;
  color: #ef4444;
  margin: 0 0 0.5rem;
  line-height: 1.4;
}

.tribute-sub {
  font-size: 0.75rem;
  color: var(--gray-400);
  margin: 0;
}

/* Final CTA */
.final-cta {
  padding: 6rem 0;
  background: linear-gradient(135deg, #1a1a1a, #0a0a0a);
  border-top: 1px solid var(--border-color);
}

.cta-content {
  text-align: center;
  max-width: 800px;
  margin: 0 auto;
}

.cta-title {
  font-size: clamp(2rem, 4vw, 3rem);
  font-weight: 800;
  color: white;
  margin: 0 0 1rem;
  background: linear-gradient(135deg, white, #ef4444);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.cta-description {
  font-size: 1.125rem;
  color: var(--gray-400);
  margin: 0 0 2.5rem;
  line-height: 1.7;
}

.cta-actions {
  display: flex;
  gap: 1rem;
  justify-content: center;
  flex-wrap: wrap;
  margin-bottom: 3rem;
}

.btn-cta-primary {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 1.25rem 2.5rem;
  background: linear-gradient(135deg, #ef4444, #dc2626);
  color: white;
  border: none;
  border-radius: 12px;
  font-weight: 700;
  font-size: 1.125rem;
  cursor: pointer;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  box-shadow: 0 8px 24px rgba(239, 68, 68, 0.4);
}

.btn-cta-primary:hover {
  transform: translateY(-4px);
  box-shadow: 0 12px 32px rgba(239, 68, 68, 0.5);
}

.btn-cta-secondary {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 1.25rem 2.5rem;
  background: transparent;
  color: white;
  border: 2px solid var(--border-color);
  border-radius: 12px;
  font-weight: 700;
  font-size: 1.125rem;
  text-decoration: none;
  cursor: pointer;
  transition: all 0.3s;
}

.btn-cta-secondary:hover {
  border-color: #ef4444;
  background: rgba(239, 68, 68, 0.1);
  transform: translateY(-4px);
}

.cta-stats {
  display: flex;
  justify-content: center;
  gap: 3rem;
  flex-wrap: wrap;
}

.cta-stat {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  color: var(--gray-400);
  font-size: 0.9375rem;
}

.cta-stat svg {
  color: #ef4444;
  flex-shrink: 0;
}

@media (max-width: 1024px) {
  .hero-content {
    grid-template-columns: 1fr;
    gap: 3rem;
  }
  
  .cube-container {
    width: 280px;
    height: 280px;
    margin: 0 auto;
    order: -1;
  }
  
  .hero-text-content {
    text-align: center;
  }
  
  .hero-title,
  .hero-description {
    text-align: center;
  }
  
  .hero-description {
    margin: 0 auto;
  }
  
  .hero-actions {
    justify-content: center;
  }
}

@media (max-width: 768px) {
  .features-grid {
    grid-template-columns: 1fr;
  }
  
  .section-title {
    font-size: 2rem;
  }
  
  .hero-title {
    font-size: 2.5rem;
  }
  
  .hero-stats {
    gap: 1rem;
  }
  
  .stat-divider {
    display: none;
  }
  
  /* Mobile cube adjustments */
  .cube-container {
    width: 220px;
    height: 220px;
    margin: 0 auto;
  }
  
  .cube span {
    width: 38px;
    height: 38px;
  }
  
  .cube > div {
    gap: 22px;
    transform: translate(calc(-52px * var(--x)), calc(-46px * var(--y)));
  }
  
  .cube span::before {
    left: -30px;
    width: 30px;
  }
  
  .cube span::after {
    top: -30px;
    height: 30px;
  }
  
  .cube.cube-2 {
    transform: translate(-50%, -50%) skewY(-20deg) translate(-45px, -45px);
  }
  
  .cube.cube-3 {
    transform: translate(-50%, -50%) skewY(-20deg) translate(45px, 45px);
  }
  
  /* Mobile demo section */
  .demo-content {
    padding: 1.5rem;
  }
  
  .demo-tabs {
    flex-direction: column;
  }
  
  .demo-tab {
    border-bottom: 1px solid var(--border-color);
    border-right: 3px solid transparent;
  }
  
  .demo-tab.active {
    border-bottom-color: var(--border-color);
    border-right-color: #ef4444;
  }
  
  /* Mobile steps */
  .steps-container {
    grid-template-columns: 1fr;
  }
  
  .step-connector {
    display: none;
  }
  
  /* Mobile tech grid */
  .tech-grid {
    grid-template-columns: repeat(auto-fit, minmax(100px, 1fr));
  }
  
  .tech-logo {
    width: 60px;
    height: 60px;
  }
  
  /* Mobile architecture */
  .architecture-diagram {
    padding: 2rem 1rem;
  }
  
  .arch-arrow svg {
    transform: rotate(90deg);
  }
  
  /* Mobile CTA */
  .cta-actions {
    flex-direction: column;
    align-items: stretch;
  }
  
  .btn-cta-primary,
  .btn-cta-secondary {
    justify-content: center;
  }
  
  .cta-stats {
    flex-direction: column;
    gap: 1.5rem;
    align-items: center;
  }
}

/* How-it-works section styling */
.how-it-works {
  padding: 2rem;
  background: var(--primary-black);
  color: whitesmoke;
  border-top: 2px solid var(--haste-yellow);
}

.how-it-works ol {
  counter-reset: step-counter;
}

.how-it-works li {
  position: relative;
  padding-left: 2.5rem;
}

.how-it-works li::before {
  content: counter(step-counter);
  counter-increment: step-counter;
  position: absolute;
  left: 0;
  top: 0;
  width: 2rem;
  height: 2rem;
  background-color: var(--haste-yellow);
  color: var(--primary-black);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: bold;
}

/* Tips & Resources Section Styling */
.tips-resources {
  padding: 2rem;
  background: var(--primary-black);
  color: whitesmoke;
  border-top: 2px solid var(--haste-yellow);
}

.tips-resources .list-disc li a {
  color: var(--haste-yellow);
  text-decoration: none;
  transition: color 0.3s;
}

.tips-resources .list-disc li a:hover {
  text-decoration: underline;
}

/* JSON Info Card */
.json-info-card {
  margin-top: 2rem;
  padding: 2rem;
  background: var(--gray-900);
  border: 1px solid var(--border-color);
  border-radius: 12px;
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.json-info-header {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.json-info-header svg {
  color: var(--haste-primary);
  flex-shrink: 0;
}

.json-info-header h3 {
  margin: 0;
  font-size: 1.5rem;
  font-weight: 700;
  color: white;
}

.json-info-text {
  margin: 0;
  font-size: 1rem;
  color: var(--gray-400);
  line-height: 1.6;
}

.json-info-features {
  display: flex;
  flex-wrap: wrap;
  gap: 0.75rem;
}

.feature-badge {
  padding: 0.5rem 1rem;
  background: rgba(var(--haste-primary-rgb), 0.1);
  border: 1px solid rgba(var(--haste-primary-rgb), 0.3);
  border-radius: 6px;
  color: var(--haste-primary);
  font-size: 0.875rem;
  font-weight: 600;
}

@media (max-width: 768px) {
  .json-info-card {
    padding: 1.5rem;
  }
  
  .json-info-header {
    flex-direction: column;
    align-items: flex-start;
  }
}
</style>
