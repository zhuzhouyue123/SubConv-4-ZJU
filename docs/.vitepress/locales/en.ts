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
      copyright: 'Copyright © 2022-present Geniucker'
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
        { text: 'What is sub-conv', link: '/guide/introduction/what-is-sub-conv' },
        { text: 'Why sub-conv', link: '/guide/introduction/why-sub-conv' },
        { text: 'Getting Started', link: '/guide/introduction/getting-started' }
      ]
    },
    {
      text: 'Deploy',
      collapsed: false,
      items: [
        { text: 'Deploy on Vercel', link: '/guide/deploy/vercel' },
        { text: 'Deploy on VPS or PC', link: '/guide/deploy/vps' }
      ]
    },
    {
      text: 'Configuration',
      collapsed: false,
      items: [
        { text: 'Rule Set', link: '/guide/configuration/rule-set' },
        { text: 'Proxy Groups', link: '/guide/configuration/proxy-groups' },
        { text: 'Cache Rules Automatically', link: '/guide/configuration/cache' }
      ]
    }
  ]
}