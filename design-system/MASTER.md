# Vector One Holdings — UI/UX Pro Max Design System

This document serves as the **Global Source of Truth** for all design rules across Vector One Holdings, covering the `index.html` web application, executive deliverables, and internal SaaS dashboards (UCG and EvoMax).

## 1. Core Aesthetic: "Strategic Cyber-Physical"
The design language of Vector One reflects authority, precision, and state-of-the-art intelligence. We reject the "generic AI" look (no pink/purple gradients or flat white walls) in favor of deep contrasts, technical data-viz elements, and structured glassmorphism.

## 2. Color Palette (Tokens)
- **Primary Accent (Cyber Blue):** `hsl(190, 100%, 50%)` / `#00d4ff` (Used for CTAs, active states, and radar UI).
- **Secondary Accent (Emerald AI):** `hsl(160, 84%, 39%)` / `#10b981` (Used for positive telemetry, EvoMax savings indicators).
- **Background (Void Black):** `hsl(216, 60%, 4%)` / `#040b14` (Deepest background layer).
- **Surface (Navy Glass):** `hsl(215, 60%, 10%)` / `rgba(10, 22, 40, 0.7)` (Used for cards and panels, accompanied by background blur).
- **Text (Primary):** `hsl(0, 0%, 95%)` / `#f2f2f2`
- **Text (Muted):** `hsl(215, 20%, 65%)` / `#94a3b8`

## 3. Typography (Google Fonts)
- **Headings (Precision/Brand):** `Outfit`, sans-serif. Weights: 600 (Semi-bold), 700 (Bold).
- **Body/UI (Readability):** `Inter`, sans-serif. Weights: 400 (Regular), 500 (Medium).
- **Data/Telemetry:** `JetBrains Mono` or `Fira Code`. Used for token counts, radar coordinates, and code snippets.

## 4. Spacing & Grid (Bento Box Structure)
- **Base Unit:** 8px.
- **Micro Spacing:** 4px, 8px, 12px (Inner padding of chips/buttons).
- **Component Spacing:** 16px, 24px, 32px (Card padding).
- **Layout Spacing:** 48px, 64px, 96px (Section margins).
- **Grid Pattern:** All dashboards and feature showcases use a structured **Bento Box Grid** layout for modular, scalable information density.

## 5. UI Elements & Micro-Animations
- **Glassmorphism Panels:** 
  - `backdrop-filter: blur(12px)`
  - `border: 1px solid rgba(0, 212, 255, 0.1)`
  - `box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3)`
- **Hover States:** Subtle Y-axis translation (`transform: translateY(-2px)`) accompanied by a faint glow (`box-shadow: 0 0 15px rgba(0, 212, 255, 0.3)`).
- **Icons:** Strict use of professional SVG libraries (Lucide Icons). **No emojis** are to be used in production UI.
- **Accessibility:** All text contrast ratios must meet or exceed WCAG AA standards (4.5:1 for normal text).

## 6. Subsidiary Brand Integration
Each subsidiary shares the master structure but overrides the primary accent color to differentiate their domain:
- **Vector Aero:** Cyan (`#00d4ff`)
- **Vector Compute:** Violet (`#7c3aed`)
- **Vector Intelligence:** Emerald (`#10b981`)
- **Vector Institute:** Amber (`#f59e0b`)
- **Vector MICE:** Red (`#ef4444`)
