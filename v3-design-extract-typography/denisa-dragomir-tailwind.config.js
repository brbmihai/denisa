/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{js,ts,jsx,tsx,html}"],
  theme: {
    screens: {
      sm: "640px",
      md: "768px", /* tablet */
      lg: "1024px", /* desktop */
      xl: "1280px", /* wide */
      "2xl": "1440px",
    },
    extend: {
      colors: {
        coal: "#0D0D0B",
        basalt: "#1F211A",
        "forest-night": "#2E3427",
        stone: "#D9E2D5",
        sand: "#D5C7B5",
        clay: "#A08B45",
        gold: "#B87942",
        "burnt-orange": "#D86A2B",
        rust: "#9A4600",
        "alpine-moss": "#6B705F",
        white: "#FAF9F6",
        paper: "#EDE7DC",
        error: "#B33A2C",
        success: "#4A6B4F",
        warning: "#C47D2A",
      },
      fontFamily: {
        display: ['"Cormorant Garamond"', "Georgia", "serif"],
        body: ['"Inter"', "system-ui", "sans-serif"],
        handwritten: ['"Caveat"', "cursive"],
      },
      /* Sizes reference CSS variables — responsive steps live in denisa-dragomir-variables.css */
      fontSize: {
        "display-hero": [
          "var(--text-display-hero-size)",
          { lineHeight: "var(--text-display-hero-lh)", letterSpacing: "var(--text-display-hero-ls)" },
        ],
        "display-xl": [
          "var(--text-display-xl-size)",
          { lineHeight: "var(--text-display-xl-lh)", letterSpacing: "var(--letter-spacing-tight)" },
        ],
        "display-lg": ["var(--text-display-lg-size)", { lineHeight: "var(--text-display-lg-lh)" }],
        "display-md": ["var(--text-display-md-size)", { lineHeight: "var(--text-display-md-lh)" }],
        "heading-xl": ["var(--text-heading-xl-size)", { lineHeight: "var(--text-heading-xl-lh)" }],
        "heading-lg": ["var(--text-heading-lg-size)", { lineHeight: "var(--text-heading-lg-lh)" }],
        "heading-md": ["var(--text-heading-md-size)", { lineHeight: "var(--text-heading-md-lh)" }],
        "heading-sm": ["var(--text-heading-sm-size)", { lineHeight: "var(--text-heading-sm-lh)" }],
        "body-xl": ["var(--text-body-xl-size)", { lineHeight: "var(--text-body-xl-lh)" }],
        "body-lg": ["var(--text-body-lg-size)", { lineHeight: "var(--text-body-lg-lh)" }],
        body: ["var(--text-body-size)", { lineHeight: "var(--text-body-lh)" }],
        "body-sm": ["var(--text-body-sm-size)", { lineHeight: "var(--text-body-sm-lh)" }],
        label: [
          "var(--text-label-size)",
          { lineHeight: "var(--text-label-lh)", letterSpacing: "var(--letter-spacing-wide)" },
        ],
        overline: [
          "var(--text-overline-size)",
          { lineHeight: "var(--text-overline-lh)", letterSpacing: "var(--letter-spacing-overline)" },
        ],
        caption: ["var(--text-caption-size)", { lineHeight: "var(--text-caption-lh)" }],
        nav: [
          "var(--text-nav-size)",
          { lineHeight: "var(--text-nav-lh)", letterSpacing: "var(--letter-spacing-nav)" },
        ],
        button: [
          "var(--text-button-size)",
          { lineHeight: "var(--text-button-lh)", letterSpacing: "var(--letter-spacing-wide)" },
        ],
        quote: ["var(--text-quote-size)", { lineHeight: "var(--text-quote-lh)" }],
        handwritten: ["var(--text-handwritten-size)", { lineHeight: "var(--text-handwritten-lh)" }],
        "polaroid-caption": [
          "var(--text-polaroid-caption-size)",
          { lineHeight: "var(--text-polaroid-caption-lh)" },
        ],
        "stat-num": ["var(--text-stat-num-size)", { lineHeight: "var(--text-stat-num-lh)" }],
        "stat-label": [
          "var(--text-stat-label-size)",
          { lineHeight: "var(--text-stat-label-lh)", letterSpacing: "var(--letter-spacing-wide)" },
        ],
        "form-title": ["var(--text-form-title-size)", { lineHeight: "var(--text-form-title-lh)" }],
        "form-label": [
          "var(--text-form-label-size)",
          { lineHeight: "var(--text-form-label-lh)", letterSpacing: "var(--letter-spacing-wide)" },
        ],
        "form-input": ["var(--text-form-input-size)", { lineHeight: "var(--text-form-input-lh)" }],
        "form-hint": ["var(--text-form-hint-size)", { lineHeight: "var(--text-form-hint-lh)" }],
        "form-error": ["var(--text-form-error-size)", { lineHeight: "var(--text-form-error-lh)" }],
        logo: ["var(--text-logo-size)", { lineHeight: "var(--text-logo-lh)" }],
      },
      letterSpacing: {
        nav: "var(--letter-spacing-nav)",
        overline: "var(--letter-spacing-overline)",
        wide: "var(--letter-spacing-wide)",
        tight: "var(--letter-spacing-tight)",
      },
      spacing: {
        section: "var(--space-section-y)",
        gutter: "var(--space-gutter)",
      },
      maxWidth: {
        content: "var(--content-max-width)",
        narrow: "var(--content-narrow)",
        prose: "36rem",
        "prose-wide": "42rem",
      },
      minHeight: {
        input: "var(--input-height)",
      },
      borderRadius: {
        sm: "var(--radius-sm)",
        md: "var(--radius-md)",
        lg: "var(--radius-lg)",
      },
      boxShadow: {
        polaroid: "var(--shadow-polaroid)",
        card: "var(--shadow-card)",
        focus: "var(--shadow-focus)",
      },
      transitionDuration: {
        slow: "800ms",
      },
    },
  },
  plugins: [],
};
