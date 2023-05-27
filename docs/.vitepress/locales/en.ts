import { defineConfig } from 'vitepress'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  lang: 'en-US',
  description: "Yet Another Subscription Converter for Clash",
  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    nav: nav(),
    sidebar: {
      '/guide/': sidebarGuide()
    },
    socialLinks: [
      { icon: 'github', link: 'https://github.com/Geniucker/sub-conv' }
    ],
    editLink: {
      pattern: 'https://github.com/Geniucker/sub-conv/edit/main/docs/:path'
    },
    search: {
      provider: 'local'
    },
    footer: {
      message: 'Released under the MIT License.',
      copyright: 'Copyright © 2022-present <a href="https://github.com/Geniucker" target="_blank">@Geniucker</a>'
    }
  }
})


function nav() {
  return [
    { text: 'Home', link: '/' },
    { text: 'Guide', link: '/guide/introduction/what-is-sub-conv'},
    { text: 'GitHub', link: 'https://github.com/Geniucker/sub-conv'}
  ]
}

function sidebarGuide() {
  return [
    {
      text: 'Introduction',
      collapsed: false,
      items: [
        { text: 'What is sub-conv', link: '../introduction/what-is-sub-conv' },
        { text: 'Why sub-conv', link: '../introduction/why-sub-conv' },
        { text: 'Getting Started', link: '../introduction/getting-started' }
      ]
    },
    {
      text: 'Deploy',
      collapsed: false,
      items: [
        { text: 'Deploy on Vercel', link: '../deploy/vercel' },
        { text: 'Deploy on VPS or PC', link: '../deploy/vps' },
        { text: 'How to Update', link: '../deploy/update' }
      ]
    },
    {
      text: 'Configuration',
      collapsed: false,
      items: [
        { text: 'Rule Set', link: '../configuration/rule-set' },
        { text: 'Proxy Groups', link: '../configuration/proxy-groups' },
        { text: 'Cache Rules Automatically', link: '../configuration/cache' }
      ]
    },
    {
      text: 'Advanced Usage',
      collapsed: false,
      items: [
        { text: 'APIs', link: '../advanced-usage/apis' }
      ]
    }
  ]
}