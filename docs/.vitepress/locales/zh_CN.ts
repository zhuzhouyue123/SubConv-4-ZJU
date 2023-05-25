import { defineConfig } from 'vitepress'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  lang: 'zh-CN',
  description: "又一个 Clash 订阅转换",
  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    nav: nav(),
    sidebar: {
      'zh_CN/guide/': sidebarGuide()
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
      message: '在 MIT 许可证下发布。',
      copyright: 'Copyright © 2022-现在 <a href="https://github.com/Geniucker" target="_blank">@Geniucker</a>'
    }
  }
})


function nav() {
  return [
    { text: '首页', link: '/zh_CN/' },
    { text: '指南', link: '/zh_CN/guide/introduction/what-is-sub-conv'},
    { text: 'GitHub', link: 'https://github.com/Geniucker/sub-conv'}
  ]
}

function sidebarGuide() {
  return [
    {
      text: '简介',
      collapsed: false,
      items: [
        { text: '什么是 sub-conv', link: '/zh_CN/guide/introduction/what-is-sub-conv' },
        { text: '为什么使用 sub-conv', link: '/zh_CN/guide/introduction/why-sub-conv' },
        { text: '开始使用', link: '/zh_CN/guide/introduction/getting-started' }
      ]
    },
    {
      text: '部署',
      collapsed: false,
      items: [
        { text: '在 Vercel 上部署', link: '/zh_CN/guide/deploy/vercel' },
        { text: '在 VPS 或 PC 上部署', link: '/zh_CN/guide/deploy/vps' }
      ]
    },
    {
      text: '配置',
      collapsed: false,
      items: [
        { text: '规则集', link: '/zh_CN/guide/configuration/rule-set' },
        { text: 'Proxy Groups', link: '/zh_CN/guide/configuration/proxy-groups' },
        { text: '规则自动缓存', link: '/zh_CN/guide/configuration/cache' }
      ]
    }
  ]
}