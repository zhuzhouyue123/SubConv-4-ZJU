import { defineConfig } from "vitepress"
import locales from './locales'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: 'SubConv',
  locales: locales.locales,
  head: [
    ['link', { rel: 'icon', href: '/favicon.png' }],
  ]
})