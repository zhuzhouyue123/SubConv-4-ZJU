import { defineConfig } from "vitepress"
import locales from './locales'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "sub-conv",
  locales: locales.locales
})