/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{js,ts,jsx,tsx,html}"],
  theme: {
    screens: {
      sm: "640px",
      md: "768px",   /* tablet */
      lg: "1024px",  /* desktop */
      xl: "1280px",  /* wide */
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
        "burnt-orange": "#D86A2B",
        "alpine-moss": "#6B705F",
        "glacier-fog": "#DDE2E3",
        error: "#B33A2C",
        success: "#4A6B4F",
        warning: "#C47D2A",
      },
      fontFamily: {
        display: ['"Cormorant Garamond"', "Georgia", "serif"],
        body: ['"Inter"', "system-ui", "sans-serif"],
        handwritten: ['"Caveat"', "cursive"],
      },
      fontSize: {
        /* Mobile-first — use md: and lg: variants in markup */
        "display-hero": ["2.5rem", { lineHeight: "1.08", letterSpacing: "-0.02em" }],
        "display-xl": ["2rem", { lineHeight: "1.1" }],
        "display-lg": ["1.75rem", { lineHeight: "1.12" }],
        "display-md": ["1.5rem", { lineHeight: "1.15" }],
        "heading-xl": ["1.375rem", { lineHeight: "1.2" }],
        "heading-lg": ["1.25rem", { lineHeight: "1.25" }],
        "heading-md": ["1.125rem", { lineHeight: "1.3" }],
        "heading-sm": ["1rem", { lineHeight: "1.35" }],
        "body-xl": ["1.0625rem", { lineHeight: "1.6" }],
        "body-lg": ["1rem", { lineHeight: "1.6" }],
        body: ["0.9375rem", { lineHeight: "1.65" }],
        "body-sm": ["0.8125rem", { lineHeight: "1.5" }],
        label: ["0.6875rem", { lineHeight: "1.4", letterSpacing: "0.04em" }],
        overline: ["0.6875rem", { lineHeight: "1.3", letterSpacing: "0.12em" }],
        caption: ["0.75rem", { lineHeight: "1.45" }],
        nav: ["0.6875rem", { lineHeight: "1.2", letterSpacing: "0.08em" }],
        "form-title": ["1.5rem", { lineHeight: "1.2" }],
        "form-label": ["0.8125rem", { lineHeight: "1.3", letterSpacing: "0.04em" }],
      },
      letterSpacing: {
        nav: "0.08em",
        overline: "0.12em",
      },
      spacing: {
        section: "3rem",
        "section-md": "4.5rem",
        "section-lg": "6rem",
        gutter: "1rem",
        "gutter-md": "1.5rem",
        "gutter-lg": "2rem",
      },
      maxWidth: {
        content: "75rem",
        narrow: "36rem",
      },
      minHeight: {
        input: "3rem",
        "input-lg": "3.25rem",
      },
      borderRadius: {
        sm: "4px",
        md: "8px",
        lg: "12px",
      },
      boxShadow: {
        polaroid: "0 4px 24px rgba(13, 13, 11, 0.15)",
        card: "0 8px 32px rgba(13, 13, 11, 0.25)",
        focus: "0 0 0 3px rgba(216, 106, 43, 0.35)",
      },
      transitionDuration: {
        slow: "800ms",
      },
    },
  },
  plugins: [],
};
