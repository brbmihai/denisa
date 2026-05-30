/**
 * Denisa Dragomir — React / CSS-in-JS theme
 * Source: test-ai-gen-web/2__4screens.png
 */

export const denisaDragomirTheme = {
  colors: {
    coal: "#0D0D0B",
    basalt: "#1F211A",
    forestNight: "#2E3427",
    stone: "#D9E2D5",
    sand: "#D5C7B5",
    clay: "#A08B45",
    burntOrange: "#D86A2B",
    alpineMoss: "#6B705F",
    glacierFog: "#DDE2E3",
    white: "#FAF9F6",
    paper: "#FAF8F4",
    background: {
      dark: "#0D0D0B",
      darkElevated: "#1F211A",
      light: "#D9E2D5",
      paper: "#D5C7B5",
    },
    text: {
      primary: "#0D0D0B",
      onDark: "#FAF9F6",
      muted: "#6B705F",
      accent: "#D86A2B",
    },
  },
  fonts: {
    display: '"Cormorant Garamond", Georgia, serif',
    body: '"Inter", system-ui, sans-serif',
  },
  fontSizes: {
    xs: "0.75rem",
    sm: "0.875rem",
    base: "1rem",
    lg: "1.125rem",
    xl: "1.5rem",
    "2xl": "2rem",
    "3xl": "2.5rem",
    "4xl": "3.5rem",
    "5xl": "4.5rem",
    hero: "6rem",
  },
  fontWeights: {
    light: 300,
    regular: 400,
    medium: 500,
    semibold: 600,
  },
  lineHeights: {
    tight: 1.1,
    snug: 1.25,
    normal: 1.5,
    relaxed: 1.65,
  },
  spacing: {
    1: "0.25rem",
    2: "0.5rem",
    3: "0.75rem",
    4: "1rem",
    6: "1.5rem",
    8: "2rem",
    12: "3rem",
    16: "4rem",
    24: "6rem",
    32: "8rem",
    section: "5rem",
    sectionLg: "7.5rem",
  },
  radii: {
    none: 0,
    sm: "4px",
    md: "8px",
    full: "9999px",
  },
  shadows: {
    polaroid: "0 8px 32px oklch(0.13 0.012 85 / 0.12)",
    card: "0 8px 32px rgba(13, 13, 11, 0.25)",
  },
  breakpoints: {
    sm: "640px",
    md: "768px",
    lg: "1024px",
    xl: "1280px",
    "2xl": "1440px",
  },
  components: {
    buttonPrimary: {
      backgroundColor: "#D86A2B",
      color: "#FAF9F6",
      padding: "12px 28px",
      fontFamily: '"Inter", sans-serif',
      fontWeight: 600,
      fontSize: "0.875rem",
      border: "none",
      cursor: "pointer",
      transition: "background-color 200ms ease",
      hover: { backgroundColor: "#c25f26" },
    },
    buttonSecondary: {
      backgroundColor: "transparent",
      color: "#0D0D0B",
      padding: "12px 28px",
      border: "1px solid #0D0D0B",
      fontFamily: '"Inter", sans-serif',
      fontWeight: 500,
    },
    stat: {
      borderTop: "2px solid #D86A2B",
      color: "#0D0D0B",
      paddingBlock: "0.5rem",
    },
  },
};

export default denisaDragomirTheme;
