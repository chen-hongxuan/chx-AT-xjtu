(() => {
  const storageKey = "chx-theme";
  const prefersDark = window.matchMedia("(prefers-color-scheme: dark)").matches;
  const saved = window.localStorage.getItem(storageKey);

  function apply(theme) {
    document.documentElement.dataset.theme = theme;
    window.localStorage.setItem(storageKey, theme);
  }

  apply(saved || (prefersDark ? "dark" : "light"));

  document.addEventListener("DOMContentLoaded", () => {
    const button = document.querySelector("[data-theme-toggle]");
    if (!button) return;
    button.addEventListener("click", () => {
      apply(document.documentElement.dataset.theme === "dark" ? "light" : "dark");
    });
  });
})();
