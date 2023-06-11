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
      { icon: 'github', link: 'https://github.com/SubConv/SubConv' }
    ],
    editLink: {
      pattern: 'https://github.com/SubConv/SubConv/edit/main/docs/:path'
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
    { text: 'Guide', link: '/guide/introduction/what-is-subconv'},
    { text: 'GitHub', link: 'https://github.com/Geniucker/subconv'}
  ]
}

function sidebarGuide() {
  return [
    {
      text: 'Introduction',
      collapsed: false,
      items: [
        { text: 'What is SubConv', link: '../introduction/what-is-subconv' },
        { text: 'Why SubConv', link: '../introduction/why-subconv' },
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